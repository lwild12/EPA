# Ex2: START HERE

**Due: Friday 13 Nov 2026, 16:00.** Aim to upload by **14:30** so you have a buffer.
Case study: still CareLink.

## NEXT (edit this one line as you go)

> **NEXT: download the M57-Jean image and record its SHA-256** (see `ex2-autopsy/README.md`)

## Rules for a busy brain

1. One task at a time. Set a timer for the time-box.
2. Stuck for 10 minutes? Write your assumption in one line, screenshot, move on.
3. Screenshot as you go. Log it in `ex2-checklists/00_evidence_log.md`.
4. Pass first, extras last. Do not start an extra until every normal item is ticked.
5. Done is better than perfect. Tick the box and stop.

## Plan (assumes two clear working days: adjust if not)

### Tonight (max 1 hour, then stop)
- [ ] Download the M57-Jean image. Record SHA-256.
- [ ] Pick 2-3 candidate malware hashes (`ex2-malware/SAMPLE_OPTIONS.md`).
- [ ] Fill in the rules of engagement (`ex2-checklists/04_legal_ethics_evidence.md`, step 1).

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
| 2:00 | E. Autopsy | `ex2-autopsy/README.md` |
| 1:00 | C. Assurance strategy | `03_assurance.md` |
| 1:30 | D. Legal, ethics and IR plan | `04_legal_ethics_evidence.md` |
| 0:45 | F. Justification (1,000 +/- 100 words) | `05_justification.md` |
| 0:30 | Check against the brief, then **upload** | bottom of this file |

## If you run short of time (in this order)
1. Make sure every topic the brief highlights has something on the page.
2. Finish the justification. Unfinished work with an honest note beats a missing section.
3. Only then add extras (items 9 and 12 below).

## What decides the grade
Your Notion page says items **9 (malware)** and **12 (threats)** decide the grade. Their extras:
- Item 9: obfuscation / anti-VM / anti-debug and how you saw past it. Your own script (be honest about what is yours).
- Item 12: threats to processes (helpdesk resets, supplier access) and a mitigation for each.

Check these against the exact wording in your brief.

## Open questions (answer these early)
- [ ] Which topics are highlighted yellow in your brief? Those are mandatory.
- [ ] Does Any.run's current free tier run your sample (OS, 32/64-bit)? If not, use your own VM sandbox.
- [ ] What does QA say about third-party or pre-written code? (`triage.py` is pre-written.)

## Final check before upload
- [ ] Every highlighted topic has evidence.
- [ ] Every figure is numbered and mentioned in the text.
- [ ] Hashes recorded: malware sample and the M57-Jean image.
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
| Malware steps | `ex2-checklists/01_malware.md`, `ex2-malware/` |
| Sample ideas | `ex2-malware/SAMPLE_OPTIONS.md` |
| Threat model template | `templates/stride_threat_model.md` |
| Assurance template | `templates/assurance_strategy.md` |
| IR plan template | `templates/incident_response_plan.md` |
| UK law quick reference | `templates/uk_legal_reference.md` |
| Writing pattern | `GUIDE.md` (the 5-part paragraph) |
