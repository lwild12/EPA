# EPA kit (Cyber Security Technologist)

Practice scripts and templates for the four practical exercises. Scripts are for use in your own lab/exam VM only.

Start with **GUIDE.md** (what to do on the day). Working on Ex2? Open **EX2_START_HERE.md**. Each exercise folder has its own README with exact steps.

## Layout

| Folder | Exercise | Main files |
|---|---|---|
| `ex1-design/` | Network and web design | `vlsm_calc.py`, `cisco_hardening.md`, `linux_audit.sh`, `php-upload/` |
| `ex2-malware/` | Malware testing | `triage.py`, `rules/*.yar`, `SAMPLE_OPTIONS.md` |
| `ex2-autopsy/` | Forensics evidence (M57-Jean) | `README.md` |
| `ex2-checklists/` | Ex2 small-step checklists | `00` to `05`, plus `EX2_START_HERE.md` at the top level |
| `ex3-monitor/` | Traffic monitoring | `gen_practice_pcap.py`, `pcap_to_sqlite.py`, `queries.sql`, `analysis.py`, `local.rules` |
| `ex4-defensive/` | Defensive code | `python/`, `c-debug/`, `mips/` |
| `templates/` | Write-up aids | justification, risk register, IR plan, key mgmt, ISMS, STRIDE, assurance, OSINT, UK law |

Writing the Ex1 justification? Start from `templates/ex1_justification_draft.md` (about 1,000 words, fill in the brackets).

## Quick start

```
pip install -r requirements.txt
python3 ex1-design/vlsm_calc.py 192.168.0.0/22 "Staff=120" "Guest=60" --growth 0.2
python3 ex2-malware/triage.py SAMPLE --yara ex2-malware/rules --md report.md
python3 ex3-monitor/pcap_to_sqlite.py capture.pcap && python3 ex3-monitor/analysis.py traffic.db
```

## Software needed

| Software | Used for | Link |
|---|---|---|
| Python 3 + pip | all scripts | https://www.python.org/downloads/ |
| Git | clone this repo | https://git-scm.com/downloads |
| Cisco Packet Tracer | Ex1 network design (needs a Cisco login) | https://www.netacad.com/cisco-packet-tracer |
| Wireshark | Ex3 capture and pcap review | https://www.wireshark.org/download.html |
| DB Browser for SQLite | Ex3 queries | https://sqlitebrowser.org/dl/ |
| Snort | Ex3 IDS rules | https://www.snort.org/downloads |
| Nessus Essentials | Ex1/Ex3 scanning (needs activation code) | https://www.tenable.com/products/nessus/nessus-essentials |
| Autopsy | Ex2 forensics | https://www.autopsy.com/download/ |
| YARA | Ex2 (also via `pip install yara-python`) | https://github.com/VirusTotal/yara/releases |
| VirusShare / Any.run | Ex2 samples and sandbox (logins) | https://virusshare.com , https://any.run |
| Kali / Metasploitable | Ex2/Ex3 attack and capture VMs | https://www.kali.org/get-kali/ , https://sourceforge.net/projects/metasploitable/ |
| MARS or SPIM | Ex4 MIPS assembler | https://courses.missouristate.edu/kenvollmar/mars/ , https://spimsimulator.sourceforge.net/ |
| GCC, GDB, Valgrind | Ex4 C debugging (Valgrind is Linux only; use WSL or a VM on Windows) | https://www.mingw-w64.org/ , https://www.sourceware.org/gdb/download/ , https://valgrind.org/downloads/ |
| PHP 8 | Ex1 upload app | https://www.php.net/downloads |

Python packages are listed in `requirements.txt`.

## Test status

Run `python3 -m pytest -q` in `ex2-malware`, `ex3-monitor`, `ex4-defensive/python`, `ex4-defensive/mips`; run `bash test_app.sh` in `ex1-design/php-upload`.

Not tested against the real tools: `ex3-monitor/local.rules` (Snort was unavailable) and the `.asm` files (checked with the included `mips_mini.py`, not MARS/SPIM). Re-check both once on the day.

## Safety

No malware is in this repo. `triage.py` only reads files and never runs them. Use samples in an isolated VM only.
