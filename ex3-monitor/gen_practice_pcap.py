#!/usr/bin/env python3
"""Generate a SYNTHETIC practice pcap for Exercise 3 (no real network traffic is sent).

Mixes normal browsing/DNS with three planted attack patterns you should be able to find:
  1. Port scan   : 10.0.0.66 -> 10.0.0.10, SYNs to many ports
  2. SSH brute   : 10.0.0.66 -> 10.0.0.10:22, many short connections
  3. Exfiltration: 10.0.0.25 -> 203.0.113.50:443, unusually large upload

Usage: python3 gen_practice_pcap.py practice.pcap [--seed 1]
Needs: pip install scapy
"""
import argparse
import random

from scapy.all import DNS, DNSQR, IP, TCP, UDP, Ether, Raw, wrpcap  # noqa: E402

SERVER = "10.0.0.10"
ATTACKER = "10.0.0.66"
EXFIL_HOST = "10.0.0.25"
EXFIL_DEST = "203.0.113.50"          # TEST-NET-3, never routable
CLIENTS = [f"10.0.0.{i}" for i in range(20, 40)]
SITES = ["example.com", "intranet.local", "updates.example.org", "cdn.example.net"]


def tcp_session(pkts, t, src, dst, sport, dport, payload_out=b"", payload_in=b"", ok=True):
    """Append a TCP handshake + optional data + teardown. Returns the next timestamp."""
    def add(p, dt=0.001):
        nonlocal t
        p.time = t
        pkts.append(p)
        t += dt
    e = Ether()
    add(e / IP(src=src, dst=dst) / TCP(sport=sport, dport=dport, flags="S", seq=100))
    if not ok:
        add(e / IP(src=dst, dst=src) / TCP(sport=dport, dport=sport, flags="RA", seq=0, ack=101))
        return t
    add(e / IP(src=dst, dst=src) / TCP(sport=dport, dport=sport, flags="SA", seq=500, ack=101))
    add(e / IP(src=src, dst=dst) / TCP(sport=sport, dport=dport, flags="A", seq=101, ack=501))
    seq, ack = 101, 501
    if payload_out:
        for i in range(0, len(payload_out), 1400):
            chunk = payload_out[i:i + 1400]
            add(e / IP(src=src, dst=dst) / TCP(sport=sport, dport=dport, flags="PA", seq=seq, ack=ack) / Raw(chunk))
            seq += len(chunk)
    if payload_in:
        for i in range(0, len(payload_in), 1400):
            chunk = payload_in[i:i + 1400]
            add(e / IP(src=dst, dst=src) / TCP(sport=dport, dport=sport, flags="PA", seq=ack, ack=seq) / Raw(chunk))
            ack += len(chunk)
    add(e / IP(src=src, dst=dst) / TCP(sport=sport, dport=dport, flags="FA", seq=seq, ack=ack))
    add(e / IP(src=dst, dst=src) / TCP(sport=dport, dport=sport, flags="FA", seq=ack, ack=seq + 1))
    return t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    random.seed(a.seed)
    pkts = []
    t = 1_700_000_000.0

    # normal traffic: DNS + HTTPS-sized sessions
    for _ in range(300):
        c = random.choice(CLIENTS)
        site = random.choice(SITES)
        q = Ether() / IP(src=c, dst="10.0.0.2") / UDP(sport=random.randint(40000, 60000), dport=53) / DNS(rd=1, qd=DNSQR(qname=site))
        q.time = t
        pkts.append(q)
        t += 0.01
        t = tcp_session(pkts, t, c, SERVER, random.randint(40000, 60000), random.choice([80, 443]),
                        payload_out=b"GET / HTTP/1.1\r\nHost: " + site.encode() + b"\r\n\r\n",
                        payload_in=b"X" * random.randint(300, 4000))
        t += random.uniform(0.05, 1.5)

    # 1) port scan
    t += 5
    for port in random.sample(range(1, 1025), 400):
        t = tcp_session(pkts, t, ATTACKER, SERVER, 54321, port, ok=(port in (22, 80, 443)))
        t += 0.002

    # 2) SSH brute force
    t += 5
    for _ in range(60):
        t = tcp_session(pkts, t, ATTACKER, SERVER, random.randint(40000, 60000), 22,
                        payload_out=b"SSH-2.0-libssh\r\n" + b"A" * 80, payload_in=b"SSH-2.0-OpenSSH_9.6\r\n")
        t += random.uniform(0.2, 0.6)

    # 3) exfiltration
    t += 5
    t = tcp_session(pkts, t, EXFIL_HOST, EXFIL_DEST, 50500, 443, payload_out=bytes(random.getrandbits(8) for _ in range(900_000)))

    pkts.sort(key=lambda p: p.time)
    wrpcap(a.out, pkts)
    print(f"wrote {len(pkts)} packets to {a.out}")


if __name__ == "__main__":
    main()
