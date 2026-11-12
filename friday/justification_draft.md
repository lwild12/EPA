# Ex2 justification: DRAFT for you to check, adapt and retype

**This is a draft, not a finished answer.** Do not paste it. Read each claim, check it against your own evidence (figures, tables, notes), and retype it in your own words.

How to use it:

1. Fix every `[CONFIRM: ...]`. Each one is something I could not verify from your files.
2. Cross out any sentence that is not true of your work. Add what you did that I missed.
3. Keep the figure and table numbers matching your document.
4. Run `wc -w` on the body only (between the two lines marked START and END). It must be 900 to 1,100.
5. Honesty rule: say what is your own work and what is pre-written or adapted.

**Claims to check before you rely on them**

| Claim in the draft | Where to check |
| --- | --- |
| Triage script rated the sample "LOW suspicion" | `report.md`, Fig 1 |
| One import, `_CorExeMain`; entropy 6.96 | Fig 1 |
| "Encrypted or compressed data" warning; VT, MWDB and Bazaar tags on the hash | Fig 2 |
| Child process and injection signatures | Fig 3, Fig 7 |
| YARA hits on dumps: `GetSavedPasswords`, `GetSavedCookies` | Fig 4 |
| `Run\xws` pointing at `Temp\xws\xws.exe` | Figs 5, 6 |
| `mscfile` command change; AMSI enumeration | Fig 6, Fig 7 |
| DNS lookup of `checkip.dyndns.org` | Fig 8 |
| Exfiltration NOT observed | Your notes; say so |
| 200 invalid tokens, all 401, no lockout | Figs 9a, 9b |
| sqlmap: 752 x 400, "not injectable" | `sqlmap.txt` |
| Sandboxes isolated; no CareLink data uploaded | Your RoE; confirm the real set-up |
| Hash re-checked at the end | Only if you actually do it on Friday |
| External sources you name (NCSC, CISA KEV, MITRE ATT&CK, OWASP) | Only name those you really consulted on Friday |

---

## START OF JUSTIFICATION (count from here)

### 1. Malware analysis

I chose Agent Tesla, a commodity infostealer, because it targets what CareLink's clinician devices cache: saved browser, email and FTP credentials. A stolen credential that already works on CareLink systems needs no exploit, so it is more dangerous than most vulnerabilities. I considered a ransomware sample, but an infostealer better matches the likeliest first step into CareLink's systems: credential theft. I recorded the SHA-256 (`699ec052ecc898bdbdafea0027c4ab44c3d01ae011c17745dd2b7fbddaa077f3`) before analysis and ran the sample only in isolated sandboxes, CAPEv2 and Any.run [CONFIRM: describe the isolation].

Static analysis alone was misleading. The triage script, which was pre-written [CONFIRM: say what you changed], found one import (`_CorExeMain`, normal for any .NET program) and rated the file "low suspicion" (Fig 1). An entropy of 6.96 and the sandbox's "encrypted or compressed data" warning showed the real payload was packed (Fig 2). Its "IP" indicators, such as 1.0.0.0, were version strings, so I discarded them as false positives.

Dynamic analysis saw past the packing. The sample started a child copy of itself and triggered process injection signatures (Fig 3). YARA matched the process dumps, not the packed file, with strings such as `GetSavedPasswords` and `GetSavedCookies` (Fig 4): this was the unpacked payload. I observed persistence through the Run key `xws` pointing to `Temp\xws\xws.exe` (Figs 5, 6), a command change under `mscfile`, a technique commonly used to bypass UAC, AMSI enumeration (Fig 7) and a DNS lookup for `checkip.dyndns.org` (Fig 8). I did not observe data leaving the machine. Exfiltration is known family behaviour from published reporting and is labelled "known" in Table 2.

CareLink should use EDR alerts for injection, application control that blocks execution from Temp, alerts on new Run keys, filtering of outbound SMTP, FTP and unusual DNS, and short-lived tokens that can be revoked.

### 2. Threats and intelligence

The key assets are patient records in the cloud care system and the clinician devices that reach them. Entry points are the devices, the sync API and supplier access. Trust boundaries are device to API and API to database. I assumed the care system is delivered as SaaS, so its hosting was out of scope.

I combined sources into an enriched view (Table 1): sandbox telemetry, VirusTotal, MWDB, MalwareBazaar (three platforms agreeing on the hash), and [CONFIRM: NCSC, CISA KEV, MITRE ATT&CK and OWASP, only those you consulted]. I followed the collect, verify, analyse, share lifecycle. Each indicator got a reliability and confidence score. Microsoft, Akamai and Let's Encrypt traffic was allowlisted so legitimate services would not be blocked, and `checkip.dyndns.org` was only medium confidence because it is also a legitimate service. Agent Tesla is commodity malware used by many actors, so attribution to one actor would be unreliable, and one sandbox run does not reproduce CareLink's environment.

Table 3 maps six threats to controls. Two are process threats: helpdesk password resets and supplier access. They matter because employees can enable an attack without realising it, by opening an attachment or resetting an account for a convincing caller. Controls include identity checks with call-backs, time-limited least-privilege supplier access, phishing-resistant MFA, conditional access, full-disk encryption and remote wipe. Human factors drive most of these routes: phishing needs a person to click, so awareness training is a control that supports the technical ones, not a substitute for them.

In my authorised lab I sent 200 invalid bearer tokens to the Ex1 sync API. Every response was 401, with no throttling or lockout (Fig 9). This is a finding: an attacker could keep guessing. The mitigation is rate limiting, lockout and long random tokens. 200 attempts is a small sample, so I do not claim the API is otherwise secure. sqlmap found no injection but received 400 responses 752 times, so the result is inconclusive: validation may have blocked the test rather than proved the code safe.

### 3. Assurance

Assurance is the evidence that lets the risk owner trust a system. "Trusted" means relied upon; "trustworthy" means it deserves that reliance. Testing closes the gap. My strategy uses four approaches. Design and implementation assurance: threat-led design and security tests on the sync API. Intrinsic assurance, from inside CareLink: regular vulnerability scans and configuration reviews, and code review before each release. Extrinsic assurance, from outside: an independent penetration test before go-live and yearly. Its benefits are independence and fresh eyes; its limits are that it is a point-in-time test with limited scope and a cost. Third-party testing gives the risk owner independent evidence. Operational policy and process: change control, incident response and supplier reviews. Supplier assurance matters because CareLink relies on the SaaS provider, so I would ask for independent evidence such as a recent penetration test summary or a certification.

Testing is prioritised by asset criticality (patient records, clinician devices), threat likelihood (phishing, infostealers) and vulnerability severity (missing throttling). Each test has a scope, expected outcome, owner and evidence. Findings are recorded, rated, fixed and retested. I would retest after every release, supplier change or new threat intelligence. An acceptance criterion: after [N] invalid tokens, further attempts are throttled [CONFIRM: match your assurance strategy].

### 4. Legal and ethical

All testing was authorised and scoped in written rules of engagement: the Ex1 sync application, the Ex1 Windows 11 VM and one malware sample. Live websites, other systems and other people's devices were out of scope. The Computer Misuse Act 1990 makes unauthorised access an offence, so scope was a legal boundary, not just a professional one. The lab used no real patient or personal data, in line with UK GDPR and the Data Protection Act 2018. Intelligence came only from open sources, respecting data protection and privacy rights under the Human Rights Act 1998. I worked to the BCS Code of Conduct. Testing was kept proportionate: only the tests needed to answer the brief were run.

Evidence was handled so it could support legal proceedings: SHA-256 recorded before analysis, the original file kept read-only with analysis on a copy, a timestamped activity log recording who did what and when, and the hash re-checked at the end [CONFIRM: only if you did]. Malware ran only in sandboxes. Only the public malware sample was submitted to a third-party service, and no CareLink data was. Escalation was defined: stop, record and report anything affecting an out-of-scope system. [CONFIRM: none occurred.]

## END OF JUSTIFICATION (stop counting here)
