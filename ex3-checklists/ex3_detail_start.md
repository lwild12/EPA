# Ex3 detailed steps: start of Tuesday (steps 0 to A3b)

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

See step A4.5 in `ex3_detail_tuesday.md`. Do it now. It uses the four times you wrote down.

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

**Next:** `ex3_detail_tuesday.md`, starting at A4.
