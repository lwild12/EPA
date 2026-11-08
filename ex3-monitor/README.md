# Ex3: Monitoring (traffic, SQL, risk, ISMS)

1. **Install.** `pip install scapy pandas numpy scikit-learn matplotlib tabulate`
2. **Get a pcap.** Use the one in the brief. If none is given, capture traffic between your Kali and Metasploitable VMs in Wireshark (nmap scan, a login attempt, some web requests) and save it.
   No pcap and no VMs? Practise with `python3 gen_practice_pcap.py practice.pcap` (synthetic).
3. **Load it.** `python3 pcap_to_sqlite.py capture.pcap --db traffic.db --csv packets.csv`
4. **Query it.** Open `traffic.db` in DB Browser for SQLite and run each query in `queries.sql`. Screenshot results.
5. **Analyse.** `python3 analysis.py traffic.db --out analysis_out`
   You get `summary.md` plus charts. Expect your own servers to show as heavy senders; that is normal, explain it.
6. **Detect.** Adapt `local.rules` for Snort and run it on the pcap. These rules are untested, so check with `snort -T` first.
7. **Risk and ISMS.** Use `../templates/risk_register.md`, `security_policy_and_isms.md`, `assurance_strategy.md`. Link each finding to a risk row.
8. **Write it up.** For each finding: what, evidence (query and figure), risk score, action.

Practice answer key (synthetic pcap): 10.0.0.66 scans and brute-forces SSH; 10.0.0.25 uploads about 900 KB to 203.0.113.50.
