# Ex3 detailed steps: Wednesday (D to H)

Adds detail to `ex3_guide.md` sections D to H. Same layout as the Tuesday file: **Do**, **You should see**, **Write**.

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
