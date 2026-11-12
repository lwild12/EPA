# Tables 1 to 3 (templates)

The same three tables are in `ex2_tables.docx`. Use whichever you prefer. The cells that are filled in are **suggestions from Thursday evening**. Check each one against your figures and replace it with your own words.

## Scoring key (put this under Table 1)

- **High:** seen directly in CAPE, or confirmed by 2 or more sources.
- **Medium:** seen once, or the item is also used legitimately.
- **Low:** from an unreliable tool, or never seen in the sandbox.

## Table 1: Intel

| Indicator | Type | Source | Reliability | Allowlist? | Enrichment | Confidence | Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `699ec052ecc898bdbdafea0027c4ab44c3d01ae011c17745dd2b7fbddaa077f3` | File hash | CAPE, VT, MWDB, Bazaar | | | | | |
| `checkip.dyndns.org` | Domain | CAPE DNS | | | | | |
| `Run\xws` | Registry key | CAPE | | | | | |
| `Temp\xws\xws.exe` | File path | CAPE | | | | | |
| `1.0.0.0`, `4.0.0.0` etc. | Static "IPs" | Triage script | | | | | |
| `lencr.org` (Let's Encrypt) | Domain | CAPE DNS | | | | | |
| Microsoft / Akamai hosts | IPs | CAPE hosts | | | | | |

Suggested starting points (verify each, then write your own):

| Indicator | Reliability | Allowlist? | Enrichment idea | Confidence | Action |
| --- | --- | --- | --- | --- | --- |
| Hash | High: CAPE plus VT, MWDB and Bazaar agree | No | YARA `agent_tesla` and `AgentTeslaV2`; .NET file | High | Block hash in EDR; SIEM watchlist |
| `checkip.dyndns.org` | Medium: seen in CAPE but a legitimate service | Not blanket | Public IP-lookup site; CAPE flags `recon_checkip`, `network_dyndns`; do a WHOIS | Medium | Alert on non-browser processes calling it |
| `Run\xws` | High: seen in CAPE | No | Persistence key (T1547.001); matches the dropped `xws.exe` | High | Detect new Run keys pointing into Temp |
| `Temp\xws\xws.exe` | High: seen in CAPE | No | Dropped copy of the malware | High | Application control: block execution from Temp |
| `1.0.0.0` etc. | Low: from the triage script | n/a | Version strings, not network traffic; not in the CAPE hosts list | Low | Discard as false positives |
| `lencr.org` | High that it is benign | Yes | Let's Encrypt certificate checks (CNAME in the DNS screenshot) | High (benign) | Allowlist |
| Microsoft / Akamai hosts | High that it is benign | Yes | `azureedge.net` and `akamaiedge.net` CNAMEs in the DNS screenshot; probably Windows background traffic (assumption) | High (benign) | Allowlist; exclude from IOCs |

Then write 2 lines: **what changed after enrichment** (e.g. "7 indicators became 3 actionable ones: 1 hash, 1 behavioural domain, 2 host artefacts"). Adjust to your real result.

## Table 2: Malware mechanisms

Label each row **Observed** (you saw it) or **Known** (from reporting).

| Stage | Mechanism | Evidence (Fig) | ATT&CK ID | Detect / contain at CareLink |
| --- | --- | --- | --- | --- |
| Access | **Known:** phishing attachment or malicious download. Not seen in the sandbox. | none; cite your source | T1566 (verify on attack.mitre.org) | Email gateway; awareness training; block risky file types |
| Execution | **Observed:** .NET file started from `explorer.exe`; YARA strings show it targets saved passwords and cookies, plus a keyboard hook; spawned `shutdown -r -t 5` | Figs 1, 3, 4 | T1129, T1106, T1059 (Fig 7) | EDR alerts on unusual process trees; application control |
| Persistence | **Observed:** `Run\xws` points to `Temp\xws\xws.exe` | Figs 5, 6 | T1547.001 (Fig 7) | Alert on new Run keys pointing into Temp |
| Evasion | **Observed:** packed or encrypted payload, process injection, AMSI enumeration, `mscfile` command change (elevation trick) | Figs 1, 2, 3, 4, 6, 7 | T1027, T1055, T1562, T1548 (Fig 7) | EDR; AMSI; registry monitoring for `mscfile` changes |
| C2 / exfil | **Observed:** DNS lookup of `checkip.dyndns.org`. **Known, not observed:** exfiltration by SMTP, FTP or HTTP | Fig 8 | T1071, T1568 (Fig 7) | DNS and egress filtering; short-lived tokens; block outbound SMTP and FTP from clinical devices |

### Merit paragraph skeleton: "how I saw past the packing"

Fill in the blanks in your own words (3 lines):

1. Static analysis showed ____ (one import, entropy ____), which suggested the file was ____ (Figs 1, 2).
2. In the sandbox, the sample ____ (started a child process, process injection signatures) (Fig 3).
3. YARA matched the ____ (process dumps), not the packed file, with strings such as ____ (Fig 4). This showed the unpacked payload.

### Two more lines

- Why the triage script said "low suspicion" while YARA said Agent Tesla: ____ (a .NET file has one import by design, so import-based rules miss it).
- What is mine and what is pre-written: ____ (the triage script was pre-written; I ____).

## Table 3: Threats

| Threat | Asset | Entry point | Technique | Impact | Control (mitigation) | Tested? |
| --- | --- | --- | --- | --- | --- | --- |
| Infostealer | Clinical devices | User download or phishing attachment | Steals saved passwords and cookies; keylogging (your sample) | Stolen credentials reach the care system; patient data exposed | EDR; short-lived tokens; MFA; small cache; isolate device and revoke tokens | Technique: yes (sandbox, Figs 3 to 6). Controls: no. |
| Phishing for credentials | Credentials and API tokens | Email link or attachment | Fake sign-in page; token theft | Attacker acts as the user and gets the sync API token | Phishing-resistant MFA (passkeys); conditional access; email gateway; awareness training | No |
| Lost or stolen device | Cached visit notes | Physical loss | Reading cached notes | Patient data exposed; unsynced notes lost | Full-disk encryption; lockout timer; MDM remote wipe; wipe timer | No |
| Helpdesk reset | User accounts | Phone or chat to helpdesk | Impersonating a clinician to get a reset | Account takeover | Identity check script; call back on a known number; manager approval for MFA resets; alert on resets | No |
| Supplier access | Care management system (SaaS) | Supplier accounts | Abusing or compromising supplier access | Access to patient records | Least privilege; time-limited access; MFA; logging; access review; supplier assurance | No |
| API token guessing | Sync API | API endpoint | Brute-forcing tokens; SQL injection attempt | Unauthorised access to patient data | Rate limiting and lockout; strong random tokens; input validation | **Yes:** Figs 9a, 9b |

Only mark **Tested? Yes** where you have a figure. Never write "secure".

### Merit sentence skeleton (rows 4 and 5: processes and services)

"An employee could enable this attack without realising it by ____ . The control is ____ ."

### Boundaries paragraph skeleton (3 lines)

- **Assets:** ____ (patient records in the cloud care system; clinician devices).
- **Entry points:** ____ (devices, sync API, supplier access).
- **Trust boundaries:** device to API; API to database. **Assumption:** the care system is delivered as SaaS, so its hosting is out of scope.
