# Ex3 guide: Tuesday (Day 1) and Wednesday (Day 2)

One small step at a time. Do the step, tick it, move on. Do not read ahead.

**Tuesday (Day 1), hands-on:** A. Data and statistics, B. Recon, C. Monitoring and detection.
**Wednesday (Day 2), documents:** D. Risk model, E. External-standard risk assessment, F. ISMS plan, G. Incident response, H. Justification. Upload by 14:30 (deadline 16:00).

**Rules from the older v4 example pack. Check each against your live brief.**

- Open book: notes, books and the internet are allowed, **but "no personal communication and or on-line asynchronous interaction permitted"**. It is an individual test. Do not message anyone, and do not use an AI chat, during test hours. This guide is written to be used on its own.
- Tests run **09:30 to 16:00**. Active time is 6 hours. Take **one 30-minute break** and **email your supervisor when it starts and when it ends**.
- If screenshots are requested: **maximum 5 pages of A4**. Crop tightly.
- **Submission is final and cannot be reloaded or amended.**
- Merit and Distinction rows for Ex3 are in your printed v4 grade tables. I have not seen them, so none are invented here. Copy them into the blank table in `ex3_brief_checklist.md`.

**If you feel stuck:**

1. Stand up, drink water, look away from the screen.
2. Say aloud: "The next step is ____."
3. Write your assumption in one line, take a screenshot, move on. Come back at the end.

## 0. The data decision (read once, then follow it)

The brief says to consider Kaggle or Hugging Face for the large data set. The pipeline in this repo (`pcap_to_sqlite.py`) needs a **pcap**. Public sets are mostly **flow CSVs**, not pcaps. So use two sources:

| Need | Source | Used for |
| --- | --- | --- |
| Large data set, labelled attacks | **CIC-IDS2017, one day, as CSV flows** (Kaggle or Hugging Face copy) | Statistics, baseline, SQL, data quality (A5) |
| A real pcap you control | **Your own capture**, Kali to Metasploitable (A2) | Wireshark, `pcap_to_sqlite.py`, `queries.sql`, `analysis.py`, Snort (A3, A4, C) |
| Both blocked | `python3 gen_practice_pcap.py practice.pcap` | Last resort. Say in the write-up that it is **synthetic**. |

**What I checked** (official UNB page, https://www.unb.ca/cic/datasets/ids-2017.html):

- It offers `GeneratedLabelledFlows.zip` (flows, profiles and pcap) and `MachineLearningCSV.zip` (CICFlowMeter CSVs).
- Capture days and sizes: Mon 11.0 GB, Tue 11 GB, Wed 13 GB, Thu 7.8 GB, Fri 8.3 GB. **Do not download raw pcaps.**
- Attacks: Tue FTP-Patator and SSH-Patator. Wed DoS and Heartbleed. Thu web attacks and infiltration. Fri botnet, port scan, DDoS.
- If you use it, **cite** Sharafaldin, Habibi Lashkari and Ghorbani, "Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization", ICISSP, January 2018.

**What I have not checked:** the Kaggle and Hugging Face copies (file names, column names, size), and whether the QA machine can reach them. Test this first thing.

**Pick one day.** Tuesday has SSH brute force, which matches your own capture story. Friday has a port scan if you prefer.

## 1. Start of day (Tuesday)

**Folders and notes**

- ☐ Make a folder `Ex3_Day1`. Inside: `screenshots`, `outputs`, `notes`.
- ☐ Open `notes/evidence_log.txt`. After every step add one line: figure number, what it shows, file name.
- ☐ Name screenshots in order: `fig01_dataset_page.png`, `fig02_columns.png`.
- ☐ Open the Snipping Tool (`Win+Shift+S`).
- ☐ **Screenshot budget:** max 5 pages of A4 if screenshots are requested. Keep a running `evidence.docx` of cropped images with captions.

**Read the brief**

- ☐ Read the whole Ex3 brief once. Touch nothing.
- ☐ Highlight every verb (apply, identify, undertake, develop, manage).
- ☐ Note the yellow topics. Those are mandatory.

**Rules of engagement** (write on the first page of `notes/`)

- ☐ Authorised by: me, for my own lab, for my own coursework.
- ☐ In scope: my Kali and Metasploitable VMs, my own capture, the public CIC-IDS2017 data, a domain I own for passive recon.
- ☐ Out of scope: any employer or <company> system, any live site I do not own, anyone else's machine.
- ☐ Safety: VM snapshots before testing, revert after. No real personal data. Attacks only between my two VMs.
- ☐ Stop and escalate if anything touches something out of scope.

**Get things running in the background**

- ☐ Start Kali and Metasploitable. Snapshot both as `clean`.
- ☐ Put both VMs on the **same host-only or internal network**. Note both IPs: `<KALI>` and `<MSF>`.
- ☐ Check Python on Windows: `python -c "import scapy, pandas, sklearn, matplotlib, tabulate; print('ok')"`
  - If it fails: `pip install scapy pandas numpy scikit-learn matplotlib tabulate`
- ☐ Copy the `ex3-monitor` folder into `Ex3_Day1`.
- ☐ Open Wireshark and DB Browser for SQLite once, to check they start.
- ☐ **Test the download now:** open Kaggle and Hugging Face. Can you reach them? Do you need an account? If blocked, note it and use the fallback in section 0.

## 2. A. Data and statistics (brief topic 1)

**Done when:** you have a baseline, at least three anomalies with evidence, and a table of big-data weaknesses.

Time inside A: A1 20, A2 30, A3 40, A4 40, A5 25, A6 20.

### A1. Get the large data set

- ☐ Search "CIC-IDS2017" on Kaggle or Hugging Face. Pick a copy with CSV files.
- ☐ Download **one day's CSV only** (the Tuesday file is usually named like `Tuesday-WorkingHours.pcap_ISCX.csv`. Check yours).
- ☐ Write in your notes: data set name, URL, authors, date downloaded.
- ☐ Hash it: `Get-FileHash -Algorithm SHA256 <file>`. Log it. Screenshot the download page (`fig01`).

### A2. Make your own pcap

Do this in the lab only.

- ☐ Snapshot both VMs.
- ☐ In Wireshark on the Windows host, choose the VM network adapter. Or in Kali: `sudo tcpdump -i eth0 -w ex3_own.pcap`.
- ☐ Start the capture. **Write down the clock time.**
- ☐ **Normal window (about 5 minutes).** From Kali:
  - `ping -c 20 <MSF>`
  - Browse `http://<MSF>/` a few times.
  - `ssh msfadmin@<MSF>` once, log in correctly, then exit. (Metasploitable 2 may need legacy SSH options. If it refuses, use `telnet <MSF>` or FTP for a normal login.)
- ☐ Write down the time the normal window ended.
- ☐ **Attack window.** From Kali, against `<MSF>` only:
  - `nmap -sS -p- <MSF>` (port scan)
  - Make a short wordlist: `printf 'password\n123456\nadmin\nletmein\nqwerty\n%.0s' {1..10} > /tmp/words.txt`
  - `hydra -l msfadmin -P /tmp/words.txt -t 4 ssh://<MSF>` (SSH brute force)
  - `nikto -h http://<MSF>/` (web scan)
- ☐ Write down the time the attack window ended. Stop the capture.
- ☐ Save as `ex3_own.pcap`. Screenshot it open in Wireshark (`fig02`).
- ☐ Revert both VMs to `clean`.
- ☐ Hash the pcap. Log it.

*Hydra is on Kali but is not on the brief's software list. Say that in your notes.*

### A3. Load the pcap and run the SQL

- ☐ `python pcap_to_sqlite.py ex3_own.pcap --db traffic.db --csv packets.csv`
- ☐ Expect: `<N> packets -> packets.csv, traffic.db`. Write down N.
- ☐ Open `traffic.db` in DB Browser for SQLite. Tab **Execute SQL**.
- ☐ Run each query in `queries.sql` one at a time. Screenshot these:
  - ☐ Query 1, top talkers (`fig04`)
  - ☐ Query 3, port scan (`fig05`)
  - ☐ Query 5, brute force (`fig06`)
- ☐ For every query write one line: what it shows, what you would do next.
- ☐ **Expect empty results in places.** Your lab has only private IPs, so **query 6 (exfiltration) and most of 7 will show nothing external.** Write "none seen, because the lab has no external hosts". Do not invent a result.
- ☐ If a query returns 0 rows because the threshold is too high (for example "more than 50 ports"), lower it, rerun, and say you changed it and why.
- ☐ **Baseline vs attack:** use your noted times (convert with `date -d "<time>" +%s` in Kali). Then run:

```sql
SELECT src, COUNT(*) AS packets, COUNT(DISTINCT dport) AS ports
FROM packets WHERE ts BETWEEN <normal_start> AND <normal_end>
GROUP BY src ORDER BY packets DESC;
```

- ☐ Run the same query for the attack window. Compare the two. That is your baseline.

### A4. Statistics on your capture

- ☐ `python analysis.py traffic.db --out analysis_out`
- ☐ Open `analysis_out/summary.md`. It has: z-score outliers, an IQR fence, KMeans clusters.
- ☐ Screenshot `summary.md` (`fig07`), `clusters.png` (`fig08`), `timeline.png` (`fig09`). `top_talkers.png` is optional.
- ☐ Write what each method does in one line:
  - **Z-score:** how many standard deviations a source is from the mean.
  - **IQR fence:** Q3 plus 1.5 times the spread. Packets above it are unusual.
  - **KMeans (k=3):** groups sources by behaviour (normal, scanner, bulk).
- ☐ Note: **your own servers will show as heavy senders. That is normal. Explain it.** Say how a baseline separates "busy server" from "attacker".
- ☐ Say what the statistics **cannot** tell you (intent, a slow scan under the threshold).

### A5. Statistics on the large data set

- ☐ Save this as `ex3_flows.py`. Put your CSV file name in the first line.

```python
import sqlite3
import numpy as np
import pandas as pd

df = pd.read_csv("Tuesday-WorkingHours.pcap_ISCX.csv")
df.columns = df.columns.str.strip()            # some copies have leading spaces
df = df.replace([np.inf, -np.inf], np.nan)     # CIC copies contain Infinity in rate columns
print(df.shape, "rows,", int(df.isna().sum().sum()), "missing or infinite values")
print(df["Label"].value_counts())

con = sqlite3.connect("ids2017.db")
df.to_sql("flows_ids", con, if_exists="replace", index=False)

benign = df[df["Label"] == "BENIGN"]
for col in ["Flow Duration", "Total Fwd Packets", "Flow Bytes/s"]:
    s = benign[col].dropna()
    mu, sd = s.mean(), s.std()
    q1, q3 = s.quantile([.25, .75])
    lo, hi = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
    z = (df[col] - mu) / sd
    for name, mask in {"|z|>3": z.abs() > 3, "IQR fence": (df[col] < lo) | (df[col] > hi)}.items():
        f = df[mask.fillna(False)]
        caught = int((f["Label"] != "BENIGN").sum())
        fp = int((f["Label"] == "BENIGN").sum())
        total_attack = int((df["Label"] != "BENIGN").sum())
        print(f"{col:18} {name:10} flagged={len(f):6} attack_caught={caught}/{total_attack} benign_flagged={fp} ({100*fp/len(benign):.1f}% of benign)")
```

- ☐ Run: `python ex3_flows.py`. Screenshot the output (`fig10`).
- ☐ Column names differ between copies. If you get a `KeyError`, print `df.columns.tolist()` and edit the three names in the list.
- ☐ **Data quality (a named knowledge item).** Write: how many rows, how many missing or infinite values, and what you did about them (replaced `inf` with blank).
- ☐ **Baseline = BENIGN flows only.** Say so.
- ☐ Read the result honestly. A feature that catches many attacks with few false positives is useful. A feature that flags thousands of benign flows is not. **A single-feature threshold is weak. Say what you would add** (several features together, or a trained model).
- ☐ Also run one SQL query on `ids2017.db` in DB Browser, for example:

```sql
SELECT Label, COUNT(*) AS flows, ROUND(AVG("Flow Duration")) AS avg_duration
FROM flows_ids GROUP BY Label ORDER BY flows DESC;
```

*My test of this script used synthetic data shaped like the real file. Real results will differ. Report your real numbers only.*

### A6. Vulnerabilities in the big data architecture

- ☐ Draw one line of boxes: **sensor or capture, collector, storage, analytics, dashboard or report.** Mark the trust boundaries.
- ☐ Fill this table. Keep the rows that fit your setup. Write "not applicable" where something does not exist.

| Stage | Weakness to assess | Hits (C, I, A, reliability) | Control |
| --- | --- | --- | --- |
| Ingestion | Log or capture feed not authenticated or encrypted, so it can be spoofed or injected | I, reliability | Authenticated, encrypted forwarding; source allow-list |
| Ingestion | Malformed or huge pcap crashes the parser | A | Size limits, parse in a sandbox, unprivileged account |
| Interfaces and APIs | Query or export interface without login, or SQL built from strings | C, I | Authentication, prepared statements, least privilege |
| Access control | Shared account, or everyone can read raw packets | C | Role-based access, logging of who queried what |
| Storage | `traffic.db` and CSVs hold IPs and DNS names (personal data), unencrypted, editable | C, I | Disk encryption, file permissions, hashes of evidence files |
| Processing | Analytics run as admin on untrusted input | C, I, A | Run unprivileged, validate input |
| Deployment | Default credentials, exposed dashboard, unpatched components, no backups | C, I, A | Hardening baseline, patching, backups, network restriction |
| Monitoring itself | An attacker deletes or poisons logs, so you go blind | I, A | Write-once storage, off-box copy, alert on log gaps |

- ☐ Pick the two most serious. Say how each would affect your ability to detect an attack.
- ☐ Screenshot or photograph the diagram and table (`fig11`).

## Break

Stand up. Water. Eat something. Look away from the screen for a bit.

## 3. B. Ethical reconnaissance and intelligence analysis (brief topic 2)

**Done when:** you have a scoped target, a sources list, a confirmed / assumed / to-validate table, and attack paths.

Time: 45 minutes. **Passive and lawful only.**

- ☐ **Scope in two lines.** Target: a domain you own (the same one you listed in the rules of engagement). Objective: show what an attacker could learn without touching the target.
- ☐ <company> is fictional. Say: "I used my own domain as a stand-in for the method, and applied the same questions to <company>'s published details in the brief (technologies, cloud provider, suppliers, device types)."
- ☐ Collect, passive only. Log each command and screenshot a few (`fig12`, `fig13`):
  - ☐ `whois <domain>`
  - ☐ `dig <domain> ANY +noall +answer` and `dig <domain> MX +short`, `dig <domain> TXT +short` (mail setup, SPF, DMARC)
  - ☐ Certificate transparency: open `https://crt.sh/?q=<domain>` in the browser. It lists subdomains.
  - ☐ `curl -sI https://<domain>` (headers show server and technology)
  - ☐ Public documentation, job adverts and vendor pages for technologies named in the brief
- ☐ Do **not** run port scans against anything you do not own. nmap only against your lab VMs.
- ☐ Fill the **confirmed vs assumed** table:

| Finding | Source | Status |
| --- | --- | --- |
| Example: subdomain `vpn.<domain>` exists | crt.sh | Confirmed |
| Example: it probably uses product X | Header guess | Assumption |
| Example: staff reuse passwords | None | Needs validation |

- ☐ List technologies, services, dependencies and third parties (cloud, mobile device management, email provider, suppliers).
- ☐ Write **three attack paths** your findings suggest. For each: entry point, what the finding enables, what would need validating.
- ☐ Write one line: "Everything above was authorised, proportionate and from public sources."
- ☐ Method words: **plan, collect, check reliability, analyse, share.** Rate each source A, B or C.

## 4. C. Monitoring, analysis and intrusion detection (brief topic 6)

**Done when:** you have a data-source table, detection rules you ran, a correlation table, and an alert-handling process.

Time: 90 minutes.

### C1. What to monitor and what is normal

- ☐ Fill this table (use your own words and numbers from A):

| Event source | Why monitor it | What normal looks like | Suspicious sign |
| --- | --- | --- | --- |
| Authentication logs | Brute force, stolen credentials | A few failed logins per user per day | Dozens of failures from one source |
| Network traffic | Scans, exfiltration | Steady traffic to known hosts | One source touching hundreds of ports |
| Endpoint events | Malware, persistence | Known processes | New autorun entries |
| Application logs | Abuse of the sync API | Few 401 or 403 | Bursts of 401 |
| Security alerts (IDS) | Known attack patterns | Few, tuned | Same alert repeating |

### C2. Snort detections

Snort rules in `local.rules` are **untested**. Do these steps in Kali.

- ☐ Check the version: `snort -V`. Screenshot (`fig14`). Snort 2 and Snort 3 use different commands.
- ☐ Copy the rules: `cp local.rules /tmp/ex3.rules`
- ☐ **Replace the network variables.** Your attacker and target are on the same subnet, so `$EXTERNAL_NET` and `$HOME_NET` would not match as written:

```
sed -i 's/\$HOME_NET/<MSF>/g; s/\$EXTERNAL_NET/<KALI>/g' /tmp/ex3.rules
```

- ☐ Copy `ex3_own.pcap` into Kali.
- ☐ Test the rules:
  - Snort 3: `snort -c /etc/snort/snort.lua -R /tmp/ex3.rules -r ex3_own.pcap -A alert_fast -q`
  - Snort 2: add the rules to your `local.rules` and run `sudo snort -T -c /etc/snort/snort.conf` first, then `sudo snort -c /etc/snort/snort.conf -r ex3_own.pcap -A console -q`
- ☐ Expect alerts for: port scan (rule 1), SSH brute force (rule 2), maybe the ICMP sweep (rule 4) if you pinged fast. **Rule 3 (large outbound upload) will not fire in your lab**, because there is no external host. Say so.
- ☐ If a rule has a syntax error, fix it and say what you changed. Screenshot the alerts (`fig15`).
- ☐ **Tune one rule.** Change a threshold, rerun, say what changed and why.
- ☐ If Snort will not run at all: show the error, then use your SQL queries 3 and 5 as the detection logic, and say that plainly.

### C3. Wireshark evidence

- ☐ Filter `tcp.flags.syn==1 && tcp.flags.ack==0` : the scan. Screenshot (`fig16`).
- ☐ Filter `tcp.port==22` : the brute-force sessions.
- ☐ Filter `http` : the Nikto requests.

### C4. Correlate (what a SIEM does)

- ☐ Build a table that joins three sources by time. Use Snort alerts, your SQL results, and the target's login log (on Metasploitable: `/var/log/auth.log`).

| Time | Source | Event | What it means |
| --- | --- | --- | --- |
| hh:mm:ss | Packet data | One source sends SYNs to 1000 ports | Port scan |
| hh:mm:ss | Snort | Rule 1 alert | Same scan, detected |
| hh:mm:ss | Auth log | Many failed SSH logins from the same IP | Brute force after the scan |

- ☐ Write the **cause** from the observables: "recon, then credential attack". Say which evidence supports it and what would change your mind.
- ☐ Save as `fig17`.

### C5. Real incident or benign?

- ☐ Write two things that look bad but are normal: for example a backup server uploading a lot, or IT's authorised vulnerability scan.
- ☐ Say how you tell them apart: baseline, scheduled change records, known IPs.

### C6. Alert handling

- ☐ Priority table:

| Priority | Example | Response time | Who |
| --- | --- | --- | --- |
| P1 | Confirmed data leaving, or compromised admin | Immediately | Incident lead |
| P2 | Brute force on an internet-facing service | Within 1 hour | Security analyst |
| P3 | Port scan from outside | Same day | Analyst |
| P4 | Informational | Weekly review | IT |

*These times are my proposals. Replace them with what suits <company>.*

- ☐ Say how alerts are **recorded** (ticket), **escalated** (P1 to the incident lead), and used to **tune** rules (review false positives monthly).

## 5. End of Tuesday

- ☐ Evidence log: every figure has a number, a file name, what it shows and where you will use it.
- ☐ Hashes recorded: CIC-IDS2017 file, `ex3_own.pcap`.
- ☐ Copy outputs: `traffic.db`, `packets.csv`, `analysis_out/`, `ids2017.db`, Snort output, notes.
- ☐ Remove anything that must not be uploaded. Revert VMs to `clean`.
- ☐ Check the brief for what must be uploaded each day. **Submission is final.**
- ☐ Save work in two places.
- ☐ Sticky note for tomorrow: "Wed: D risk, E standard, F ISMS, G incident response, H justification, upload by 14:30."

---

# Wednesday (Day 2)

Make `Ex3_Day2` with `notes` and `outputs`. Keep the evidence log going (`fig18` onwards).

Open these templates in `templates/`: `risk_register.md`, `security_policy_and_isms.md`, `incident_response_plan.md`, `assurance_strategy.md`.

## 6. D. Risk modelling, analysis and trade-offs (brief topic 3)

**Done when:** every Day 1 finding is a row in a risk register, with a treatment and a residual risk.

Time: 45 minutes.

- ☐ List **assets**: patient notes database, API tokens, staff devices, monitoring data (`traffic.db`), the sync service.
- ☐ Turn each Day 1 finding into a row:

| ID | Threat | Vulnerability (your evidence) | Asset | L (1-5) | I (1-5) | Score | Treatment | Residual |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | Port scan then SSH brute force | No rate limit; 61 SSH attempts in query 5 *(use your number)* | Sync server | 4 | 4 | 16 | Rate limit, key-only SSH, alert | 6 |

- ☐ **One scale for everything.** Write the scale (1 = rare / minor, 5 = almost certain / severe). Score = L x I. Say what counts as High (for example 15 or more).
- ☐ **Relationships.** Draw or write: Threat exploits Vulnerability, which exposes Asset, which causes Impact.
- ☐ **Qualitative and quantitative.** Add one quantitative row with the formula: SLE = asset value x exposure factor, ALE = SLE x ARO (annual rate of occurrence). Use clearly marked **assumed** values.
- ☐ **Assumptions and limitations** (3 lines): scores are judgement, lab data is small, impact values are assumed.
- ☐ **Trade-offs.** For your top two risks, compare 2 or 3 treatments:

| Option | Security gain | Cost | Usability | Performance | Availability | Choice |
| --- | --- | --- | --- | --- | --- | --- |
| Rate limiting | Medium | Low | Low impact | Low | Low risk of lockout | Chosen |
| MFA on admin access | High | Medium | Some friction | None | None | Chosen |
| Network IPS inline | High | High | None | Adds latency | Risk of false blocks | Rejected for now |

- ☐ Justify each choice with evidence (figure number).
- ☐ **Residual risk:** list the risks still above your acceptable level, and what extra monitoring or management action covers them.
- ☐ Save as `fig18` (register) and `fig19` (matrix).

## 7. E. Risk assessment to an external standard (brief topic 4)

**Done when:** another person could repeat your assessment from your records.

Time: 60 minutes.

- ☐ **Choose the standard.** I suggest **ISO/IEC 27005:2022** (information security risk management). It pairs with ISO/IEC 27001, which you use in F. **Alternative:** NIST SP 800-30 Rev. 1. Say why you chose yours and what you rejected.
- ☐ **I cannot access the paid standard text.** Use the stage names from your own notes or course material. Do not quote clauses from memory. Check that your headings match your copy.
- ☐ Work through these stages in order, one short section each:

| Stage | What you write |
| --- | --- |
| Scope and context | Systems in scope, assets, dependencies, assumptions |
| Criteria | Impact scale, likelihood scale, risk acceptance level |
| Identification | Threats, vulnerabilities, existing controls (from A, B, C) |
| Analysis | Likelihood and impact for each risk |
| Evaluation | Compare to the acceptance level, rank |
| Treatment | Modify, retain, avoid or share, with a plan and owner |
| Residual risk | What remains, who accepts it |
| Monitoring and review | When it is reassessed, what triggers a reassessment |

- ☐ **Map risks to controls.** Use ISO/IEC 27001:2022 Annex A control themes (organisational, people, physical, technological). Mark any risk with **no control** as a gap.
- ☐ **Record it systematically:** one table, one row per risk, with source figure. This is your evidence that you followed the standard.
- ☐ Document **limitations and areas needing more work** (3 lines).
- ☐ Check the brief for regulators relevant to the case (health and social care data, UK GDPR). Link risks to them in one line.
- ☐ Save as `fig20`.

## 8. F. Management system and ISMS plan (brief topic 5)

**Done when:** you have a one-page plan with measurable objectives and a review cycle.

Time: 45 minutes.

- ☐ **Context:** <company>, 420 staff on laptops and mobiles (check the brief for the real numbers), patient notes, cloud services, suppliers.
- ☐ **Stakeholders and roles:** board or senior owner, IT lead, data protection lead, staff, suppliers. One line each on responsibility.
- ☐ **Approach:** based on **ISO/IEC 27001** plan, do, check, act. Policies you will have: access control, acceptable use, data protection, password and credential management, incident management, third-party access (see your Ex1 `policy.md` and `templates/security_policy_and_isms.md`).
- ☐ **Measurable objectives** (these values are proposals, adjust them):

| Objective | Measure | Target | Owner |
| --- | --- | --- | --- |
| Detect scans quickly | Time from first scan packet to alert | Under 5 minutes | Security analyst |
| Fix serious weaknesses | Days to patch critical findings | 14 days | IT lead |
| Staff awareness | Staff who completed phishing training | 95 percent | HR |
| Incidents handled | P1 incidents with a review in 10 days | 100 percent | Incident lead |

- ☐ **Plan sections:** risk treatment, access management, monitoring, incident management, training, continual improvement. One short paragraph each.
- ☐ **How it is measured and reviewed:** monthly metrics, quarterly management review, annual internal audit.
- ☐ **Change feedback:** new threats, new technology, new regulation, or an incident triggers a reassessment of the risk register and the plan.
- ☐ Save as `fig21`.

## Break

Stand up. Water. Eat something. Look away from the screen for a bit.

## 9. G. Intrusion response, including third parties (brief topic 7)

**Done when:** you have a response plan, a third-party table, a notification note, and a worked exercise.

Time: 60 minutes.

- ☐ **Phases.** One line each for: identification, triage, containment, eradication, recovery, post-incident review. Use the example from Day 1: scan, then SSH brute force, then a possible successful login.
- ☐ **Roles and escalation:**

| Role | Authority | Escalate to |
| --- | --- | --- |
| Analyst | Triage, record, contain minor events | Incident lead |
| Incident lead | Declare an incident, isolate systems | Senior owner |
| Senior owner | Approve notifications, external help | Board if needed |

- ☐ **Severity and when to call for help.** Re-use P1 to P4 from C6. Say what makes you call outside help: confirmed compromise of patient data, ransomware, or no ability to contain it in-house.
- ☐ **Third parties:**

| Party | Role in an incident | What you share | Controls |
| --- | --- | --- | --- |
| Cloud provider | Logs, isolation, restore | Account and time details | Contract support route |
| Managed security service | Monitoring, triage | Logs and alerts | Data processing agreement |
| Software supplier | Patch or workaround | Version and error details | Named contact |
| External incident response team | Forensics and containment | Evidence copies | NDA, chain of custody |
| NCSC and police | Advice, reporting | Summary | Via the incident lead |

- ☐ **Sharing evidence securely:** copy not original, record hashes, send over an encrypted channel, share the minimum, log who received what, no real patient data unless necessary.
- ☐ **Notification:** a personal data breach likely to risk people's rights must be reported to the regulator **within 72 hours** of becoming aware (UK GDPR). Affected people must be told if the risk is high. Also check contracts, health sector reporting routes and your insurer. **Check the current reporting route for the regulator and for fraud reporting before you write names.**
- ☐ **Run an exercise (tabletop).** Use this scenario from your own findings and fill the table:

| Time | Inject | Expected action | Who | Gap found |
| --- | --- | --- | --- | --- |
| T+0 | Snort alert: port scan from one source | Analyst triages, checks baseline | Analyst | |
| T+15 | Auth log: 60 failed SSH logins, then one success | Escalate to incident lead, isolate host | Incident lead | |
| T+30 | Large upload to an external IP | Declare incident, call cloud provider, preserve evidence | Incident lead | |
| T+60 | Regulator clock started | Decide on notification | Senior owner | |

- ☐ **Improvements** from the "Gap found" column. Write at least three, one about third parties.
- ☐ Save as `fig22` (plan) and `fig23` (exercise).

## 10. H. Justification (brief final topic)

**Time: 45 minutes. Target 1,000 words (900 to 1,100).**

- ☐ Open `ex3_justification.md`. Write it last, from your evidence log.
- ☐ Fill each part in 3 to 5 short sentences.
- ☐ Use the 5-part pattern for each decision: what you chose, which risk or requirement, evidence (figure number), one alternative rejected, remaining risk.
- ☐ Be honest about what is pre-written (`pcap_to_sqlite.py`, `analysis.py`, `local.rules`, templates) and what you changed. Say what you could not run.
- ☐ Count words and check every figure number appears in the text.

## 11. Upload

- ☐ Evidence log complete. Figures renamed to match.
- ☐ Remove anything that must not go in: real credentials, tokens, real personal data.
- ☐ Count screenshot pages: **5 pages of A4 maximum** if screenshots are requested.
- ☐ Upload what the brief asks for. **Submission is final.**
- ☐ Confirm the upload shows as submitted.
- ☐ Aim to finish by **14:30**.

## If something breaks

- **Cannot download CIC-IDS2017:** use `gen_practice_pcap.py`, say the data is synthetic, and say what real data you would use.
- **Hydra or nmap will not run:** use your Kali tools list from the brief. Say what you ran and what you did not.
- **Snort will not run:** show the error, use SQL queries 3 and 5 as the detection logic, say so plainly.
- **Query returns nothing:** lower the threshold or say "none seen". Do not invent results.
- **Metasploitable will not accept SSH:** use FTP or telnet for the normal and brute-force traffic. Say why.
