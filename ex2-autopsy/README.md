# Ex2: Autopsy evidence (M57-Jean)

QA does not supply evidence, so you source your own. M57-Jean is the chosen public scenario.

- Scenario: https://digitalcorpora.org/corpora/scenarios/m57-jean/
- Other public disk images: https://digitalcorpora.org/corpora/disk-images/
- Background write-up (read AFTER your own analysis, and cite it if used):
  https://infosecinstitute.com/resources/digital-forensics/forensics-investigation-document-exfiltration-involving-spear-phishing-m57-jean-case/

## Why it fits CareLink

The scenario is a confidential document leaving a company after a spear-phishing attack. That maps to the CareLink threat of confidential data leaving staff devices, and gives you an email trace (the PST / "trace the email" checklist item).

## Check before you download (not verified)

- Exact files, formats and sizes on the scenario page. Make sure you have the disk space.
- The data is synthetic, but still record where it came from and the licence/terms.

## Steps (maps to the legal/ethical topic)

1. Download. Record SHA-256 of every file BEFORE opening anything.
2. Keep the original read-only. Work on a copy. Note the date, time, who and why (chain of custody).
3. Autopsy: create case, add data source, verify hash.
4. Run ingest modules: hash, keywords, file type, web, recent activity, email.
5. Build a timeline. Tag key items. Trace the email.
6. Generate the report. Keep the activity log in order: this is your auditable record.

## Own work

Public write-ups of this case exist. Do the analysis yourself, say which sources you used, and do not copy their findings.
