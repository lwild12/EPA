# Ex2 Friday: full walkthrough

One small step at a time. Do the step, tick it, move on. Do not read ahead.
Today: finish the evidence, write the assurance strategy, write the justification, **upload**. Submission is **final**.

**If you feel stuck (10 minutes is the limit):**

1. Stand up, drink water, look away from the screen.
2. Say aloud: "The next step is ____."
3. Write your assumption in one line. Move on. Come back at the end.

## 0. The facts (read once, 2 minutes)

- Test runs **09:30 to 16:00**. Break **12:30 to 13:00**. No break emails and no time logging.
- Upload to **Blackboard**. Submission cannot be reloaded or amended.
- Screenshots: **maximum 5 pages of A4**. Crop tightly.
- Open book, but it is an individual test (v4 pack). Do not message anyone during test hours.
- What you must attempt: the **five yellow topics in the v11 brief** (malware, threats, assurance, legal and ethics, justification).
- How it is marked: the **v4 tables**.

| Topic (v4 item) | Pass | Merit | Distinction |
| --- | --- | --- | --- |
| Malware (9) | Analyse malware, identify its mechanisms | Malware with **obfuscation and anti-reverse-engineering** | **Script or compose custom tool sets** |
| Threats (12) | Research with external sources (NCSC, OWASP), **combine sources into an enriched view**, demonstrate an attack in a lab | Evaluate threats to **technology, services and processes** | **Devise mitigations** |
| Assurance (21) | Develop an assurance strategy | none | none |
| Legal and ethics (25) | Organise testing and investigation legally and ethically (English law); **secure evidence** | none | none |

**So:** protect **Malware** and **Threats** first. Assurance and legal are pass only. Do them properly. Do not gold-plate.

## 1. What is in this folder

| File | What it is |
| --- | --- |
| `README.md` | This walkthrough |
| `pocket_guide.pdf` | The 8-page PocketJet tick-list (print this). Source: `pocket_guide.md` |
| `justification_draft.md` | The ~1,000-word draft. Check it, adapt it, retype it |
| `templates/tables.md` | Tables 1 to 3, scoring key, merit and boundary skeletons |
| `templates/ex2_tables.docx` | The same three tables as a Word file |
| `templates/assurance_strategy.md` | Assurance strategy template (pass only) |
| `templates/lab_test_writeup.md` | Write-up of the token test and sqlmap |
| `templates/evidence_log_and_captions.md` | Figure captions, page budget, activity log |
| `templates/lookup_cheatsheet.md` | How to do each lookup, hash command, word count |

## 2. Before 09:30 (2 minutes)

- ☐ Open: your tables, the `Ex2 Figures` folder, your RoE, the justification draft.
- ☐ Have the printed pocket guide and the printed v4 rows in front of you.
- ☐ Open `templates/lookup_cheatsheet.md`. You will use it in block 1.

## 3. Schedule

| # | Block | Mins | Clock |
| --- | --- | --- | --- |
| 1 | Intel table | 60 | 09:30 to 10:30 |
| 2 | Malware table | 60 | 10:30 to 11:30 |
| 3 | Threat table | 60 | 11:30 to 12:30 |
|   | **Break** | 30 | 12:30 to 13:00 |
| 4 | Lab evidence and screenshots | 30 | 13:00 to 13:30 |
| 5 | Assurance strategy | 35 | 13:30 to 14:05 |
| 6 | Justification | 60 | 14:05 to 15:05 |
| 7 | Final check and upload | 40 | 15:05 to 15:45 |
| 8 | Buffer (no new work) | 15 | 15:45 to 16:00 |

The buffer is short. **Aim to be uploading by 15:30.**

---

## Block 1: Intel table (09:30 to 10:30)

**Criterion:** Threats, pass. "Combine different sources to create an enriched view" and use external sources.
**Open:** Table 1 (`templates/tables.md` or your docx) and `templates/lookup_cheatsheet.md`.
**Output:** Table 1 with all 8 columns filled, 2 external sources cited, 2 lines on "what changed".

1. ☐ **(5 min)** Read the 7 rows of Table 1. Check the full hash is in row 1.
2. ☐ **(25 min) One real lookup per row.** Paste a short result into **Enrichment**:
   - ☐ Hash: VirusTotal. Note detections, family label, first seen.
   - ☐ `checkip.dyndns.org`: WHOIS. Note owner or registrar and creation date. Say what it is for.
   - ☐ `lencr.org`: say it is Let's Encrypt certificate infrastructure (use the CNAME in your DNS screenshot).
   - ☐ Microsoft and Akamai hosts: an ASN or owner lookup on one or two IPs. Use the `azureedge.net` and `akamaiedge.net` CNAMEs as support.
   - ☐ `Run\xws` and `Temp\xws\xws.exe`: no lookup. Write "host artefact from CAPE (Figs 5, 6)".
   - ☐ `1.0.0.0` etc.: no lookup. Write "version strings, not network traffic".
3. ☐ **(15 min) Two external sources.**
   - ☐ One **NCSC** page you really read (for example on phishing or device security). Write title, URL, date accessed, one sentence on what it told you.
   - ☐ One **OWASP** page you really read (the API Security Top 10 fits your token test). Same four details.
4. ☐ **(10 min) Score each row.** Reliability, Confidence and Action, using the key under Table 1. Mark Microsoft, Akamai and Let's Encrypt as **allowlisted** with the reason. Mark `1.0.0.0` etc. as **false positives**.
5. ☐ **(5 min) Write 2 lines: "what changed after enrichment".** For example: "7 indicators became 3 actionable ones; 4 were allowlisted or discarded."
6. ☐ Add a line to the activity log.

**Done when:** every row has 8 columns, 2 external sources cited, the 2 lines written.

---

## Block 2: Malware table (10:30 to 11:30)

**Criterion:** Malware, pass and **merit** (obfuscation). Distinction only if you scripted something yourself.
**Open:** Table 2 and your figures.
**Output:** Table 2 checked, merit paragraph, two extra lines.

1. ☐ **(10 min) Check every row against a figure.** Open the Fig named in each row. Does it really show what the row says? Change the row if not.
2. ☐ **(10 min) Check ATT&CK IDs.**
   - ☐ Compare each ID with Fig 7.
   - ☐ For IDs not in Fig 7 (for example T1566), look them up on attack.mitre.org.
   - ☐ Delete any ID you cannot confirm.
3. ☐ **(10 min) Label each row Observed or Known.** Exfiltration is **Known, not observed**. Access (phishing) is **Known**.
4. ☐ **(15 min) MERIT: "how I saw past the packing".** Use the 3-line skeleton in `templates/tables.md`:
   - ☐ Line 1: static (Figs 1, 2): one import (normal for .NET), entropy 6.96, "compressed data" warning.
   - ☐ Line 2: sandbox (Fig 3): child process, injection signatures.
   - ☐ Line 3: YARA on the process dumps (Fig 4): `GetSavedPasswords`, `GetSavedCookies`. This is the unpacked payload.
5. ☐ **(5 min)** Write 2 lines: why the triage script said "low suspicion" but YARA said Agent Tesla.
6. ☐ **(5 min)** Write 1 line: what is yours and what is pre-written (the triage script).
7. ☐ **(5 min) DISTINCTION, only if true.** Did you script or adapt a tool yourself? If not, skip. Do not claim it.
8. ☐ Add a line to the activity log.

**Done when:** all 5 rows checked, merit paragraph written.

---

## Block 3: Threat table (11:30 to 12:30)

**Criterion:** Threats, pass, **merit** (services and processes) and **distinction** (mitigations).
**Open:** Table 3 and `templates/tables.md` (boundaries and merit skeletons).
**Output:** 6 complete rows, a boundaries paragraph, two merit sentences.

1. ☐ **(10 min)** Read each row. Does each have asset, entry point, technique, impact and control? Fill any gaps.
2. ☐ **(15 min) MERIT: the two process threats.**
   - ☐ Row 4 (helpdesk reset): one sentence on how an employee could enable the attack without realising it, and the control.
   - ☐ Row 5 (supplier access): same.
   - Skeleton: "An employee could enable this by ____. The control is ____."
3. ☐ **(10 min)** Write the 3 lines: assets, entry points, trust boundaries (device to API; API to database), and the SaaS assumption.
4. ☐ **(10 min) DISTINCTION:** check every row has at least one mitigation in the Control column, and that each mitigation answers its threat.
5. ☐ **(10 min) Be honest in "Tested?"**
   - ☐ Row 6 (API tokens): **Yes**, Figs 9a, 9b.
   - ☐ Row 1: technique yes (sandbox), controls no.
   - ☐ Every other row: **No**.
6. ☐ **(5 min)** Link back to Table 1: one sentence on which indicators feed which threat.
7. ☐ Add a line to the activity log.

**Done when:** 6 rows complete, merit sentences written, mitigations present.

---

## Break (12:30 to 13:00)

- ☐ Eat. Drink water. Walk. Look at something far away. No screens if you can.

---

## Block 4: Lab evidence and screenshots (13:00 to 13:30)

**Criterion:** Threats, pass ("demonstrate attack techniques in a lab"). Also legal ("auditable record").
**Open:** `templates/lab_test_writeup.md` and `templates/evidence_log_and_captions.md`.
**Output:** lab write-up, figures with captions inside 5 pages of A4.

1. ☐ **(5 min)** Open Figs 9a, 9b and `sqlmap.txt`. Check the numbers: 200 requests all 401; 752 x 400.
2. ☐ **(10 min) Write the token test** with the template: aim, target (Ex1 sync app only), method, result, finding, mitigation, limit.
   - ☐ Write "200 attempts is a small sample". Never write "secure".
3. ☐ **(5 min) Write the sqlmap lines.** No injection found, 752 x 400 responses, so **inconclusive**.
4. ☐ **(8 min) Build the figure page.**
   - ☐ Paste Figs 1 to 9b into one document.
   - ☐ Give each a number and a one-line caption (suggestions in the evidence file).
   - ☐ Check the page count. It must be 5 or fewer.
   - ☐ If over, cut in this order: crop Fig 7 harder; stack 9a and 9b; merge Figs 5 and 6; drop Fig 8.
5. ☐ **(2 min)** Add a line to the activity log.

**Done when:** lab write-up done, figures captioned, 5 pages or fewer.

---

## Block 5: Assurance strategy (13:30 to 14:05)

**Criterion:** Assurance, **pass only**. Stop on time.
**Open:** `templates/assurance_strategy.md`.
**Output:** a short strategy: objectives, acceptance criteria, four approaches, test plan, findings workflow.

1. ☐ **(3 min)** Write what needs assuring.
2. ☐ **(4 min)** Write 3 security objectives.
3. ☐ **(5 min)** Write 3 measurable acceptance criteria.
4. ☐ **(2 min)** Write "trusted" versus "trustworthy" in 2 lines.
5. ☐ **(7 min)** Fill the four approaches. Give **2 intrinsic** examples and **1 extrinsic** example with its benefits and limits.
6. ☐ **(2 min)** Write how third-party testing contributes.
7. ☐ **(8 min)** Fill the test plan table. 5 rows or more.
8. ☐ **(1 min)** Write the priority rule: asset criticality, threat likelihood, vulnerability severity.
9. ☐ **(3 min)** Write the findings workflow (record, rate, fix, retest) and the retest triggers (release, supplier change, new threat).
10. ☐ Stop at 14:05. Add a line to the activity log.

**Done when:** all of the above exist. It does not need to be perfect.

---

## Block 6: Justification (14:05 to 15:05)

**Criterion:** the written justification (900 to 1,100 words). It also carries your knowledge evidence for all four topics.
**Open:** `justification_draft.md` (printed or on screen) and a new blank document.
**Output:** the final justification, **retyped in your own words**.

For each of the four sections, do this loop (about 12 minutes each):

1. ☐ Read the section once.
2. ☐ Check each claim against your figures and tables. Delete anything that is not true of your work.
3. ☐ Resolve each `[CONFIRM: ...]`.
4. ☐ Close the draft. Write the section from your own understanding, using the figure numbers.
5. ☐ Compare. Add anything important you missed.

Then:

6. ☐ Section 3 (assurance) must match the strategy you wrote in block 5.
7. ☐ Add one thing you did that the draft missed.
8. ☐ Every figure and table must be mentioned by number.
9. ☐ Count the words (body only; see `templates/lookup_cheatsheet.md`). Target 1,000.
   - Under 900: add a sentence on what you did not do, or what you would add next.
   - Over 1,100: cut the longest sentence in the longest section.

**Done when:** 900 to 1,100 words, no `[CONFIRM]` or `[N]` left.

---

## Block 7: Final check and upload (15:05 to 15:45)

1. ☐ Words 900 to 1,100.
2. ☐ Every figure and every table is mentioned in the text.
3. ☐ Screenshots are 5 pages of A4 or fewer.
4. ☐ The hash is the same in Table 1 and the justification.
5. ☐ No `[CONFIRM]` or `[N]` left anywhere.
6. ☐ It is clear what is your own work and what is pre-written.
7. ☐ The RoE, tables, figures and justification are all in the upload.
8. ☐ No malware sample, credentials or real personal data in the upload.
9. ☐ File names are clear and in the formats the pack asks for.
10. ☐ **Upload to Blackboard.**
11. ☐ Check it shows as submitted. Take a screenshot of the confirmation.

If the upload fails, try again, then tell your supervisor straight away.

## Block 8: Buffer (15:45 to 16:00)

Do not start new work.

## If you run short of time

Do these in order:

1. The Malware merit paragraph and the Threat table (merit and distinction live here).
2. The hash and an evidence-handling paragraph (pass, legal).
3. A short assurance strategy: objectives, test plan, four approaches.
4. The justification. A short honest one beats a missing one.
5. Everything else.
