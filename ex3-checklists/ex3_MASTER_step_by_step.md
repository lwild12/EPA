# Ex3 MASTER step-by-step (start here)

One file, in order, from opening your laptop to uploading on Blackboard.
Follow it top to bottom. Do not skip. Do not read ahead.

**If you get lost:** find the last figure number in your `evidence_log.txt`, then search this file for the next one.

## Order of work

| When | Part | Steps | Time |
| --- | --- | --- | --- |
| Tue am | Set up | 0 to 0d | 45 min |
| Tue am | Data and database | A1, A2, A3, A3b | 2 h |
| Tue midday | Statistics | A4 to A6 | 1 h 30 |
| Tue pm | Recon | B | 45 min |
| Tue pm | Monitoring | C1 to C7 | 1 h 45 |
| Wed am | Risk model | D1 to D7 | 2 h |
| Wed am | Standard, plan | E, F | 2 h |
| Wed pm | Incident response | G | 1 h 15 |
| Wed pm | Justification and upload | H | 45 min, upload by 14:30 |

**Reminders**

- Test hours 09:30 to 16:00. One 30-minute break. Email your supervisor at the start and end of the break (check your live brief).
- Screenshots (if requested): maximum 5 pages of A4.
- Submission is final. Open the uploaded file to check it.
- Use `<company>` for the case study name in anything public.
- Every number marked EXAMPLE is a demonstration. Replace it with your own.

**Anything that fails twice:** log it as FAILED, screenshot the error, and move on.

---


Same layout as the other detail files: **Do**, **You should see**, **If not**, **Log**.

**Log** = the one line you add to `notes/evidence_log.txt`. Format: `fig## | what it shows | file name`.

**Golden rules (read once):**

1. One step at a time. Tick it. Move on.
2. If a step fails twice, write "FAILED: [what], [error text]" in the log, take a screenshot of the error, and go to the next step. Errors are evidence too.
3. Never run a command against anything except your own two VMs.
4. Screenshots: press `Win+Shift+S`, drag around ONLY the useful part, save with the figure name.
5. Never delete a file. Make a new one with a new name.

---

## 0. Set up the folders (10 min)

**Do**

1. Open File Explorer. Make a folder called `Ex3_Day1`.
2. Inside it make three folders: `screenshots`, `outputs`, `notes`.
3. Copy the whole `ex3-monitor` folder from the repo into `Ex3_Day1`.
4. In `notes`, make a text file called `evidence_log.txt`.
5. In `notes`, make a text file called `rules_of_engagement.txt`. Paste in:

```
Authorised by: me, for my own lab and coursework.
In scope: my Kali VM, my Metasploitable VM, my own captures, public CIC-IDS2017 data, a domain I own (passive recon only).
Out of scope: any employer or <company> system, any live site I do not own, anyone else's machine.
Safety: VM snapshots before testing and revert after. No real personal data. Attacks only between my two VMs.
Stop and escalate if anything touches something out of scope.
```

**You should see:** the folder tree `Ex3_Day1 / ex3-monitor, screenshots, outputs, notes`.

**Log:** `00 | folders and rules of engagement created | notes/rules_of_engagement.txt`

## 0b. Read the brief (10 min)

1. Read the whole Ex3 brief once. Do not start work.
2. Highlight the yellow topics. There are 8 (see `ex3_brief_checklist.md`).
3. Open `ex3_brief_checklist.md` on a second screen or print it. You will tick it as you go.

## 0c. Check the machines (15 min)

### Windows host

**Do:** open PowerShell. Paste:

```
python -c "import scapy, pandas, sklearn, matplotlib, tabulate; print('ok')"
```

**You should see:** `ok`.

**If not** (an error says `No module named ...`): paste

```
pip install scapy pandas numpy scikit-learn matplotlib tabulate
```

wait for it to finish, then run the check again.

**If `python` is not found:** try `py` instead of `python` everywhere in this guide.

### Kali

**Do:** open a terminal in Kali. Run these one at a time:

```
snort -V
hydra -h | head -2
nmap --version | head -1
```

**You should see:** a version line for each.

**If one says `command not found`:** `sudo apt update && sudo apt install -y snort hydra nmap`. If asked questions during the Snort install, press Enter to accept the defaults.

**If there is no internet in Kali:** write "tool X not installed, no internet" in the log, and use the alternative: Wireshark display filters replace Snort (C3), and the Python or SQL queries replace the rest.

### Both VMs on the same network

**Do:**

1. In your hypervisor, set both VMs to the **same** host-only or internal network adapter.
2. Start both.
3. In Kali: `ip a`. Find the line starting `inet 192.168...` (or `10....`). **Write down the address as KALI-IP.**
4. In Metasploitable log in with `msfadmin` / `msfadmin`. Run `ifconfig`. **Write down the `inet addr` as MSF-IP.**
5. In Kali: `ping -c 3 [MSF-IP]`.

**You should see:** `3 packets transmitted, 3 received, 0% packet loss`.

**If 100% packet loss:** both VMs are on different networks. Go back to step 1.

### Snapshots

**Do:** in the hypervisor take a snapshot of each VM called `clean`. **Do this before any attack.**

**Log:** `01 | tools checked, IPs: KALI=[x], MSF=[y], snapshots taken | notes`

## 0d. Test the data download (10 min)

**Do**

1. Open a browser. Go to `kaggle.com` and search `CIC-IDS2017`.
2. Also try `huggingface.co` and search the same.

**You should see:** a data set page with files.

**If blocked, or you need an account you do not have:** write "blocked" in the log. Use the fallback: `python3 gen_practice_pcap.py practice.pcap` (from `ex3-monitor`). In the write-up say clearly the data is **synthetic**.

---

## A1. Get the large data set (20 min)

**Do**

1. On the data set page find the file list.
2. Pick **one** CSV for one day. The Tuesday file contains FTP and SSH brute force, matching your lab story.
3. Download only that file.
4. Move it into `Ex3_Day1/outputs`.
5. In PowerShell: `Get-FileHash -Algorithm SHA256 "C:\path\to\file.csv"`. Copy the long Hash value into your notes.
6. Screenshot the download page (**fig01**).

**You should see:** a file of tens or hundreds of MB.

**Write in `notes/datasets.txt`:**

```
Data set: CIC-IDS2017
Day used: [Tuesday]
URL: [paste]
Authors: Sharafaldin, Habibi Lashkari, Ghorbani (ICISSP 2018)
Downloaded: [today's date and time]
SHA-256: [paste]
```

**Log:** `fig01 | download page for CIC-IDS2017 | screenshots/fig01_dataset_page.png`

---

## A2. Make your own capture (30 min)

**Everything here is run in Kali against MSF-IP only.**

### A2.1 Start the capture

**Do:** in a Kali terminal:

```
sudo tcpdump -i eth0 -w ex3_own.pcap
```

(If `eth0` is wrong, `ip a` shows the real interface name. Replace `eth0` with it.)

**You should see:** `listening on eth0 ...`. The terminal stays busy. **Leave it running.**

**Write down the clock time now.** This is NORMAL START.

### A2.2 Normal traffic (5 min)

**Do:** open a **second** terminal in Kali. Run each, one by one:

```
ping -c 20 [MSF-IP]
curl -s http://[MSF-IP]/ | head -5
curl -s http://[MSF-IP]/ | head -5
ftp [MSF-IP]
```

For the `ftp` line: when asked for a name type `msfadmin`, then the password `msfadmin`. Type `quit` to leave.

**You should see:** replies from the ping, some HTML from curl, and `230 Login successful` from FTP.

**If `ftp` is refused:** write it in the log. Use `telnet [MSF-IP]` for a normal login instead.

**Write down the clock time now.** This is NORMAL END.

### A2.3 Attack traffic (10 to 15 min)

**Write down the clock time.** This is ATTACK START.

**1. Port scan**

```
nmap -sS -p- [MSF-IP]
```

This takes 1 to 5 minutes. You will see a list of open ports at the end.

**2. Make a password list**

```
printf 'password\n123456\nadmin\nletmein\nqwerty\n%.0s' {1..10} > /tmp/words.txt
wc -l /tmp/words.txt
```

**You should see:** `50 /tmp/words.txt`.

**3. Password guessing (use the one that works)**

SSH first:

```
hydra -l msfadmin -P /tmp/words.txt -t 4 ssh://[MSF-IP]
```

**If SSH is refused** (typical on Metasploitable): use FTP instead:

```
hydra -l msfadmin -P /tmp/words.txt -t 4 ftp://[MSF-IP]
```

**You should see:** hydra prints attempts and may find or not find a password. Either result is fine.

**4. Web scan**

```
nikto -h http://[MSF-IP]/
```

Takes a few minutes. You can press Ctrl+C after 2 minutes.

**Write down the clock time.** This is ATTACK END.

### A2.4 Stop and save

1. Go back to the first terminal. Press **Ctrl+C**.
2. You will see `N packets captured`. **Write N down.**
3. Check the file: `ls -lh ex3_own.pcap`.
4. Copy the file to Windows (shared folder, `scp`, or drag and drop) into `Ex3_Day1/ex3-monitor`.

**On Windows:**

5. Open `ex3_own.pcap` in Wireshark. Screenshot (**fig02**).
6. Hash it: `Get-FileHash -Algorithm SHA256 ex3_own.pcap`. Add to `datasets.txt`.

**Revert** both VMs to `clean` **after** you have copied the log files (see A3b).

**Write the four times in `notes/times.txt`:**

```
NORMAL START: [hh:mm:ss]
NORMAL END:   [hh:mm:ss]
ATTACK START: [hh:mm:ss]
ATTACK END:   [hh:mm:ss]
```

**Log:** `fig02 | own capture opened in Wireshark | ...` and `02 | times recorded, hydra used [ssh/ftp] | notes/times.txt`

---

## A3. Load the capture into a database and run the SQL (40 min)

### A3.1 Load

**Do:** in PowerShell:

```
cd C:\path\to\Ex3_Day1\ex3-monitor
python pcap_to_sqlite.py ex3_own.pcap --db own_traffic.db --csv own_traffic.csv
```

**You should see:** `<N> packets -> own_traffic.csv, own_traffic.db`. Write N down.

**If it errors:** copy the last line of the error into the log. Check the file name is exactly right and you are in the right folder (`dir` should list `pcap_to_sqlite.py`).

### A3.2 Open the database

1. Open **DB Browser for SQLite**.
2. **File, Open Database**. Choose `own_traffic.db`.
3. Click the **Browse Data** tab. You should see a table called `packets` with rows.
4. Click the **Execute SQL** tab. You will paste queries here.

**To run a query:** paste it, press **Ctrl+Return**. Results appear in the grid below.

### A3.3 Run the queries

**Do:** open `queries.sql` in Notepad. Copy **one query at a time** into Execute SQL. After each:

1. Look at the result.
2. Write one line in your notes: what it shows.

**Screenshot these (crop to the result grid):**

| Query | What it finds | Figure |
| --- | --- | --- |
| 1 | Top senders | fig04 |
| 3 | Port scan (many ports from one source) | fig05 |
| 5 | Brute force (many connections to login ports) | fig06 |

**It is normal for some queries to return nothing.** Your lab has no external hosts, so query 6 (exfiltration) shows no rows. Write: "none seen, the lab has no external hosts". **Never invent a result.**

**If a query returns no rows because the threshold is high** (for example `more than 50 ports`): change the number to a smaller one, rerun, and write "I lowered the threshold from [50] to [10] because [the lab has only two hosts]".

### A3.4 Baseline vs attack

See step A4.5 further down this file. Do it now. It uses the four times you wrote down.

---

## A3b. Add the login log and design the database (30 min)

**Why:** a Pass item asks for a designed database with different kinds of data.

### Step 1: draw the design (paper is fine)

Draw four boxes and one line label:

```
packets (one row per packet)      flows (one row per connection)
flows_ids (CIC-IDS2017 flows)     auth_events (failed logins)
Link between tables: source IP address (src)
```

Take a photo or screenshot (**fig04a**).

### Step 2: get the login log (do this BEFORE reverting the VMs)

**If you attacked with SSH:** on Metasploitable run `sudo cp /var/log/auth.log /tmp/` (or `/var/log/messages`). Copy to Windows as `auth.log`.

**If you attacked with FTP (SSH refused):** on Metasploitable run `sudo cp /var/log/vsftpd.log /tmp/`. Copy to Windows as `vsftpd.log`.

**If you cannot copy any log:** skip to step 4 and use the Wireshark fallback.

### Step 3: load it

**SSH:** save the `load_auth.py` script from `ex3_guide.md` section A3b in `ex3-monitor`, then:

```
python load_auth.py
```

(It reads `auth.log` and writes into `traffic.db`. **Edit the file name inside the script from `traffic.db` to `own_traffic.db` if that is the name you used.**)

**FTP:**

```
python load_ftp.py own_traffic.db vsftpd.log
```

**You should see:** `N failed ... logins loaded` and a list of `(source IP, count)`. **The top source should be the Kali IP.**

**If it loads 0 rows:**

1. In PowerShell run `Select-String -Path vsftpd.log -Pattern "FAIL" | Select-Object -First 3`.
2. Copy one real line into your notes.
3. Say: "The log format did not match the pattern, so I used the Wireshark fallback."

### Step 4: Wireshark fallback (works with FTP and needs no log)

1. Open `ex3_own.pcap` in Wireshark.
2. In the filter bar type `ftp.response.code==530`. Press Enter.
3. The status bar at the bottom shows **Displayed: N**. That is the number of failed logins. Screenshot (**fig04c**).

### Step 5: join the two sources

In DB Browser, **Execute SQL**:

```sql
SELECT a.src, a.n AS failed_logins, p.ports AS distinct_ports
FROM (SELECT src, COUNT(*) AS n FROM auth_events GROUP BY src) a
JOIN (SELECT src, COUNT(DISTINCT dport) AS ports FROM packets GROUP BY src) p ON a.src = p.src;
```

**You should see:** one row, the Kali IP, with the failed login count and the number of distinct ports. Screenshot (**fig04b**).

**Write:** "The same source address appears in the packet data and the service log, with [N] failed logins and [M] ports. Two independent sources agree."

### Step 6: graph idea (knowledge item)

```sql
SELECT src, COUNT(DISTINCT dst) AS out_degree FROM packets GROUP BY src ORDER BY out_degree DESC;
```

**Write:** "Treating hosts as nodes and conversations as edges, each source has [1] neighbour, so the graph is trivial in a two-VM lab. In a real network a scanner would have a high out-degree."

### Step 7: now revert

Revert both VMs to `clean`. **Only now.**

**Log:** `fig04a | database design | ...`, `fig04b | join of packets and logins | ...`, `03 | auth_events loaded via [load_auth/load_ftp/wireshark] | ...`

---

**Next:** A4, below.

---



For each step in the sections below:

- **Do** = exactly what to click or type
- **You should see** = what a correct result looks like
- **Write** = example wording for your notes. Replace anything in [square brackets] with your own result.

**Every number marked EXAMPLE is a demonstration, not your result.** Never copy an example number into your work. Use your own.

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

---





**Anything marked EXAMPLE is there to show the shape. Do not copy example scores, costs or names into your work. Use your own, and label them as assumptions.**

**Timing:** D 2h, E 1h15, F 45m, G 1h15, H 45m, upload by 14:30. Deadline is 16:00.

---

## D. Risk modelling and trades (this is the only row that can earn Merit or Distinction)

You need: a risk register, **two methods** compared and contrasted (Merit), and **investment options** (Distinction).

### D1. Assets (15 min)

**Do:** make a table with five columns: ID, Asset, Owner, Where it lives, Value (H/M/L).

**EXAMPLE rows (adapt to <company>):**

| ID | Asset | Owner | Where | Value |
| --- | --- | --- | --- | --- |
| A1 | Patient care notes | Care Director | Cloud sync service | H |
| A2 | Carer login credentials | IT lead | Identity provider | H |
| A3 | Monitoring logs and database | Security analyst | Analyst laptop | M |
| A4 | Mobile app and sync service | Product lead | Cloud hosting | H |
| A5 | Staff laptops | IT lead | Offices and homes | M |

**Check:** five to eight assets is enough. Every asset has an owner.

### D2. Threat and vulnerability list (15 min)

**Do:** for each asset ask: "Who or what could harm it, and how?" Write one line each.

**Use your own lab evidence where you can:**

| Threat | Vulnerability | Evidence from my work |
| --- | --- | --- |
| Credential guessing on an exposed service | Weak or default passwords, cleartext protocol (FTP) | Failed-login log and Snort rule 1000006 (fig [x]) |
| Reconnaissance before attack | Services visible from the network | nmap scan seen in baseline comparison (fig [x]) |
| Data theft by a malicious insider | Over-wide access | Not tested, assumption |
| Monitoring blinded | Logs on one machine only | A6 table |

### D3. Likelihood and impact scales (10 min)

**Do:** write the scale once and use it for every risk.

| Score | Likelihood | Impact |
| --- | --- | --- |
| 1 | Rare (less than once in 5 years) | Minor, no patient effect |
| 2 | Unlikely | Small disruption |
| 3 | Possible (about yearly) | Some patient or data effect |
| 4 | Likely | Serious effect on patients or data |
| 5 | Almost certain | Severe harm or major breach |

**Risk score = likelihood x impact** (1 to 25). Rating: 1 to 5 Low, 6 to 12 Medium, 15 to 25 High.

**Write one sentence of limitation:** "Scores are my judgement and are not measured, so two people could score differently."

### D4. The risk register (30 min)

**Do:** a table with these columns: ID, Risk (threat on asset), L, I, Score, Rating.

**EXAMPLE (scores are illustrations only):**

| ID | Risk | L | I | Score | Rating |
| --- | --- | --- | --- | --- | --- |
| R1 | Credential brute force on exposed service gives access to patient notes | 4 | 5 | 20 | High |
| R2 | Phishing of a carer account | 4 | 4 | 16 | High |
| R3 | Lost unencrypted staff laptop | 3 | 4 | 12 | Medium |
| R4 | Monitoring logs deleted by an intruder | 2 | 4 | 8 | Medium |
| R5 | Sync service outage | 3 | 3 | 9 | Medium |

**Do:** sort by score. The top two are your "significant risks" for the rest of D and E.

**Draw the model (needed for "risk model showing relationships"):** on paper draw:

```
Threat actor -> exploits -> Vulnerability -> on -> Asset -> causes -> Impact
                                                   ^
                                   Control reduces likelihood or impact
```

Label it with R1 as your example (attacker, weak password, patient notes, data breach).

### D5. Second method and comparison (Merit) (40 min)

The brief wants two methods from: **SABSA, DBSy, CVSS, STRIDE, NIST 800-154**, compared and contrasted. Use **STRIDE** and **CVSS**. They are quick and suit your lab.

**Method 1: STRIDE (threat categories) on one component.**

**Do:** take the monitoring database or the FTP service. For each letter, write whether it applies:

| Letter | Meaning | Applies to [component]? | How |
| --- | --- | --- | --- |
| S | Spoofing | Yes | Attacker logs in with guessed credentials |
| T | Tampering | Yes | Edit `own_traffic.db` to hide the scan |
| R | Repudiation | Yes | No user-level audit of who ran queries |
| I | Information disclosure | Yes | Cleartext FTP shows passwords |
| D | Denial of service | Possible | SYN flood on the service |
| E | Elevation of privilege | Possible | vsftpd 2.3.4 backdoor (CVE-2011-2523) gives a shell. **Cite only, do not exploit.** |

**Method 2: CVSS (severity score for one specific vulnerability).**

**Do:**

1. Open the FIRST CVSS v3.1 calculator in your browser (search "FIRST CVSS 3.1 calculator").
2. Pick one vulnerability, such as the vsftpd backdoor.
3. Click the value for each metric, in order: Attack Vector, Attack Complexity, Privileges Required, User Interaction, Scope, Confidentiality, Integrity, Availability.
4. Read the **Base Score** and **vector string** at the top. Screenshot it.

**Known examples to check your clicking:**

| Vector | Base score |
| --- | --- |
| `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H` (remote, no login, full compromise) | 9.8 Critical |
| `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N` (remote, no login, read data only) | 7.5 High |
| `AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N` (remote, low login, read data only) | 6.5 Medium |

If your result differs from these for the same clicks, you clicked a wrong metric.

**Compare and contrast table (write this):**

| Question | STRIDE | CVSS |
| --- | --- | --- |
| What does it produce? | A list of threat types per component | A number from 0 to 10 per vulnerability |
| When is it used? | Design and early analysis | When a specific vulnerability is known |
| Needs technical detail? | Moderate | High (you must know how it is exploited) |
| Considers business impact? | No | Not by itself (base score ignores your assets) |
| Weakness | Gives no ranking | Same score for a patient system and a test box |
| Strength | Finds threats before vulnerabilities exist | Repeatable and widely understood |

**Write (3 to 4 sentences):** "STRIDE found [N] threat types for [component], including [two]. CVSS scored the [vulnerability] at [score]. The two methods are complementary: STRIDE identified what could go wrong without needing a known flaw, and CVSS ranked the one known flaw. I used STRIDE to extend the register and CVSS to raise the likelihood of R1 from [x] to [y], because a remote, unauthenticated flaw with a published exploit is easy to attack."

### D6. Treatment options and trades (25 min)

**Do:** for each of your top two risks write **three options** (technical, procedural, monitoring or design).

**EXAMPLE for R1:**

| Option | Type | Reduces | Cost (assumed) | Trade-off |
| --- | --- | --- | --- | --- |
| Replace FTP with SFTP and enforce strong passwords plus lockout | Technical | Likelihood | Low | Staff retraining, small usability cost |
| Add multi-factor authentication | Technical | Likelihood | Medium | Extra step for carers on shift |
| Alert on failed logins (Snort rule 6, log monitoring) | Monitoring | Time to detect | Low | Needs an analyst to respond |

**Residual risk:** after the chosen option, re-score. EXAMPLE: R1 L 4 to 2, I stays 5, new score 10, Medium. Write what remains: "stolen credentials from phishing would still work, which is why R2 is treated next."

### D7. Investment options (Distinction) (20 min)

**Do:**

1. Pick a **quantitative** measure. Simple one: **Annual Loss Expectancy (ALE) = Single Loss Expectancy (SLE) x Annual Rate of Occurrence (ARO).**
2. For R1 write your assumptions. **Label every number "assumed".**

**EXAMPLE only (invented figures):**

| Item | Value | Basis |
| --- | --- | --- |
| SLE | 200,000 | Assumed cost of a breach: response, notification, loss of trust |
| ARO | 0.5 | Assumed once every two years |
| ALE before | 100,000 | 200,000 x 0.5 |
| Option A (SFTP and lockout) | cost 5,000 per year, ARO falls to 0.1 | Assumed |
| ALE after A | 20,000 | 200,000 x 0.1 |
| Benefit | 80,000 | 100,000 minus 20,000 |
| Option B (MFA) | cost 25,000 per year, ARO falls to 0.05 | Assumed |
| ALE after B | 10,000 | 200,000 x 0.05 |
| Benefit | 90,000 | 100,000 minus 10,000 |

3. Work out **net benefit = benefit minus annual cost** for each option. EXAMPLE: A = 75,000, B = 65,000.
4. **Rank the options.** Write which you recommend and what you would do with the budget.

**Write (4 sentences):** "I compared [options] using ALE. Option [A] gives the best net benefit of [x] on my assumptions. The figures are assumed, not measured, so I would test sensitivity by changing the ARO by [50 percent] and checking whether the ranking changes. I would still [add the other option] for [reason], because [residual risk from a different threat]."

**Be honest:** "These costs are illustrative and would be replaced with <company> data."

---

## E. Risk assessment to an external standard (ISO/IEC 27005:2022)

### E1. Say why

**Write:** "I used ISO/IEC 27005:2022 because it is the information security risk standard that pairs with ISO/IEC 27001 and gives me a repeatable process. I rejected NIST SP 800-30 for this task because [it is US government oriented / I wanted the 27001 control mapping]." (Swap if you chose NIST.)

### E2. Walk through the stages (use these headings in your document)

| Stage | Do this | Where in your work |
| --- | --- | --- |
| Context | Scope, assets, assumptions, dependencies, criteria | D1, D3 |
| Risk identification | Assets, threats, vulnerabilities, consequences | D1, D2 |
| Risk analysis | Likelihood and impact | D4 |
| Risk evaluation | Compare to criteria, decide priority | D4 sort |
| Risk treatment | Choose options, controls | D6 |
| Monitoring and review | Plan to repeat and check | F |
| Communication | Who is told what | G |

### E3. Fill the table (example rows, adapt)

| Risk | Treatment | ISO/IEC 27001:2022 Annex A control | Status | Gap |
| --- | --- | --- | --- | --- |
| R1 | Mitigate | A.8.5 Secure authentication | Partly in place | No lockout, cleartext protocol |
| R1 | Mitigate | A.8.16 Monitoring activities | Done in lab (Snort, queries) | Not in production |
| R2 | Mitigate | A.6.3 Information security awareness, education and training | Not in place | No phishing training |
| R3 | Mitigate | A.8.1 User endpoint devices | Partly | Disk encryption unconfirmed |
| R4 | Mitigate | A.8.15 Logging | Partly | Logs not copied off the host |

**Check the control numbers against the standard yourself before submitting.** The 2022 edition has 93 controls in four themes: organisational (5), people (6), physical (7), technological (8). If your copy differs, use yours.

### E4. Limits (write 3 sentences)

- Scores are subjective (D3).
- The assessment covered a lab and one case study, not a live network.
- I did not have access to <company> records, so likelihood is judgement.

### E5. Evidence of following the standard

**Write:** "Each stage of ISO/IEC 27005 is mapped to a section of this document in E2, so another analyst can repeat the process and reach a comparable register."

---

## F. Management system and plan (ISO/IEC 27001, Plan-Do-Check-Act)

### F1. Context (5 lines)

**Write:** "<company> provides [care software]. Interested parties: patients, carers, regulators, the NHS or local authority customers, suppliers. Scope: [the sync service, the mobile app and staff laptops]."

### F2. Roles table

| Role | Responsibility |
| --- | --- |
| Board or Director | Approves policy and budget |
| Information Security Manager | Owns the plan and risk register |
| IT lead | Implements controls |
| Security analyst | Monitors and triages alerts |
| All staff | Follow policy, report incidents |

### F3. Objectives with measures (mark as proposals)

| Objective | Measure | Target (proposal) | Review |
| --- | --- | --- | --- |
| Detect brute force quickly | Mean time from first failed login to alert | Under 5 minutes | Monthly |
| Reduce phishing success | Click rate in simulated phishing | Under 5 percent | Quarterly |
| Keep devices protected | Share of laptops with disk encryption | 100 percent | Quarterly |
| Handle incidents well | Tabletop exercise actions closed | 90 percent in 30 days | After each exercise |

### F4. The plan (cover all six, one line each)

1. **Risk treatment:** treat the register, review top risks quarterly.
2. **Access management:** least privilege, MFA, joiner-mover-leaver process.
3. **Monitoring:** logs from authentication, network and IDS reviewed daily.
4. **Incident management:** plan in section G.
5. **Training:** onboarding and yearly refresher, with phishing tests.
6. **Continual improvement:** Plan (assess and set objectives), Do (implement), Check (measure and audit), Act (correct and update).

### F5. What triggers a rethink

**Write:** "Changes in threat (a new vulnerability in the sync service), technology (a move to a new cloud provider) or regulation (a change to data protection law) trigger reassessment of the register and an update to the plan."

---

## G. Incident response and third parties

### G1. Phases

Write one line for each: **Preparation, Identification, Triage, Containment, Eradication, Recovery, Post-incident review.**

**EXAMPLE for your scenario (credential attack):**

- **Identification:** Snort rule 6 fires and the log shows many FAIL LOGIN lines.
- **Triage:** check if any login succeeded. If yes, P1.
- **Containment:** block the source address and disable the targeted account.
- **Eradication:** reset credentials, remove any persistence, patch or replace the vulnerable service.
- **Recovery:** restore service, monitor closely for a week.
- **Review:** what we missed, update rules and plan.

### G2. Roles and authority

| Role | Decision |
| --- | --- |
| Incident lead | Declares an incident and its severity, authorises containment |
| Security analyst | Investigates, preserves evidence |
| Communications lead | Customer, staff and media messages |
| Legal or data protection officer | Regulator notification decision |
| Director | Authorises shutting a service or paying for outside help |

### G3. Severity

| Level | Criterion | Escalation |
| --- | --- | --- |
| P1 | Confirmed compromise or personal data leaving | Incident lead and director at once |
| P2 | Attack in progress, no confirmed access | Incident lead within 1 hour |
| P3 | Failed or low-impact attempt | Analyst, log and review |

**When to ask for specialist help:** "If I cannot confirm what the attacker accessed, or if patient data is involved, I would call an external incident response provider."

### G4. Third parties (cover at least three)

| Third party | Role | When involved | What we share |
| --- | --- | --- | --- |
| Cloud provider | Logs, takedown, infrastructure support | Incident in their environment | Time range, resource IDs |
| Managed security service | Out-of-hours monitoring and response | P1 or P2 | Alerts, log copies |
| External forensic or IR team | Investigation | Unknown scope | Disk images, hashes |
| Customers (health bodies) | Contract duty to notify | Their data affected | Summary of impact |
| Regulator (ICO) | Notification | Personal data breach likely to risk individuals | Facts of the breach |
| Police | Crime report | Criminal activity | Evidence copy |

**Secure sharing (write):** "Evidence is shared as copies, never originals. I record SHA-256 hashes before sending and send over an encrypted channel. Access is limited to named people."

### G5. Notification

**Write:** "Under UK GDPR Article 33 a personal data breach must be reported to the regulator within 72 hours of becoming aware, unless it is unlikely to result in a risk to individuals. If the risk is high, affected individuals are told directly without undue delay. Customers may also be due notice under their contracts."

### G6. Tabletop exercise (do it: 15 min)

**Do:** set a timer. Walk through this scenario out loud, writing what you would do at each step.

1. **Alert (11:20):** many failed logins on the sync service.
2. **Inject (11:30):** one login succeeded from the same address.
3. **Inject (11:45):** an unusual download of 2,000 records is seen.
4. **Decision:** who declares the incident, who is told, what do you contain first?

**Write a table:**

| Step | Decision made | Gap found |
| --- | --- | --- |
| 1 | Analyst raises P2 | No on-call number for the incident lead |
| 2 | Escalate to P1 | No rule for disabling accounts out of hours |
| 3 | Start 72-hour clock | Unclear who tells the customer |

The gaps column is the evidence of improvement. **Find at least two real gaps.** Write: "I would fix these by [actions]."

---

## H. The justification (1,000 words, 45 min)

### H1. Method

1. Open `ex3_justification.md` and copy it to a Word document.
2. Fill one part at a time using the prompts. **Write 3 to 5 short sentences per part.**
3. After each part, put its **figure numbers** in brackets.
4. Delete the prompts.

### H2. Worked example of one part (Part 4, about 200 words)

**EXAMPLE shape (replace everything in brackets with your results):**

"I recorded [5] risks in a register scored on a 1 to 5 likelihood and impact scale (Fig [20]). The highest was R1, credential guessing on an exposed service, scored [20]. I compared STRIDE and CVSS. STRIDE found [six] threat types for the service, while CVSS scored the [vsftpd backdoor] at [9.8], which led me to raise R1's likelihood. STRIDE is better for finding threats early, but gives no ranking. CVSS ranks, but ignores the value of the asset (Fig [21]). For investment I compared [SFTP with lockout] and [multi-factor authentication] using ALE (Fig [22]). On my assumed figures [SFTP and lockout] gave the best net benefit, so I chose it, accepting that [phishing] remains a risk. I assessed to ISO/IEC 27005:2022 because it pairs with ISO/IEC 27001 and I rejected NIST SP 800-30 because [reason] (Fig [23]). Gaps include [lockout and logging]. My costs are assumptions."

### H3. Word count

- **Word:** bottom-left of the window shows words. Select the whole text first so headings are included or excluded consistently.
- **Target:** 900 to 1,100.
- **Over?** Cut examples first, then repeated explanation.
- **Under?** Add the "alternative rejected" and "remaining risk" lines from the 5-part pattern.

### H4. Final checks (15 min)

1. Every figure number in the document is also in the text.
2. Every item in `ex3_brief_checklist.md` has a tick.
3. Say what is pre-written: `pcap_to_sqlite.py`, `analysis.py`, `queries.sql`, `local.rules`. Say what **you** changed or ran.
4. Say what is synthetic or untested (for example, "Snort was run on a recorded capture, not live traffic").
5. Save as **PDF if the brief says so, otherwise Word.** Check the file name rule in your exam pack.
6. **Upload to Blackboard by 14:30.** Open the upload afterwards and confirm it opens.

---

## Final checklist (tick before you submit)

- ☐ Every one of the 8 topics in `ex3_brief_checklist.md` is ticked
- ☐ Every figure number in the document has a screenshot and a mention in the text
- ☐ Evidence log matches the files
- ☐ Justification is between 900 and 1,100 words
- ☐ Pre-written tools are named, and what you changed or ran is stated
- ☐ Anything synthetic, blocked or failed is stated honestly
- ☐ File opens, correct name, correct format
- ☐ Uploaded to Blackboard by 14:30
- ☐ Opened the uploaded copy to check

## If something breaks

| Problem | Do this |
| --- | --- |
| Download blocked | Use `gen_practice_pcap.py`, say it is synthetic |
| SSH refused | Use FTP (A2.3 step 3, A3b step 3) |
| `dig ANY` returns nothing | Query each type: `dig [domain] A`, `NS`, `MX`, `TXT` separately (many servers refuse ANY, RFC 8482) |
| Snort will not run | Use Wireshark filters and the SQL queries, say so |
| Script error | Copy the last line of the error into the log, check the file name and folder, try once more, then move on |
| Out of time | Finish the Pass items first. Merit and Distinction are in D only |
