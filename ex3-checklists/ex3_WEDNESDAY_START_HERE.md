# Ex3 Wednesday: START HERE (one small step at a time)

Writing day. Open this file and nothing else. Do one box. Tick it. Next box.

**Deadline 16:00. Aim to upload by 15:00.** That leaves a safety gap.

## How to use this file

1. Look at the clock. Find your section in the time table.
2. Set a phone timer for that section's minutes.
3. Do the boxes in order. One at a time.
4. Timer rings? Finish the sentence you are on, then **move on**. You can come back at the end.
5. Do not read ahead.

## If you feel stuck

1. Stand up. Drink water. Look out of a window for 30 seconds.
2. Say out loud: "The next step is ____."
3. Write one rough line. A rough line beats a blank page.
4. Still stuck? Write "TO DO" in the document and go to the next section.

## Rules to remember (check them against your live brief)

- Open book. Individual test. Follow the rules your assessor gave you on AI use.
- If any text was AI-assisted, **reference it** the way your assessor said, and rewrite it in your own words from your own evidence.
- One 30-minute break. **Email your supervisor when it starts and when it ends.**
- Screenshots (if requested): 5 pages of A4 maximum. Crop tightly.
- Submission is final. You cannot change it after.

## Time table (6 hours of work, about 70 minutes spare)

| Clock | Task | Minutes |
| --- | --- | --- |
| 09:30 | Setup | 10 |
| 09:40 | C Monitoring write-up | 35 |
| 10:15 | A6 Big-data weaknesses | 15 |
| 10:30 | B3 to B7 Recon | 20 |
| 10:50 | D Risk model (**only section with Merit and Distinction**) | 75 |
| 12:05 | **Break** (two emails) | 30 |
| 12:35 | E Standard-based assessment | 30 |
| 13:05 | F ISMS plan | 25 |
| 13:30 | G Incident response | 30 |
| 14:00 | H Justification | 40 |
| 14:40 | Upload and check | 10 |

**Running behind? Cut in this order:**

1. C5 to C7: one line each.
2. A6: two weaknesses only.
3. Second Snort fix: say it was not confirmed.
4. **Never cut D.**

---

## 09:30 SETUP (10 min)

- ☐ Open your submission document.
- ☐ Open your folder of screenshots.
- ☐ Open `evidence_log.txt`.
- ☐ Open the live brief. Find: file format, file name rule, upload place.
- ☐ Find which standard the brief wants for risk assessment. Write it down.
- ☐ Make a list: figure number, what it shows, file name.
- ☐ Write straight into the submission document. Not into notes first.

**Done when:** the document is open and the figure list exists.

---

## 09:40 C. MONITORING (35 min)

**C1 Table (5 min)**

- ☐ Make a table with four columns: source, why, normal, suspicious.
- ☐ Add a row for your login log. Put your numbers in "normal" and "suspicious".
- ☐ Add a row for network traffic. Use your baseline and attack numbers.
- ☐ Add a row for IDS alerts (Snort).
- ☐ Add two more rows: endpoint events, application logs.

**C2 Snort (10 min)**

- ☐ Write the Snort version.
- ☐ Write how you adapted the rules (the two network variables).
- ☐ Write any error you hit and how you fixed it. Quote the error text.
- ☐ Write how many alerts each rule gave on the attack capture.
- ☐ Write what fired on the normal capture.
- ☐ Write which rules did not apply and why.
- ☐ Write one tuning change and why. (Idea: one scan gave thousands of alerts, which is alert fatigue.)

**C3 Wireshark (3 min)**

- ☐ Screenshot the filter `tcp.flags.syn==1 && tcp.flags.ack==0`.
- ☐ Screenshot the filter `ftp.response.code==530` (or your service's failure code).
- ☐ Write the "Displayed" count under each.

**C4 Correlation table (10 min)**

- ☐ Make a table: time, source, event, meaning.
- ☐ Add one row per attack phase from the packet data.
- ☐ Add one row for the log (failed logins, successful logins).
- ☐ Add one row for the Snort alerts.
- ☐ Write the cause in 3 sentences.
- ☐ Write the breach decision: did anyone get in? Give the evidence.
- ☐ Write what would change your mind.
- ☐ Add ATT&CK names: Network Service Discovery (T1046), Brute Force (T1110).
- ☐ Write the clock offset between log and capture, if there is one.

**C5 to C7 (7 min)**

- ☐ C5: two benign things that look bad. One line on how to tell them apart.
- ☐ C6: priority table P1, P2, P3 with who responds and how fast.
- ☐ C7: one line on rules versus statistics. Use a real example from your own results.

**Done when:** all of C has some text and a figure number.

---

## 10:15 A6. BIG-DATA WEAKNESSES (15 min)

- ☐ Draw five boxes: capture, parser, storage, analysis, report.
- ☐ Draw a dashed line around the whole thing: trust boundary.
- ☐ Make a table: stage, weakness, which of C/I/A, control. One row per box.
- ☐ Pick the two worst weaknesses.
- ☐ For each, write what an attacker gains.
- ☐ Add one real example from your own data (missing values, a weak statistic).
- ☐ Write one sentence on benefits and costs of big data.

---

## 10:30 B3 to B7. RECON (20 min)

- ☐ **B3:** table: finding, source, status, reliability.
- ☐ Statuses: confirmed, assumed, needs validation.
- ☐ Reliability: A = direct from the system, B = public record that may be old, C = guess.
- ☐ Mark anything a server says about itself as an **assumption**.
- ☐ **B4:** find two sources that differ. Write which you trust and why.
- ☐ **B5:** write three attack paths: entry point, what it enables, how you would validate.
- ☐ **B6:** one line each on port scanning, OSINT, insider.
- ☐ **B7:** write: "All collection was passive and from public sources. Nothing was scanned."

---

## 10:50 D. RISK MODEL (75 min). The only section with Merit and Distinction.

**D1 Assets (8 min)**

- ☐ Table: ID, asset, owner, location, value (H, M, L).
- ☐ Add 5 to 8 assets from your case study.

**D2 Risk register (12 min)**

- ☐ Write the scale: likelihood 1 to 5, impact 1 to 5, score = L x I.
- ☐ Write the bands: 1 to 5 Low, 6 to 12 Medium, 15 to 25 High.
- ☐ Table: ID, risk (threat on asset), L, I, score, rating.
- ☐ Add 5 risks. Use evidence from your lab where you have it.
- ☐ Draw the model: threat, vulnerability, asset, impact, control.
- ☐ Write one sentence of limitation: scores are judgement.

**D3 Method 1: STRIDE (10 min)**

- ☐ Pick one component.
- ☐ Write one line each for Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege.

**D4 Method 2: CVSS (10 min)**

- ☐ Open the FIRST CVSS 3.1 calculator.
- ☐ Pick one known vulnerability.
- ☐ Click the eight metrics.
- ☐ Screenshot the vector and score.
- ☐ Check the score against the NVD entry.

**D5 Compare and contrast (10 min) This is the Merit item.**

- ☐ Table: STRIDE vs CVSS. Rows: output, when used, detail needed, business impact, weakness, strength.
- ☐ Write 3 sentences on how you used both together.

**D6 Options and trades (12 min)**

- ☐ Pick your top 2 risks.
- ☐ For each, write 3 options: technical, procedure, monitoring.
- ☐ Table: option, type, what it reduces, cost, trade-off.
- ☐ Re-score the risk after your chosen option. That is the residual risk.

**D7 Investment options (13 min) This is the Distinction item.**

- ☐ Write the formula: ALE = SLE x ARO.
- ☐ Write your assumed SLE and ARO. Label them **assumed**.
- ☐ Work out the ALE before.
- ☐ Work out the ALE after for two options.
- ☐ Net benefit = benefit minus annual cost.
- ☐ Rank the options. Write which you recommend.
- ☐ Sensitivity: change the ARO by 50 percent. Does the ranking change?
- ☐ Check your arithmetic with a calculator.

**Done when:** D1 to D7 each have a table or text.

---

## 12:05 BREAK (30 min)

- ☐ Email your supervisor: break starts.
- ☐ Leave the desk. Eat. Drink. Walk.
- ☐ Email your supervisor: break ended.

---

## 12:35 E. STANDARD-BASED ASSESSMENT (30 min)

- ☐ Write which standard you used and why (look at the brief's wording).
- ☐ Write one reason you did not use an alternative.
- ☐ Table: stage, where in this document (context, identification, analysis, evaluation, treatment, monitoring, communication).
- ☐ Table: risk, treatment, control from the standard, status, gap.
- ☐ **Check each control number in your own copy of the standard.**
- ☐ Write three limits: scores are subjective, lab not real records, costs assumed.
- ☐ Write one sentence: another analyst could repeat this by following the stage table.

---

## 13:05 F. MANAGEMENT PLAN (25 min)

- ☐ Write context: the organisation, who is affected, scope (5 lines).
- ☐ Table: role, responsibility (board, security lead, IT, analyst, all staff).
- ☐ Table: 4 objectives with a measure, a target (**mark as proposal**), and a review period.
- ☐ Write one line each: risk treatment, access, monitoring, incident management, training, improvement.
- ☐ Write Plan, Do, Check, Act in one line each.
- ☐ Write what triggers a rethink: threat, technology, regulation.

---

## 13:30 G. INCIDENT RESPONSE (30 min)

- ☐ Write 7 phases, one line each: preparation, identification, triage, containment, eradication, recovery, review.
- ☐ Table: role, decision authority.
- ☐ Write severity P1 to P3 and when to call specialists.
- ☐ Table: third party, role, when involved, what is shared (at least three).
- ☐ Write how evidence is shared: copies, hashes, encrypted, named people.
- ☐ Write the notification rule: regulator within 72 hours if a personal data breach risks individuals (UK GDPR Article 33).
- ☐ **Tabletop (10 min):** set a timer. Walk three injects aloud: alert, login succeeds, data leaves.
- ☐ Table: step, decision, gap, fix. Find at least two real gaps.

---

## 14:00 H. JUSTIFICATION (40 min)

- ☐ Open `ex3_justification.md` in this folder.
- ☐ Fill one part at a time. 3 to 5 short sentences each.
- ☐ After each part, add the figure numbers.
- ☐ For each decision write: what you chose, which threat, evidence, one alternative you rejected, what risk remains.
- ☐ Say what is pre-written (the scripts and rules) and what **you** ran or changed.
- ☐ Say what is assumed or not confirmed.
- ☐ Count the words. Target 900 to 1,100.
- ☐ Check every figure number appears in the text.

---

## 14:40 UPLOAD (10 min)

- ☐ Right format. Right file name.
- ☐ All 8 topics covered (see `ex3_brief_checklist.md`).
- ☐ If AI helped, the reference is included.
- ☐ Upload.
- ☐ Open the uploaded file to check it.
- ☐ Done. Stop.

---

## Where the detail is

- Every step in full: `ex3_MASTER_step_by_step_THIS_ONE.md`
- Brief checklist: `ex3_brief_checklist.md`
- Justification skeleton: `ex3_justification.md`
- Blank document: `Ex3_submission_template.docx`
