# Ex2: START HERE

**Due: Friday 13 Nov 2026, 16:00.** Aim to upload by **14:30** so you have a buffer.
Case study: still CareLink.

## NEXT (edit this one line as you go)

> **NEXT: fill in the rules of engagement** (`ex2-checklists/04_legal_ethics_evidence.md`, step 1)

## Rules for a busy brain

1. One task at a time. Set a timer for the time-box.
2. Stuck for 10 minutes? Write your assumption in one line, screenshot, move on.
3. Screenshot as you go. Log it in `ex2-checklists/00_evidence_log.md`.
4. Pass first, extras last. Do not start an extra until every normal item is ticked.
5. Done is better than perfect. Tick the box and stop.

## The brief (v11, 16 Oct 2026): what Ex2 must contain

Ex2 has **five highlighted topics**. All five are mandatory. Dashed bullets in the brief are prompts, not extra requirements.

| # | Highlighted topic in the brief | Your file |
|---|---|---|
| 1 | Analyse malware and identify its mechanisms | `ex2-checklists/01_malware.md` |
| 2 | Discover, identify and analyse threats, attack techniques, vulnerabilities and mitigations | `ex2-checklists/02_threats_and_attacks.md` |
| 3 | Develop an assurance strategy | `ex2-checklists/03_assurance.md` |
| 4 | Organise testing and investigation work in accordance with legal and ethical requirements | `ex2-checklists/04_legal_ethics_evidence.md` |
| 5 | Produce a written justification (1,000 +/- 100 words) | `ex2-checklists/05_justification.md` |

**Not in the v11 Ex2 brief:** an Autopsy forensics task and an incident response plan. Incident response is in **Ex3** ("Manage intrusion response"). Autopsy is now an optional extra: it is useful evidence for topic 4 (evidence handling) but nothing in the brief asks for it. Do it only after all five topics are done.

The brief also says to use the **supplementary tables** to check you have the pass, merit and distinction evidence. Open those next to this file.

## Plan (assumes two clear working days: adjust if not)

### Tonight (max 1 hour, then stop)
- [ ] Fill in the rules of engagement (`ex2-checklists/04_legal_ethics_evidence.md`, step 1). Scope and authorisation come before any testing.
- [ ] Pick 2-3 candidate malware hashes (`ex2-malware/SAMPLE_OPTIONS.md`).

### Thursday (Day 1, about 6 hours)
| Time-box | Do | File |
|---|---|---|
| 0:30 | Read the brief, plan | this file |
| 2:00 | A. Malware | `01_malware.md` |
| 2:30 | B. Threats and attacks | `02_threats_and_attacks.md` |
| 1:00 | Tidy notes and evidence log | `00_evidence_log.md` |

### Friday (Day 2, about 6 hours, start about 08:30)
| Time-box | Do | File |
|---|---|---|
| 1:30 | C. Assurance strategy | `03_assurance.md` |
| 2:00 | D. Legal, ethics, safe testing and evidence handling | `04_legal_ethics_evidence.md` |
| 1:00 | F. Justification (1,000 +/- 100 words) | `05_justification.md` |
| 0:30 | Check against the brief, then **upload** | bottom of this file |
| spare | Optional extras: Autopsy (`ex2-autopsy/README.md`), Merit/Distinction items | see below |

## If you run short of time (in this order)
1. Make sure every topic the brief highlights has something on the page.
2. Finish the justification. Unfinished work with an honest note beats a missing section.
3. Only then add extras (items 9 and 12 below, then Autopsy).

## What decides the grade (from the older v4 example pack: check the live brief's supplementary tables)
Merit = every pass criterion, plus Merit on items 9 and 12 (and others in Ex1 and Ex3).
- **Item 9 (malware).** Pass: identify mechanisms. **Merit: obfuscation and anti-reverse-engineering.** Distinction: script or compose custom tool sets.
- **Item 12 (threats).** Pass: lab attacks, combine sources. **Merit: threats to services and processes too.** Distinction: mitigations for those.

So these are not optional extras if you want Merit.

## Rules from the v4 pack (check the live brief)
- 09:30 to 16:00, 6 hours active, one 30-minute break. **Email your supervisor at break start and end.**
- Screenshots: **max 5 pages of A4**. Crop.
- **No personal communication or asynchronous online interaction. Individual test.**
- Each day's submission is **final**.
- Autopsy and the IR plan were in the older v4 pack. The v11 brief has neither in Ex2 (IR is in Ex3). They are optional extras here.

## Open questions (answer these early)
- [x] Which topics are highlighted yellow? Answered by the v11 brief: the five in the table above. Re-check your live copy matches.
- [ ] Does Any.run's current free tier run your sample (OS, 32/64-bit)? If not, use your own VM sandbox.
- [ ] What does QA say about third-party or pre-written code? (`triage.py` is pre-written.)

## Final check before upload
- [ ] Every highlighted topic has evidence.
- [ ] Every figure is numbered and mentioned in the text.
- [ ] Hashes recorded: malware sample (and the M57-Jean image, if you did Autopsy).
- [ ] Sources cited (tools, public write-ups, repos).
- [ ] Own work and adapted work clearly separated.
- [ ] Justification is 900 to 1,100 words (`wc -w`).
- [ ] No sample, no real personal data, no credentials in what you upload.
- [ ] Upload, then confirm it shows as submitted.

## Where things are
| Need | File |
|---|---|
| **Thursday full guide (print this)** | `ex2-checklists/ex2_thursday_guide_pocketjet.pdf` (source: `ex2_thursday_guide.md`) |
| **Thursday fill-in sheets (print this)** | `ex2-checklists/ex2_thursday_tracker_pocketjet.pdf` (source: `ex2_thursday_tracker.md`) |
| **Friday pocket guide (print this)** | `ex2-checklists/ex2_friday_pocketjet.pdf` (source: `ex2_friday_pocketjet.md`) |
| **Friday full guide (read tonight)** | `ex2-checklists/ex2_friday_guide.md` |
| **Justification draft (check, adapt, retype)** | `ex2-checklists/ex2_justification_draft.md` |
| Malware steps | `ex2-checklists/01_malware.md`, `ex2-malware/` |
| Sample ideas | `ex2-malware/SAMPLE_OPTIONS.md` |
| Threat model template | `templates/stride_threat_model.md` |
| Assurance template | `templates/assurance_strategy.md` |
| IR plan template | `templates/incident_response_plan.md` |
| UK law quick reference | `templates/uk_legal_reference.md` |
| Writing pattern | `GUIDE.md` (the 5-part paragraph) |
