# Ex3 detailed steps: Tuesday (A4 to C7)

This adds detail to `ex3_guide.md`. Same section letters. For each step:

- **Do** = exactly what to click or type
- **You should see** = what a correct result looks like
- **Write** = example wording for your notes. Replace anything in [square brackets] with your own result.

**Every number marked EXAMPLE comes from the synthetic practice file, not from you.** Never copy an example number into your work. Use your own.

**How much to write per step:** 2 to 4 sentences. One screenshot. One line in the evidence log.

---

## A4. Statistics on your own capture

### A4.1 Run it

**Do**

1. Open a terminal in the folder with your database.
2. Type (use your own file name, here `own_traffic.db`):

```
python analysis.py own_traffic.db --out analysis_out
```

**You should see:** text ending with `Charts and summary.md saved in analysis_out/`.

**If you get an error:** copy the last line into your notes, then read A4.2 before doing anything else. A small lab can cause expected "none" results.

### A4.2 What a small lab does to the results

Your lab has few hosts (Kali, Metasploitable, maybe the Windows host). That changes what you will see.

- **A z-score needs a crowd.** With only a few sources, no host can be more than 2 standard deviations from the mean. With fewer than about 6 sources you will usually see `none` under both "Outlier" headings. **This is correct, not a bug.**
- **KMeans needs at least 3 sources.** With 2 hosts, `clusters.png` is not created. Also expected.
- **The IQR fence still works** with any number of hosts.

**Write (use this if your result says none):**
"With only [N] hosts the z-score tests report no outliers, because a sample this small cannot produce a z-score above 2. I therefore used the IQR fence on packet length and a time-window comparison between normal and attack traffic, and I used the CIC-IDS2017 data (A5) for a statistically meaningful sample."

### A4.3 Read `summary.md` section by section

**Do:** open `analysis_out/summary.md` in Notepad or VS Code. Read top to bottom.

| Section | What it means | What to look for |
| --- | --- | --- |
| `Packets: N | Sources: M` | How much data you have | Write N and M down |
| Outlier senders (z > 2 on bytes) | Sources sending far more bytes than the others | A server or a bulk uploader |
| Outlier port-diversity | Sources contacting many different ports | A **scanner**. This is your nmap source |
| IQR fence on packet length | Packets larger than Q3 + 1.5 x (Q3 minus Q1) | The top sources are usually servers sending pages or files |
| KMeans clusters | Hosts grouped by behaviour | See A4.4 |

**EXAMPLE of a good result (synthetic file):** one source had 400 distinct destination ports and a z of 3.43. That is the scanner.

### A4.4 Read the KMeans table (only if you got one)

Look at the last three columns for each cluster:

| Pattern | Likely meaning |
| --- | --- |
| Many `dst_ports` AND high `syn_ratio` (above about 0.5) AND small `mean_len` | Port scanner |
| Very high `bytes` and large `mean_len` | Server or bulk transfer |
| Few packets, few ports, low `syn_ratio` | Ordinary client |

**EXAMPLE (synthetic):** cluster 2 had 400 ports, syn_ratio 0.71 and mean_len 63. That fits a scanner.

### A4.5 Baseline comparison (use this even if z-scores say none)

**Do:** in DB Browser for SQLite, tab **Execute SQL**, paste, press **Ctrl+Return**.

1. Find your window times. Convert from clock time to epoch seconds in Kali: `date -d "2026-11-17 11:00:00" +%s` (change to your date and time). Do it for: normal start, normal end, attack start, attack end.
2. Normal window:

```sql
SELECT src, COUNT(*) AS packets, COUNT(DISTINCT dport) AS ports, SUM(length) AS bytes
FROM packets WHERE ts BETWEEN [normal_start] AND [normal_end]
GROUP BY src ORDER BY packets DESC;
```

3. Attack window: same query with the attack times.
4. Screenshot both result grids side by side (one image is fine).

**You should see:** in the attack window, one source (Kali) has far more packets and far more distinct ports than in the normal window.

**Write:** "Between [start] and [end] (normal) [src] sent [x] packets to [y] ports. Between [start] and [end] (attack) the same source sent [x] packets to [y] ports, a [z]-fold increase in port diversity. The baseline is therefore [y] ports and attacks exceed it by a large margin."

### A4.6 Charts

**Do:** open `analysis_out/timeline.png`. Screenshot it. If `top_talkers.png` exists, screenshot that too.

**Write:** "The timeline shows [a flat period then a burst starting at hh:mm], matching my attack window."

### A4.7 Explain the methods (needed for the knowledge criteria)

Copy these three lines into your notes in your own words:

- **Z-score:** how many standard deviations a value is from the mean. Above 2 or 3 is unusual.
- **IQR fence:** the spread of the middle half of the data (Q3 minus Q1). A value more than 1.5 times that spread above Q3 is an outlier.
- **KMeans:** groups hosts into k clusters with similar behaviour. It needs a few hosts to be meaningful.

**Then write one limit:** "Statistics show that something is unusual, not why. A busy server and an attacker both look large, and a slow scan under the threshold would not appear."

---

## A5. Statistics on the CIC-IDS2017 slice

### A5.1 Run it

**Do**

1. Save the script from `ex3_guide.md` section A5 as `ex3_flows.py`, in the same folder as your CSV.
2. Change the first file name inside the script to match your CSV exactly.
3. Run `python ex3_flows.py`.

**You should see** (in this order):

1. A line like `(N, 79) rows, [M] missing or infinite values`. First number is rows, second is columns.
2. A list of labels and counts, for example `BENIGN` and `SSH-Patator`.
3. Up to six lines starting with a column name, for example `Flow Duration |z|>3 flagged=... attack_caught=x/y benign_flagged=...`.

**If you get `KeyError`:** run `python -c "import pandas as pd; print(pd.read_csv('YOURFILE.csv', nrows=1).columns.tolist())"`. Edit the three names in the list in the script to match exactly (watch for leading spaces).

**If it is slow or runs out of memory:** add `nrows=300000` inside `pd.read_csv(...)`, and say in your notes you used the first 300,000 rows.

### A5.2 Read each output line

Take one line:

`Flow Duration  |z|>3  flagged=1200  attack_caught=300/5000  benign_flagged=900 (0.9% of benign)`

| Part | Meaning |
| --- | --- |
| `flagged=1200` | The test marked 1,200 flows as unusual |
| `attack_caught=300/5000` | 300 of the 5,000 real attack flows were flagged (a **detection rate** of 6 percent) |
| `benign_flagged=900 (0.9%)` | 900 normal flows were wrongly flagged (a **false alarm rate** of 0.9 percent) |

**EXAMPLE numbers above are made up to explain the layout.**

**Judge each line:**

- High detection rate, low false alarm rate = **good** feature.
- Low detection rate = **misses** most attacks.
- High false alarm rate = **noisy**, would swamp an analyst.

### A5.3 What to write

1. **Data quality (3 sentences):** "The file has [N] rows and [C] columns. [M] values were missing or infinite, mainly in [Flow Bytes/s]. I replaced infinite values with blanks and excluded them from the calculations, so the totals are slightly understated."
2. **Baseline:** "The baseline is the BENIGN flows only: [mean], [spread] for [column]."
3. **Result:** "Using [column] with [test], I caught [x] of [y] attack flows ([x/y as %]) with a false alarm rate of [z]% of benign flows."
4. **Honest conclusion:** "A single feature [did / did not] separate the attack well. A real detector would combine several features, or use a trained model, and would be tested on a separate day of data."

### A5.4 One SQL query on the large data

**Do:** open `ids2017.db` in DB Browser for SQLite. **Execute SQL**:

```sql
SELECT Label, COUNT(*) AS flows, ROUND(AVG("Flow Duration")) AS avg_duration
FROM flows_ids GROUP BY Label ORDER BY flows DESC;
```

**You should see:** one row per label. **Screenshot** it. Write one sentence: "Attack flows have a [shorter / longer] average duration than benign flows ([x] vs [y])."

---

## A6. Big-data weaknesses: worked example

### A6.1 Draw the architecture

**Do:** on paper or in Draw.io or PowerPoint, draw five boxes in a row and label them:

```
[Capture: Wireshark/tcpdump] -> [Collector: pcap_to_sqlite.py] -> [Storage: SQLite + CSV] -> [Analytics: analysis.py, SQL] -> [Report: charts, summary]
```

Draw a dashed line around the whole thing and write "my laptop: trust boundary". Draw a second dashed line between Kali/Metasploitable and the capture: "lab network: trust boundary".

### A6.2 Fill the table: worked rows

**Do:** make a table with four columns: Stage, Weakness, Which of C/I/A/reliability it hits, Control. Use these worked rows as a guide and adapt to your set-up:

| Stage | Weakness | Hits | Control |
| --- | --- | --- | --- |
| Capture | A host on the lab network could spoof or flood traffic and distort the baseline | Reliability, I | Capture on a dedicated interface; record the capture times |
| Collector | A malformed or very large pcap could crash the parser | A | Check file size first; run as a normal user, not admin |
| Storage | `own_traffic.db` and CSVs contain IPs (personal data) and can be edited | C, I | Encrypted disk; read-only copy; record SHA-256 hashes |
| Analytics | SQL built from strings could be injected; scripts run as the logged-in user | C, I | Use fixed queries; least privilege |
| Report | Charts and notes copied to shared drives expose internal addresses | C | Restrict sharing; remove addresses if not needed |
| Monitoring itself | An attacker with access can delete logs and blind the analyst | I, A | Keep an off-box copy; alert on gaps in the data |

### A6.3 Two serious ones

**Write (2 sentences each):** "[Weakness] is most serious because [effect on detection]. For example, if [attacker action], my analysis would [wrongly show nothing / wrongly show an attack]. I would reduce it with [control]."

### A6.4 Benefits and limits

**Write:** "Big-data approaches let a monitoring team analyse millions of flows quickly, but they cost more to store and run, depend on data quality, and bring privacy duties because the data holds personal information."

**Name an architecture:** "In a larger deployment a Hadoop-style cluster would ingest logs, store them across several machines, and process them in batches. The same weaknesses apply, with more interfaces to secure."

---

## B. Recon: worked example

### B.1 Scope (2 lines)

**Write:** "Target: [your domain]. It stands in for <company>, which is fictional. I only use public sources and make no connection to the target other than DNS and standard web requests."

### B.2 Run and read each command

| Command | You should see | What it tells you |
| --- | --- | --- |
| `whois [domain]` | Registrar, creation date, name servers (some fields hidden by privacy) | Who runs the domain, how old it is |
| `dig [domain] A +short` | One or more IP addresses | Where the site is hosted |
| `dig [domain] NS +short` | Name server host names | Who runs DNS |
| `dig [domain] MX +short` | Mail server host names | Which email provider is used |
| `dig [domain] TXT +short` | Text records. One starts `v=spf1`, which lists who may send mail | Email set-up and some third-party services |
| `dig _dmarc.[domain] TXT +short` | A record starting `v=DMARC1` (or nothing) | Whether spoofing protection is set |
| `curl -sI https://[domain]` | Header lines such as `HTTP/2 200` and `server:` | Web server and technology |
| Browser: `https://crt.sh/?q=[domain]` | A table of certificates with names | Sub-domains that have had certificates |

**If a command returns nothing:** write "[command]: no result" in your log and carry on. **That is a finding too.**

### B.3 The confirmed, assumed and to-validate table: worked rows

| Finding | Source | Status | Reliability (A/B/C) |
| --- | --- | --- | --- |
| [domain] resolves to [IP] | `dig A` | Confirmed | A (direct DNS) |
| Mail handled by [provider] | `dig MX` | Confirmed | A |
| SPF record lists [service] | `dig TXT` | Confirmed | A |
| Site likely runs [software] | `server:` header | **Assumption**, headers can be changed | B |
| Sub-domain `[x].[domain]` exists | crt.sh | Confirmed it had a certificate; **needs validation** that it is live | B |
| Staff reuse passwords | None | **Needs validation**, no evidence | C |

**Reliability scale:** A = direct from the system, B = public record that could be out of date, C = guess or hearsay.

### B.4 Two sources that disagree

**Do:** look for any mismatch. Examples:

- The `server:` header names one product but the page itself names another.
- A certificate lists a sub-domain that does not resolve in DNS.
- WHOIS says a domain was created on one date but the first certificate is older.

**Write:** "[Source A] says [x] but [source B] says [y]. I trust [A/B] more because [direct vs indirect, more recent, harder to fake]. This affects my conclusion by [how]."

**If you find none:** write "I checked for contradictions between [sources] and found none."

### B.5 Attack paths (write three)

Use this pattern:

1. **Entry point:** [what is exposed].
2. **What the finding enables:** [for example phishing, because the SPF or DMARC record is weak or missing].
3. **What I would validate next:** [how, using authorised methods only].

**EXAMPLE shape (not a finding):** "Entry: staff email. The domain has no DMARC record, so an attacker could send spoofed mail. Validate by checking a test message in an authorised test."

### B.6 Behaviours (one line each)

- **Port scanning in your sources:** "An external scan would show in my logs as [one source touching many ports], as in my own capture (fig [x])."
- **Open-source intelligence:** "This section is OSINT: all information came from public records."
- **Insider:** "An insider would not appear in DNS at all; they would appear in authentication and access logs, which is why C4 correlates the login log."

### B.7 Last line

**Write:** "All collection was passive, from public sources, against a domain I own. Nothing was scanned or tested."

---

## C. Monitoring and detection

### C1. Table: worked rows

| Event source | Why monitor | Normal looks like | Suspicious sign |
| --- | --- | --- | --- |
| Authentication logs (`auth.log`, `vsftpd.log`) | Spot password guessing | A user mistypes once or twice | One IP with dozens of failures in a minute |
| Network traffic (pcap, flows) | Spot scans and bulk transfers | Steady flows to known servers | One host touching hundreds of ports |
| Endpoint events | Spot malware and persistence | Known processes | New auto-start entries |
| Application logs | Spot abuse of the sync service | Few failed API calls | Bursts of 401 or 403 |
| IDS alerts (Snort) | Known attack patterns | Few, reviewed | The same alert repeating |

**Use your own baseline numbers from A4.5 in the "Normal" column.**

### C2. Snort: step by step

**Do** (in Kali):

1. `snort -V`. Read the version line. Screenshot (fig14). Note **2.9.x or 3.x**.
2. `cp local.rules /tmp/ex3.rules`
3. Replace the variables (use your real IPs):

```
sed -i 's/\$HOME_NET/[MSF-IP]/g; s/\$EXTERNAL_NET/[KALI-IP]/g' /tmp/ex3.rules
```

4. Check the replacement worked: `grep -c HOME_NET /tmp/ex3.rules`. **Expect `0`.**
5. Copy `ex3_own.pcap` (or your pcap name) into Kali if it is on Windows.
6. Run the command for your version (full commands in the guide, C2).
7. Look at the output.

**You should see lines like (this format is typical, yours will differ):**

```
11/17-11:20:03.123456 [**] [1:1000006:1] EPA possible FTP brute force [**] [Classification: ...] [Priority: 1] {TCP} 192.168.56.101:40022 -> 192.168.56.102:21
```

Read it left to right: **time**, **rule number (sid)**, **rule message**, **source IP:port**, arrow, **destination IP:port**.

**Which rule fires when:**

| Rule (sid) | Fires on | Expected in your lab? |
| --- | --- | --- |
| 1000001 | Many SYNs from one source in 10 seconds (port scan) | Yes, from nmap |
| 1000002 | Many connections to port 22 (SSH brute force) | Only if you brute-forced SSH |
| 1000006 | Many connections to port 21 (FTP brute force) | Yes if you used FTP |
| 1000004 | ICMP echo sweep | Maybe, if you pinged quickly |
| 1000005 | Cleartext `PASS` to ports 21, 23, 110 | Yes with FTP (often once per attempt) |
| 1000003 | Large upload to an external host on 443 | **No**, the lab has no external host |

**Write:** "Snort [version] raised [N] alerts: [n1] for port scan, [n2] for [FTP/SSH] brute force. [Rule] did not fire because [reason]."

**Count alerts per rule:** `snort ... | grep -o 'sid:[0-9]*\|\[1:[0-9]*' | sort | uniq -c` (the exact text depends on your version; if it prints nothing, count by eye and say so).

**Tune one rule (example):** change `count 30, seconds 10` to `count 100, seconds 10`. Rerun. Write: "I raised the threshold from 30 to 100, so [rule] [no longer fired / fired fewer times], showing the trade-off between catching slow scans and false alarms."

**If a syntax error appears:** copy the error line into your notes. Open `/tmp/ex3.rules`, go to the line number shown, fix the typo, rerun.

### C3. Wireshark: click by click

1. Open `ex3_own.pcap` (File, Open).
2. Click the green bar (display filter). Type `tcp.flags.syn==1 && tcp.flags.ack==0`. Press Enter. The status bar (bottom) shows **Displayed: N**. Write N. Screenshot (fig16).
3. Clear the filter. Type `tcp.port==21` (or 22). Press Enter. Screenshot.
4. Clear. Type `ftp.response.code==530`. Press Enter. Each row is a failed login. Write the count.
5. Clear. Type `http`. Press Enter. Click one request. Look in the bottom pane for `User-Agent`.
6. **Inspect packet structure.** Click one SYN packet. In the middle pane, click the arrow next to **Transmission Control Protocol**. Find **Flags**. Write: "Flags: SYN only (no ACK). Window size [x]."
7. **Statistics menu:** try **Protocol Hierarchy**, **Conversations** (TCP tab, sort by Packets), **I/O Graph**. Take one screenshot.

**Write (one line each):** "A SYN with no ACK means a connection attempt that was never completed; many of these to many ports is a port scan." "The FTP 530 responses show the server rejected [N] logins."

### C4. Correlation table: worked example (shape only)

| Time | Source | Event | Meaning |
| --- | --- | --- | --- |
| [11:15:02] | Packet data | [Kali] sends SYNs to [1000] ports on [MSF] | Port scan |
| [11:15:03] | Snort | Rule 1000001 alert | Same scan, detected |
| [11:20:03] | Packet data | [N] connections to port [21] | Credential attack |
| [11:20:04] | `vsftpd.log` | [N] FAIL LOGIN from [Kali IP] | Failed guesses |
| [11:20:05] | Snort | Rule 1000006 alert | Brute force, detected |

**To fill the times:** convert epoch times with `date -d @[epoch]` in Kali, or compare with your noted window times. Use the earliest time in each group.

**Write the cause (4 sentences):** "The evidence supports reconnaissance followed by a credential attack. The scan [time] preceded [N] failed logins from the same address at [time]. Three independent sources (packets, Snort and the service log) agree. This conclusion would be weakened if [the source were an authorised scanner, or the logins were from a known admin]."

**ATT&CK mapping (copy):**
- Scan = Network Service Discovery (T1046)
- Brute force = Brute Force (T1110)

**Breach decision:** "Did the attacker get in? [Yes / No / Unsure]. Evidence: [any OK LOGIN line after the failures, or no successful login]."

**Impact (3 sentences):** "If this were a <company> server, the data at risk is [patient notes / credentials]. The people affected would be [patients, staff]. The impact is [high / medium] because [reason]."

### C5. Things that look bad but are normal

**Write two:**
- "A backup server uploading a lot of data at night looks like exfiltration. I would tell them apart by checking the change calendar and that the destination is a known backup address."
- "An authorised vulnerability scan from IT looks like an attack. I would tell it apart by checking the scan schedule and the scanner's known address."

### C6. Alert priority table (proposals)

| Priority | Example | Response time | Who |
| --- | --- | --- | --- |
| P1 | Confirmed data leaving or compromised admin account | Immediately | Incident lead |
| P2 | Brute force on an exposed service | Within 1 hour | Security analyst |
| P3 | External port scan | Same day | Analyst |
| P4 | Information only | Weekly review | IT |

**Write:** "Every alert is recorded in a ticket with time, source and decision. P1 and P2 go to the incident lead. Each month I review false positives and adjust thresholds, as I did when I changed [rule]."

### C7. Trade-offs

Copy the four-row table from the guide, then write: "My Snort rules detect known patterns well and have few false alarms, but they would miss a slow scan under the threshold. My z-score and IQR tests can flag behaviour I did not write a rule for, but they need a good baseline."

**SIEM line:** "In production I would feed these logs into [Wazuh / Splunk / Microsoft Sentinel] so the correlation in C4 happens automatically. I did not run a SIEM in this exercise."
