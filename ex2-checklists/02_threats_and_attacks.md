# B. Threats and attacks (time-box: 2.5 hours)

**Brief topic 2:** Discover, identify and analyse threats, attack techniques, vulnerabilities and mitigations.

**Done when:** you have a threat model, scan results, and at least 3 attacks on your own app, each with worked? / impact? / fix?

**First:** the rules of engagement in `04_legal_ethics_evidence.md` must be filled in. Only test your own app on your own machine.

## Intel (30 min)
- [ ] Describe the process in 4 words: collect, check reliability, analyse, share.
- [ ] Combine two or more sources into one **enriched view** (a table: source 1, source 2, meaning for CareLink).
- [ ] Show one intel-to-attack link: a threat you found, then a lab attack that demonstrates it.
- [ ] List sources: NCSC, CISA KEV, MITRE ATT&CK, OWASP, vendor intel.
- [ ] Passive, lawful monitoring only for dark web / social.
- [ ] Pick 3 realistic threats to CareLink. Include both **technical and human factors** (the brief asks for both).

## Assets and attack surface (15 min)
The brief starts here. Write a short table before the threat model.
- [ ] Key assets (cached clinical notes, credentials, the sync API, the DB).
- [ ] Entry points (login, API endpoints, uploads, admin, supplier access).
- [ ] Trust boundaries (device to API, API to database, staff to admin).
- [ ] Attack surface: what an attacker can reach from each entry point.

## Threat model (30 min)
- [ ] Draw the data flow of your Ex1 app (`ex1-design/prototype/`).
- [ ] STRIDE on each part: `templates/stride_threat_model.md`.

## Scan (45 min)
- [ ] nmap on your local test VM.
- [ ] Nessus Essentials (if it activates quickly; otherwise skip and say so).
- [ ] Nikto and dirb.
- [ ] Burp walk-through.
- [ ] Screenshot each. Log them.

## Attack your own app (45 min)
Run the prototype first (`ex1-design/prototype/README.md`). Note: it has not been attacked with Burp or SQLMap yet, so any finding is yours.

| Attack | Worked? | Impact | Fix |
|---|---|---|---|
| SQL injection (sqlmap) | | | |
| Brute force a token (Burp Intruder) | | | |
| IDOR / bad upload | | | |

## Map and validate (20 min)
- [ ] **Map** each threat or attack technique to a control or mitigation, and say in one line how it reduces the risk (ATT&CK ID, STRIDE category).
- [ ] **Validate** at least one vulnerability and one mitigation in your controlled lab, and record before and after evidence.
- [ ] Say how each vulnerability could be exploited in the CareLink scenario, not only in the lab.

## MERIT (item 12): threats to services and processes
- [ ] Threats to processes: helpdesk password resets, supplier access, leavers, staff enabling a phish.

## DISTINCTION (item 12, only if ahead)
- [ ] A mitigation for each of those.

## If stuck
A tool will not install: describe what you would run, show the closest evidence you can, and say plainly what you did not run.
