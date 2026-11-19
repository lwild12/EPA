# Ex4 justification: DRAFT for you to check, adapt and retype

**This is a draft, not a finished answer.** Prepared before the test, with AI assistance. Do not paste it. Read each claim, check it against your own log and screenshots, and retype it in your own words.

How to use it (F9, 90 minutes):

1. Fix every `[CONFIRM: ...]` and `[CHOOSE: ...]`. Each one is something only your own work or live brief can settle.
2. Cross out any sentence that is not true of your work. Add what you did that the draft missed.
3. Keep every number matching your own run (timings, test counts, fuzz results).
4. Copy the text between START and END into a blank Word file and use its word count. It must be 900 to 1,100.
5. Honesty rule: say what is starter code and what you did yourself.

## Fix these in your log before you write (small steps)

- [ ] **Memory.** The algorithm keeps the valid alerts in a list, so memory grows with the input. Only the working memory is fixed. Write: "working memory beyond the input is fixed (open-group cap plus the best-100 heap)". Do not write that total memory is fixed.
- [ ] **Timing.** If 100 times more alerts took less than 100 times longer, the growth is near-linear and far below n squared (10,000 times). An n log n curve would predict slightly more than 100 times. Write "near-linear, nowhere near n squared". Do not write "matches n log n".
- [ ] **Flood test.** The flood test asks for the top 50 (`top_n=50`) while the default is 100. Say so in one line, so "50" does not look like a mistake.
- [ ] **Flood limitation.** Closing the oldest group at the cap protects memory, but a flood can force a real incident to close early and split into two. Say this as the limitation.
- [ ] **Criticality values.** Check the numbers in your log match `CRITICALITY` in `alert_triage.py`.
- [ ] **Provenance.** The defects were reproduced by removing the fixes from starter code. Do not write that you "found" them by initial testing or "wrote" the code. Write the order you actually followed (for example: all fixes removed together, then restored one at a time with a retest after each).
- [ ] **Typos in the log.** Check field names (`created_at`), "deeply", and each test name.

## Claims to check before you rely on them

| Claim in the draft | Where to check |
| --- | --- |
| Script A: 31 starter tests plus [your own] pass. Script B: 16 plus [your own] pass. Command-line script: 6 | Screenshots A1, B1, A9 and your own-test screenshots |
| With all fixes removed, 4 tests failed; restoring them one at a time, with a retest each time, ended with all passing | Your screenshots of each run |
| Bandit: no issues | Screenshot A6 |
| Fuzzer: 20,000 requests, 0 failures; fails with the D2 fix removed | Screenshots A7, A8 |
| Also ran 1,000,000 fuzz requests | Only if you really did; otherwise delete |
| Timings and the growth ratio | Screenshot B2, your own numbers |
| Flood test: 20,000 unique alerts, under 60 MB | `test_alert_triage.py`, B1 |
| MIPS prediction (65536 changed to 1000) matched | Your log, screenshot C1 |
| Syntax tree and bytecode | Screenshot C2; wording varies by Python version |
| Compiler and interpreter features (F5) | Screenshot P2, only what you ran |
| Methodology chosen, system description, lifecycle | Your F7 log |

---

## START OF JUSTIFICATION (count from here)

### 1. Why these components

The case study lists weak API authentication, insecure sync, cached records and alert fatigue as risks. Staff devices send visit notes to a cloud API, so I chose a strict input boundary in front of that API (Script A) and an algorithm that reduces alert noise so real incidents are seen (Script B). I used Python because it is portable, quick to test and easy for a small team to maintain. It is slower than compiled languages, which is acceptable because both scripts are input-bound. I added a MIPS assembler version of the body-size check, to show the same rule at machine level.

### 2. Script A and the three language levels

Script A rejects everything not explicitly allowed. Its specification, recorded in my log before I ran the tests, limits IDs to 64 safe characters, notes to 20,000 characters, dates to at most 30 days old and 5 minutes ahead, and the body to 64 KB; extra fields and duplicate keys are rejected. The starter code was prepared with AI assistance. I ran its 31 tests (normal, boundary, error and security), reviewed each one and added [CONFIRM: three] of my own.

I then used a short command-line script, which returns exit code 0, 1 or 2, so the check can run in automation. The same size rule exists at three levels: Python source, Python bytecode, and MIPS assembler. In Python, `0 < n <= 65536` is one comparison node with two operators, compiled to two compares and jumps. In MIPS it is a function that rejects by default: one branch rejects zero or negative values and another rejects values over the limit. I predicted that lowering the limit to 1000 would change the result from Accept, Reject, Reject to Reject, Reject, Reject, and the run matched [CONFIRM].

### 3. Secure programming

I reproduced three subtle defects by removing their fixes from the starter code and watching the tests fail. A trailing newline in an ID passed because `$` matches before a final newline (CWE-20), which could split log lines. A lone surrogate in a note is valid JSON but cannot be stored as UTF-8, so storing it would crash (CWE-176). Deeply nested JSON fits inside the size limit but exhausts the parser (CWE-674); two tests caught that, so four failed in total. I restored the fixes one at a time, retesting after each, until every test passed.

Bandit found no issues. A fuzzer sent 20,000 mutated requests and checks two rules: the validator only returns a result or raises its error, and anything accepted is safe. With the UTF-8 fix removed, it reported failures; with the fix restored, it reported none. I applied allow-listing, fail-closed handling, resource limits and errors that never echo input, drawing on OWASP and CERT guidance. Together these form a validation gateway: one function every request passes through, returning a clean new dictionary and never the raw input, so a bad device cannot reach the database. As a formal method I described CSP: it proves properties over every behaviour of a model, but it proves the model and not the code. [CONFIRM: add one compiler or interpreter feature you ran in F5.]

### 4. Script B and the algorithm

Alert fatigue could bury real incidents, so Script B groups duplicate alerts and ranks the rest. Inputs are source, type, asset, severity and time; the output is the top 100 incidents and a count of rejected alerts. Alerts with the same source, type and asset within ten minutes of a group's first alert form one group. The score is severity multiplied by asset criticality multiplied by log(count + 1) (criticality: care records 5, sync-api 4, laptop 3, mobile 2, anything else 1). I assumed timestamps are trusted. Its 16 starter tests and [CONFIRM: two] of my own pass, including a flood of 20,000 unique alerts under 60 MB.

I compared two approaches. Comparing every pair of alerts is O(n squared), so an attacker could slow detection by flooding. A dictionary keyed by group gives one lookup per alert, but unique alerts could use up memory, so the oldest open group is closed at a cap and a heap keeps only the best incidents. Sorting dominates at O(n log n). Working memory beyond the input is fixed. My timings were [CONFIRM: 0.002, 0.014 and 0.138 seconds for 1,000, 10,000 and 100,000 alerts]: 100 times more alerts took about [CONFIRM: 69] times longer, near-linear and nowhere near n squared. The same-key relation is an equivalence relation, so it partitions the alerts. After processing k alerts, each valid alert is in exactly one group. The limitation is that a flood can force an early close and split a real incident; a rolling window would help.

### 5. Methodology and lifecycle

For the proposed solution I choose [CHOOSE: agile with security gates, or a V-model]. The case study has [CONFIRM: your reasons from F7, for example staged rollout and changing requirements], so [CHOOSE: reason]. A sequential model offers clear stages and a full audit trail but gives late feedback; an agile model gives early feedback but can skip security tasks under pressure unless they are in the definition of done. Security appears at every stage: abuse cases at requirements, trust boundaries and threat modelling at design, review and tests at build, and monitoring with Script B once deployed.

### 6. Limits, next steps and AI use

These are prototypes. I did not test real network attacks, real data or integration with the live API, and controls outside the code are not covered. Next steps are a rolling window for alert groups, an integration test against the live API, a process to keep the criticality table current, and more checks as new attacks appear. Every change would re-run all the tests.

AI assistance (Claude) was used before the test to prepare starter code and an outline. During the test I ran, tested, debugged and reviewed the code, and wrote this text from my own evidence.

## END OF JUSTIFICATION
