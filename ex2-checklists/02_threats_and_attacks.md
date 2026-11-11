# B. Threats and attacks (time-box: 2.5 hours)

**Done when:** you have a threat model, scan results, and at least 3 attacks on your own app, each with worked? / impact? / fix?

**First:** the rules of engagement in `04_legal_ethics_evidence.md` must be filled in. Only test your own app on your own machine.

## Intel (30 min)
- [ ] Describe the process in 4 words: collect, check reliability, analyse, share.
- [ ] List sources: NCSC, CISA KEV, MITRE ATT&CK, OWASP, vendor intel.
- [ ] Passive, lawful monitoring only for dark web / social.
- [ ] Pick 3 realistic threats to CareLink (human and technical).

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

## Extras (item 12, only after everything above)
- [ ] Threats to processes: helpdesk password resets, supplier access.
- [ ] A mitigation for each of those.

## If stuck
A tool will not install: describe what you would run, show the closest evidence you can, and say plainly what you did not run.
