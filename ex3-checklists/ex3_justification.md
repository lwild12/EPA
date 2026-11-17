# Ex3 justification (time-box: 45 min). Target 1,000 words (900 to 1,100)

**Brief topic:** Produce a written justification for the approach taken (1,000 +/- 100 words). One document for the whole of Ex3.

Write this LAST, from your evidence log. Fill each part in 3 to 5 short sentences. Delete the prompts when you are done. Use your real results only.

| Part | Words | Say |
| --- | --- | --- |
| 1. Context and scope | 100 | <company>, what you monitored, rules of engagement, authorisation |
| 2. Data and statistics | 150 | Data sets, baseline, methods, findings, big-data weaknesses |
| 3. Reconnaissance | 100 | Scope, public sources, confirmed vs assumed, attack paths |
| 4. Risk model and external standard | 200 | Register, the **two methods compared**, investment options, the standard chosen, gaps |
| 5. Management system | 120 | ISMS approach, objectives, measures, review |
| 6. Monitoring and detection | 150 | Data sources, rules, correlation, alert handling |
| 7. Incident response | 130 | Phases, roles, third parties, notification, exercise result |
| 8. Limits and next steps | 50 | What you did not do, what you would add |
| **Total** | **1,000** | |

## Draft prompts

**1. Context and scope.** "For <company>, I monitored [what] in a lab made of [Kali, Metasploitable, my own capture]. I worked only on systems I own, under the rules of engagement in [fig]. I chose [approach] because [requirement]."

**2. Data and statistics.** "I used [CIC-IDS2017, day, source, cited] for scale and my own capture for packet detail (fig). The baseline was [BENIGN flows / normal window]. [Method] flagged [source] at [number] standard deviations (fig). The busiest host was the server, which is expected, so I excluded it and said why. Data quality: [number] missing or infinite values, handled by [method]. Big-data weaknesses I judged most serious: [two], because they would let an attacker [blind or poison] monitoring (fig)."

**3. Reconnaissance.** "I scoped recon to [domain], passive sources only. I found [confirmed item] (confirmed) and [assumption] (needs validation). This suggests [attack path] (fig). I rejected [active scanning] because it was not authorised."

**4. Risk model and external standard.** "I scored [N] risks on a [1-5] scale (fig). The top risk is [R1] scored [x]. I used STRIDE and CVSS and compared them: [STRIDE added risk X to the register; CVSS moved risk Y up or down] (fig). I compared [option A] and [option B] and ranked [A] first as an investment because [evidence, cost and value for money]. I assessed to [ISO/IEC 27005 or NIST SP 800-30] because [reason] and rejected [other] because [reason]. Gaps: [control gap]. Residual risk: [what remains]."

**5. Management system.** "I based the plan on ISO/IEC 27001 plan, do, check, act. Objectives include [measure and target, marked as proposals]. They are reviewed [how often] and changes in [threat, technology, regulation] trigger reassessment (fig)."

**6. Monitoring and detection.** "I monitored [sources]. Normal was [baseline]. My detections were [Snort rules, SQL thresholds]. [Rule] fired on [event] (fig). I tuned [rule] by [change] because [reason]. Correlating [three sources] showed [recon then credential attack] (fig). Alerts are [prioritised, recorded, escalated, reviewed]."

**7. Incident response.** "The plan follows [phases]. An incident lead decides [authority]. I would involve [third parties] when [criteria]. Evidence is shared as [copies, hashes, encrypted]. A personal data breach is reported to the regulator within 72 hours where required. My tabletop exercise found [gaps], so I would [improvement] (fig)."

**8. Limits and next steps.** "I did not [run Snort on live traffic / use a SIEM / test the real <company> network]. With more time I would [add]."

## The 5-part pattern for each decision

1. What you chose. 2. Which threat or requirement. 3. Evidence (figure number). 4. One alternative you rejected. 5. Remaining risk.

## Be honest about

- What is pre-written or adapted: `pcap_to_sqlite.py`, `analysis.py`, `queries.sql`, `local.rules`, the templates. Say what **you** changed or ran.
- Anything you could not run, and anything synthetic.
- Which numbers are your results and which are assumptions or proposals.

## Check

- Word count: `wc -w justification.md` (or Word's count). Target 900 to 1,100.
- Every figure number appears in the text.
- Every topic in `ex3_brief_checklist.md` is covered.
