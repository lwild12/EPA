#!/usr/bin/env python3
"""pcap -> CSV + SQLite for Exercise 3.

Usage: python3 pcap_to_sqlite.py capture.pcap [--db traffic.db] [--csv packets.csv]

Creates tables:
  packets(ts, src, dst, proto, sport, dport, length, flags, dns_query)
  flows(src, dst, dport, proto, packets, bytes, first_ts, last_ts, syn, synack, rst, fin)  (built from packets)
Works with any pcap (including a Wireshark capture). Needs: pip install scapy
"""
import argparse
import csv
import sqlite3

from scapy.all import DNS, DNSQR, IP, TCP, UDP, PcapReader  # noqa: E402

FIELDS = ["ts", "src", "dst", "proto", "sport", "dport", "length", "flags", "dns_query"]


def rows(pcap):
    with PcapReader(pcap) as r:
        for p in r:
            if IP not in p:
                continue
            ip = p[IP]
            proto, sport, dport, flags, q = "OTHER", None, None, "", ""
            if TCP in p:
                proto, sport, dport, flags = "TCP", p[TCP].sport, p[TCP].dport, str(p[TCP].flags)
            elif UDP in p:
                proto, sport, dport = "UDP", p[UDP].sport, p[UDP].dport
                if DNS in p and DNSQR in p and p[DNS].qr == 0:
                    q = p[DNSQR].qname.decode("ascii", "ignore").rstrip(".")
            elif ip.proto == 1:
                proto = "ICMP"
            yield (float(p.time), ip.src, ip.dst, proto, sport, dport, len(p), flags, q)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pcap")
    ap.add_argument("--db", default="traffic.db")
    ap.add_argument("--csv", default="packets.csv")
    a = ap.parse_args()

    data = list(rows(a.pcap))
    with open(a.csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(FIELDS)
        w.writerows(data)

    con = sqlite3.connect(a.db)
    con.executescript("""
        DROP TABLE IF EXISTS packets; DROP TABLE IF EXISTS flows;
        CREATE TABLE packets (ts REAL, src TEXT, dst TEXT, proto TEXT, sport INT, dport INT, length INT, flags TEXT, dns_query TEXT);
        CREATE INDEX idx_src ON packets(src); CREATE INDEX idx_dst ON packets(dst); CREATE INDEX idx_dport ON packets(dport);
    """)
    con.executemany("INSERT INTO packets VALUES (?,?,?,?,?,?,?,?,?)", data)
    con.executescript("""
        CREATE TABLE flows AS
        SELECT src, dst, dport, proto,
               COUNT(*) AS packets, SUM(length) AS bytes, MIN(ts) AS first_ts, MAX(ts) AS last_ts,
               SUM(CASE WHEN flags = 'S'  THEN 1 ELSE 0 END) AS syn,
               SUM(CASE WHEN flags = 'SA' THEN 1 ELSE 0 END) AS synack,
               SUM(CASE WHEN flags LIKE '%R%' THEN 1 ELSE 0 END) AS rst,
               SUM(CASE WHEN flags LIKE '%F%' THEN 1 ELSE 0 END) AS fin
        FROM packets WHERE proto IN ('TCP','UDP') GROUP BY src, dst, dport, proto;
    """)
    con.commit()
    n = con.execute("SELECT COUNT(*) FROM packets").fetchone()[0]
    print(f"{n} packets -> {a.csv}, {a.db}")
    con.close()


if __name__ == "__main__":
    main()
