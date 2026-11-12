# Ex2 Friday (Day 2): full guide

One small step at a time. Do the step, tick it, move on. Do not read ahead.
Today: finish the evidence, write the assurance strategy, write the justification, **upload**. Submission is **final**.

**Rules from the v4 example pack. You confirmed the v4 pack applies, with the v11 brief for what must be attempted.**

- Tests run **09:30 to 16:00**. Active time is 6 hours. Take **one 30-minute break** and **email your supervisor when it starts and when it ends**.
- Open book, but it is an individual test. **No messaging anyone and no AI chat during test hours.** Everything you need is in this guide and your bring-in files.
- Screenshots: **maximum 5 pages of A4**. Crop tightly.
- Upload to **Blackboard**. Submission cannot be reloaded or amended.
- Work you bring in must be work you have adapted and can explain. **Retype in your own words. Do not paste.**

**If you feel stuck (10 minutes is the limit):**

1. Stand up, drink water, look away from the screen.
2. Say aloud: "The next step is ____."
3. Write your assumption in one line. Move on. Come back at the end.

## Bring-in list (check tonight)

- ☐ `Ex2 Tables.docx` (Tables 1 to 3, filled in with your suggestions)
- ☐ `Ex2 Figures` folder (Fig1 to Fig9b, cropped)
- ☐ RoE (retyped, with the three fixes)
- ☐ Justification draft (`ex2_justification_draft.md`), printed
- ☐ Printed v4 rows for Technical Competencies 9, 12, 21, 25
- ☐ This guide and the pocket guide, printed
- ☐ `Ex2_Notes` (your notes) and `sqlmap.txt`

## What each grade needs (v4 tables)

| Item | Pass | Merit | Distinction |
| --- | --- | --- | --- |
| 9 Malware | Analyse malware, identify its mechanisms | Malware with **obfuscation and anti-reverse-engineering** | **Script or compose custom tool sets** |
| 12 Threats | Research with external sources (NCSC, OWASP), **combine sources into an enriched view**, demonstrate an attack in a lab | Evaluate threats to **technology, services and processes** | **Devise mitigations** |
| 21 Assurance | Develop an assurance strategy | none | none |
| 25 Legal and ethics | Organise testing and investigation legally and ethically (English jurisdiction); **secure evidence for legal proceedings** | none | none |

So: protect **Malware** and **Threats** first. Assurance and legal are pass only. Do them properly, but do not gold-plate.

## Schedule

| # | Block | Mins | Clock |
| --- | --- | --- | --- |
| 1 | Start and RoE | 30 | 09:30 to 10:00 |
| 2 | Intel table | 45 | 10:00 to 10:45 |
| 3 | Malware table | 45 | 10:45 to 11:30 |
| 4 | Threat table | 45 | 11:30 to 12:15 |
|   | **Break + 2 emails** | 30 | 12:15 to 12:45 |
| 5 | Lab evidence and screenshots | 30 | 12:45 to 13:15 |
| 6 | Assurance strategy | 35 | 13:15 to 13:50 |
| 7 | Justification | 60 | 13:50 to 14:50 |
| 8 | Final check and upload | 40 | 14:50 to 15:30 |
| 9 | Buffer (no new work) | 30 | 15:30 to 16:00 |

---

## 1. Start and RoE (30 min)

**The RoE is already done (prepared Thursday). Today: fill in the v2 time and check the hash.**
**Done when:** the v2 time is filled in and the hash matches everywhere.

- ☐ Write your real start time on the pocket guide.
- ☐ Make a folder `Ex2_Day2` with `screenshots`, `outputs`, `notes`.
- ☐ Copy in the bring-in files.
- ☐ Open the RoE. Fill in the v2 update time: "v1 authorised 09:30, 12 Nov 2026. v2 updated [today's time]."
- ☐ Work out the sample hash again: `Get-FileHash -Algorithm SHA256 <file>`. Write the time and value in `notes`.
- ☐ Compare it with the RoE. If it does not match: stop, write a note, do not continue with that file.
- ☐ If the sample file is not on this PC, write: "Hash taken from the CAPE report (Fig 2)".
- ☐ Open the v11 brief. Tick off the five yellow topics: malware, threats, assurance, legal and ethics, justification.

## 2. Intel table (45 min)

**Done when:** every row of Table 1 has all 8 columns filled, and you have cited at least 2 external sources.

- ☐ Open Table 1.
- ☐ Do one real lookup per row and paste a short result in **Enrichment**:
  - hash: VirusTotal (family label, detections)
  - domains: WHOIS (owner, creation date)
  - IPs: an ASN lookup (who owns the range)
- ☐ Read one NCSC page and one OWASP page on a topic that fits (phishing, credential theft, API authentication). Write the title, URL and date accessed.
- ☐ Fill **Reliability** using the key: High (seen in CAPE or 2+ sources agree), Medium (seen once, or also legitimate), Low (unreliable tool).
- ☐ Fill **Confidence** and **Action**.
- ☐ Mark Microsoft, Akamai and Let's Encrypt as allowlisted, with the reason.
- ☐ Mark `1.0.0.0` and similar as false positives (version strings).
- ☐ Write 2 sentences on what changed after enrichment. This is your "enhancement" demonstration.

## 3. Malware table (45 min)

**Done when:** Table 2 is filled and the merit paragraph is written.

- ☐ For each row of Table 2, check that the Fig number really shows what you claim.
- ☐ Check every ATT&CK ID against Fig 7. For IDs not in Fig 7 (e.g. T1566), look them up on attack.mitre.org. If you cannot confirm one, delete it.
- ☐ Label each mechanism **Observed** or **Known**. Exfiltration is **Known**, not observed.
- ☐ **MERIT: write 3 lines on how you saw past the packing.** Static analysis showed one import and high entropy. The sandbox showed injection. YARA matched the process dumps (Fig 4).
- ☐ Write 2 lines on why the triage script said "low suspicion" while YARA said Agent Tesla.
- ☐ Write 1 line on what is yours and what is pre-written (the triage script).
- ☐ **DISTINCTION (only if true):** did you script or adapt a tool yourself? If not, skip it. Do not claim it.

## 4. Threat table (45 min)

**Done when:** all 6 rows complete, with a mitigation on each.

- ☐ Check each row has asset, entry point, technique, impact, control.
- ☐ Rows 4 and 5 are your **MERIT** evidence (processes and services): helpdesk reset and supplier access. Write one sentence each on how an employee could enable the attack without realising it.
- ☐ Row 6: mark **Tested? Yes, Figs 9a and 9b**. Every other row says **No** unless you have evidence.
- ☐ Write 3 lines: assets, entry points, trust boundaries (device to API, API to database), and the SaaS assumption.
- ☐ **DISTINCTION:** check every row has a mitigation in the Control column.

## Break (12:15 to 12:45)

- ☐ Email your supervisor: break starting. Write the time: ______
- ☐ Eat. Drink water. Walk. Look at something far away.
- ☐ Email your supervisor: break ended. Write the time: ______

## 5. Lab evidence and screenshots (30 min)

**Done when:** the lab test is written up and screenshots fit in 5 pages of A4.

- ☐ Open Figs 9a and 9b and `sqlmap.txt`.
- ☐ Check the target was the Ex1 sync application only. Write that in the log.
- ☐ Write 4 lines: what you did (200 invalid bearer tokens), the result (all 401, no lockout), the finding (no rate limiting seen), the mitigation (rate limit, lockout, long random tokens).
- ☐ Write: "200 attempts is a small sample." Never write "secure".
- ☐ Write 3 lines on sqlmap: no injection found, but 752 x 400 responses, so the result is **inconclusive**.
- ☐ Paste Figs 1 to 9b into one document and check the page count.
- ☐ If over 5 pages, cut in this order: crop Fig 7 harder, stack 9a and 9b together, merge Figs 5 and 6, drop Fig 8.
- ☐ Give each figure a number and a one-line caption.

## 6. Assurance strategy (35 min)

**Done when:** you have objectives, a test plan table (5 rows or more), and the four approaches.

- ☐ Write what needs assuring: patient records, clinician devices, the sync API.
- ☐ Write 3 security objectives (e.g. patient data stays confidential; only authorised devices and tokens connect; infostealers are detected and contained).
- ☐ Write 3 acceptance criteria that can be measured (e.g. after [N] invalid tokens, attempts are throttled; devices are encrypted; EDR alerts on injection).
- ☐ Make a test plan table with columns: Test, Scope, Expected result, Owner, Evidence, Priority. Add 5 rows or more.
- ☐ Write the priority rule: asset criticality, threat likelihood, vulnerability severity.
- ☐ Name the four approaches: design and implementation, intrinsic, extrinsic, operational policy and process. Give an example of each.
- ☐ Give 2 intrinsic examples, and 1 extrinsic example (e.g. independent penetration test) with its benefits and limits.
- ☐ Write 2 lines: "trusted" versus "trustworthy".
- ☐ Write 2 lines: how third-party testing contributes.
- ☐ Write the findings workflow: record, rate, fix, retest. Write what triggers a retest (release, supplier change, new threat).
- ☐ Stop at 13:50. This is pass only.

## 7. Justification (60 min)

**Done when:** 900 to 1,100 words, retyped in your own words, no `[CONFIRM]` left.

- ☐ Open the draft. Read **section 1** only.
- ☐ Check each claim against your figures and tables. Delete anything that is not true of your work.
- ☐ Retype section 1 in your own words. Resolve each `[CONFIRM]`.
- ☐ Repeat for **section 2**, then **3**, then **4**. (About 12 minutes each.)
- ☐ Section 3 must match the strategy you wrote in block 6.
- ☐ Add one thing you did that the draft missed.
- ☐ Every figure and table must be mentioned by number.
- ☐ Count the words (body only). Target 1,000. If you are under 900, add a sentence on what you did not do or what you would add next. If you are over 1,100, cut the longest sentence in the longest section.

## 8. Final check and upload (40 min)

- ☐ Words: 900 to 1,100.
- ☐ Every Fig and every Table mentioned in the text.
- ☐ Screenshots: 5 pages of A4 or fewer.
- ☐ The hash is the same in the RoE, Table 1 and the justification.
- ☐ No `[CONFIRM]` or `[N]` left.
- ☐ It is clear what is your own work and what is pre-written.
- ☐ No malware sample, no credentials, no real personal data in the upload.
- ☐ File names are clear, in the formats the pack asks for.
- ☐ **Upload to Blackboard.**
- ☐ Check that it shows as submitted. Take a screenshot of the confirmation.

## 9. Buffer (15:30 to 16:00)

- ☐ Do not start new work.
- ☐ If the upload fails, try again, then tell your supervisor straight away. Write down the time.

## If you run short of time

Do these in order:

1. The Malware merit paragraph and the Threat table (merit and distinction live here).
2. The RoE and the hash (pass, legal).
3. A short assurance strategy: objectives, test plan, four approaches.
4. The justification. A short honest one beats a missing one.
5. Everything else.

## Where things are

| Need | File |
| --- | --- |
| Justification draft | `ex2-checklists/ex2_justification_draft.md` |
| Pocket guide (print this) | `ex2-checklists/ex2_friday_pocketjet.pdf` |
| Assurance template | `templates/assurance_strategy.md` |
| UK law quick reference | `templates/uk_legal_reference.md` |
| Writing pattern | `GUIDE.md` |
