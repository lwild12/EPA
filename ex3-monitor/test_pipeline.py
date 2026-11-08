"""End-to-end test: synthetic pcap -> SQLite -> queries find the three planted attack patterns.
Run: python3 -m pytest -q test_pipeline.py"""
import os
import sqlite3
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def run(*args):
    return subprocess.run([sys.executable, *args], cwd=HERE, check=True, capture_output=True, text=True)


def test_pipeline_finds_planted_attacks(tmp_path):
    pcap, db, csv = tmp_path / "p.pcap", tmp_path / "t.db", tmp_path / "p.csv"
    run("gen_practice_pcap.py", str(pcap))
    run("pcap_to_sqlite.py", str(pcap), "--db", str(db), "--csv", str(csv))
    con = sqlite3.connect(db)

    scan = con.execute("""SELECT src, COUNT(DISTINCT dport) FROM packets WHERE flags='S'
                          GROUP BY src, dst HAVING COUNT(DISTINCT dport) > 50""").fetchall()
    assert scan and scan[0][0] == "10.0.0.66"

    brute = con.execute("""SELECT src, COUNT(*) FROM packets WHERE flags='S' AND dport=22
                           GROUP BY src HAVING COUNT(*) > 20""").fetchall()
    assert brute and brute[0][0] == "10.0.0.66"

    exfil = con.execute("""SELECT src, SUM(length) FROM packets WHERE dst NOT LIKE '10.%'
                           GROUP BY src ORDER BY 2 DESC LIMIT 1""").fetchone()
    assert exfil[0] == "10.0.0.25" and exfil[1] > 500_000


def test_analysis_runs(tmp_path):
    pcap, db, csv, out = tmp_path / "p.pcap", tmp_path / "t.db", tmp_path / "p.csv", tmp_path / "out"
    run("gen_practice_pcap.py", str(pcap))
    run("pcap_to_sqlite.py", str(pcap), "--db", str(db), "--csv", str(csv))
    res = run("analysis.py", str(db), "--out", str(out))
    assert "10.0.0.66" in res.stdout and "10.0.0.25" in res.stdout
    assert (out / "summary.md").exists() and (out / "clusters.png").exists()
