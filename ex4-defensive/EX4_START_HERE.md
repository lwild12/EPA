# Ex4: START HERE (Thursday and Friday, one small step at a time)

Open this file and nothing else. Do one box. Tick it. Next box.

**Deadline: Friday 16:00. Aim to upload by 14:45.** That leaves a safety gap.

## How to use this file

1. Look at the clock. Find your section in the time table.
2. Set a phone timer for that section's minutes.
3. Do the boxes in order. One at a time.
4. Timer rings? Finish the sentence you are on, then **move on**. Come back at the end if there is time.
5. Do not read ahead.

## If you feel stuck (10 minutes is the limit)

1. Stand up. Drink water. Look out of a window for 30 seconds.
2. Say out loud: "The next step is ____."
3. Write one rough line. A rough line beats a blank page.
4. Still stuck? Write "TO DO" and go to the next box.

## Rules to remember (check them against your live brief)

- Open book. Individual test. Follow the rules your assessor gave you on AI use.
- Starter code in this folder was drafted with AI. **Reference that** the way your assessor said. You run it, test it, debug it, review it, and write the justification in **your own words from your own evidence**.
- Screenshots: crop tightly. Check the page limit in your live brief.
- Break rules differ between exercises. Check your live brief for what to do about the break.
- Submission to Blackboard is final. You cannot change it after.

## What Ex4 asks for (v11 brief, five topics)

| # | Topic | Your evidence | Where it is |
| --- | --- | --- | --- |
| 1 | Defensive programming | Script A, tests, a bug found, fixed and retested | `sync-validator/` |
| 2 | Algorithms | Script B, definition, two approaches, timings | `alert-triage/` |
| 3 | Secure programming principles | The 9 vulnerable and fixed pairs, plus Script A | `python/` |
| 4 | Methodology | A short secure development table | Friday, Step F4 |
| 5 | Written justification | 1,000 words (900 to 1,100) | Friday afternoon |

Marking uses the **v4 grade tables**. Keep the printed v4 pack open beside you.

## Time tables

**Thursday**

| Clock | Task | Minutes |
| --- | --- | --- |
| 09:30 | T1 Setup | 15 |
| 09:45 | T2 Read the brief and the v4 table | 15 |
| 10:00 | T3 Log: problem and spec for Script A | 20 |
| 10:20 | T4 Run Script A tests | 10 |
| 10:30 | T5 Show the bug, fix it, retest | 20 |
| 10:50 | T6 Static scan | 10 |
| 11:00 | T7 Understand Script A | 30 |
| 11:30 | T8 Test table and link to Ex1 | 15 |
| 11:45 | T9 Add three tests of your own | 30 |
| 12:15 | Spare time | 15 |
| 12:30 | **Break** | 30 |
| 13:00 | T10 Script B: problem, definition, pseudocode | 30 |
| 13:30 | T11 Two approaches | 10 |
| 13:40 | T12 Run Script B tests | 10 |
| 13:50 | T13 Understand Script B | 30 |
| 14:20 | T14 Time it | 15 |
| 14:35 | T15 Add two tests of your own | 20 |
| 14:55 | T16 Save and tidy | 15 |
| 15:10 | Spare time, then stop | 20 |

**Friday**

| Clock | Task | Minutes |
| --- | --- | --- |
| 09:30 | F1 Setup | 10 |
| 09:40 | F2 The 9 secure programming pairs | 30 |
| 10:10 | F3 Principles used in Script A | 15 |
| 10:25 | F4 Secure development table | 20 |
| 10:45 | F5 Gather evidence into one document | 45 |
| 11:30 | F6 Justification sections 1 and 2 | 60 |
| 12:30 | **Break** | 30 |
| 13:00 | F7 Justification sections 3, 4 and 5 | 50 |
| 13:50 | F8 Word count and tidy | 15 |
| 14:05 | F9 Check against the v4 table | 25 |
| 14:30 | F10 Final checks | 15 |
| 14:45 | F11 **Upload** | 15 |
| 15:00 | Spare hour (do not use it unless you must) | 60 |

---

# WEDNESDAY NIGHT (10 minutes, optional)

Do T1 now if you can. Then stop.

---

# THURSDAY

## T1 Setup (15 min)

- [ ] Open **Command Prompt** (press the Windows key, type `cmd`, Enter).
- [ ] Go to your repo. Type this (change the path to wherever your EPA folder is) and press Enter:
  ```
  cd C:\path\to\EPA\ex4-defensive
  ```
- [ ] Check the files are there. Type `dir` and press Enter. You should see `sync-validator` and `alert-triage` in the list.
- [ ] Check Python works:
  ```
  python --version
  ```
  You should see `Python 3.` and a number. If you get an error, try `py --version`. If `py` works, use `py` instead of `python` for every command in this guide.
- [ ] Install the tools:
  ```
  pip install pytest bandit
  ```
  You should see `Successfully installed` (or `already satisfied`).
- [ ] Make an evidence folder **outside the repo**: on your Desktop, create a folder named `ex4-evidence`. All screenshots go there.
- [ ] Open Notepad. Save a new file as `ex4-evidence\log.txt`. You will paste text into this all day.
- [ ] Paste this at the top of the log and save:
  ```
  EX4 LOG

  NOTE ON AI USE: The starter code for both scripts was drafted with AI
  assistance (Claude). I ran, tested, debugged and reviewed it myself.
  ```

**How to take a screenshot:** press Windows key + Shift + S, drag a box, then paste into Paint and save, or into the Word document directly. Name files as the steps say.

## T2 Read the brief (15 min)

- [ ] Open the v11 brief. Find **Exercise 4**. Read the five circle bullets (the ones you must attempt).
- [ ] Open the printed **v4 pack**. Find the Ex4 table. Look for anything it asks for that is not in the time table above.
- [ ] If the v4 table asks for something extra (a specific language, a code listing, a number of test cases), write it in the log under the heading `EXTRA FROM V4`.

## T3 Log: problem and spec for Script A (20 min)

- [ ] Paste into the log. **Fill in the blanks using your own case study.**

  ```
  SCRIPT A PROBLEM
  The company's sync API takes visit notes from staff devices. A weak or
  unchecked request could store bad data or leak patient records. I built a
  validator that rejects bad requests before they reach the database.
  Risks from the case study this addresses: [write the ones that apply, for
  example weak API authentication, insecure sync]
  ```

- [ ] Paste this spec table. It states the inputs, outputs and constraints, which the brief asks for.

  | Field | Rule |
  | --- | --- |
  | client_id, staff_id, patient_ref | text, 1 to 64 characters, letters, digits, `_` and `-` only |
  | note_text | text, 1 to 20,000 characters, not blank, no control characters (newlines and tabs allowed) |
  | created_at | a valid date, not more than 5 minutes in the future, not older than 30 days |
  | whole request | valid JSON object, max 64 KB |
  | extra fields | rejected |
  | duplicate JSON keys | rejected |

  ```
  Input:  the raw request body (bytes)
  Output: a clean dictionary, or an error that names only the bad field
  Rule:   reject everything unless it is explicitly allowed
  Order:  cheapest checks first (size, then JSON, then fields)
  ```

## T4 Run Script A's tests (10 min)

- [ ] Go to the folder:
  ```
  cd sync-validator
  ```
- [ ] Run:
  ```
  python -m pytest -v
  ```
- [ ] You should see 28 lines ending `PASSED`, then `28 passed`.
- [ ] Screenshot it. Save as `A1_tests_pass.png`.

## T5 Show the bug, fix it, retest (20 min)

This is your **debug and retest** evidence.

**What the bug is:** the first draft checked IDs with `match` and a pattern ending in `$`. In Python, `$` also matches just before a trailing newline. So an ID like `abc` followed by a newline slipped through. This is a real, well-known mistake. The fix is `fullmatch`, which must match the whole string. The test suite caught it.

- [ ] Open the file:
  ```
  notepad sync_validator.py
  ```
- [ ] Press Ctrl+F. Search for `fullmatch`. You will find this line:
  ```
  if not ID_PATTERN.fullmatch(data[name]):
  ```
- [ ] Change `fullmatch` to `match`. Save the file (Ctrl+S).
- [ ] Run the tests again:
  ```
  python -m pytest -q
  ```
- [ ] You should see `1 failed, 27 passed`. The failing test is `test_security_trailing_newline_in_id`.
- [ ] Screenshot it. Save as `A2_bug_found.png`.
- [ ] Change `match` back to `fullmatch`. Save the file.
- [ ] Run the tests again:
  ```
  python -m pytest -q
  ```
- [ ] You should see `28 passed`. Screenshot it. Save as `A3_fixed_retest.png`.
- [ ] Paste into the log:
  ```
  BUG FOUND AND FIXED
  Defect: ID_PATTERN.match with "$" accepts an ID with a trailing newline.
  Found by: test_security_trailing_newline_in_id (1 failed, 27 passed).
  Why it matters: a newline in an ID could split log lines or bypass filters.
  Fix: use fullmatch so the whole string must match.
  Retest: 28 passed. No other test affected.
  ```

**If the file got messed up**, restore it:
```
git checkout -- sync_validator.py
```

## T6 Static scan (10 min)

- [ ] Run (still in `sync-validator`):
  ```
  python -m bandit -r sync_validator.py
  ```
- [ ] You should see `No issues identified.`
- [ ] Screenshot it. Save as `A4_bandit.png`.
- [ ] Paste into the log: `Static analysis (bandit) found no issues in Script A.`

## T7 Understand Script A (30 min)

You must be able to explain this code. Open `sync_validator.py` in Notepad and read it with this table beside you.

| Part of the code | Plain English |
| --- | --- |
| `MAX_BODY`, `FIELDS` | The limits. 64 KB for the whole request, and a maximum length for each field. |
| `ValidationError` | An error that carries only a field name. It never repeats what the user sent, so nothing leaks. |
| `_no_duplicate_keys` | Rejects a request that repeats a key, like two `client_id`s. An attacker might hope one check sees the first and another sees the last. |
| `_parse_date` | Checks the date is real, not more than 5 minutes ahead, not older than 30 days. |
| `validate`, step 1 | Check the size before doing anything else. A huge body can't tie up the server. |
| `validate`, step 2 | Parse the JSON. If it is broken or not valid text, reject. |
| `validate`, step 3 | Must be an object with exactly the expected fields. No extras (like `is_admin`), none missing. |
| `validate`, step 4 | Each field must be text, not blank, and not too long. |
| `validate`, step 5 | IDs may only use safe characters. Notes may not contain control characters like a null byte. |
| `validate`, step 6 | Final date check. |

- [ ] For each row, write **one sentence in your own words** in the log under `SCRIPT A: MY UNDERSTANDING`. If you can't, ask me in the chat.

## T8 Test table and link to Ex1 (15 min)

- [ ] Paste into the log:
  ```
  SCRIPT A TEST SUMMARY (28 tests)
  Normal (2)     good note; multi-line note with a tab
  Boundary (8)   64/65 char IDs; 20,000/20,001 char note; 29d23h old OK and
                 31d old rejected; 4 min future OK and 10 min future rejected
  Error (9)      empty body; not JSON; JSON list; missing field; number for
                 string; blank note; bad date; date as number; text not bytes
  Security (9)   SQL injection; path traversal; trailing newline; null byte;
                 10 MB body; duplicate keys; extra "is_admin" field; invalid
                 UTF-8; error does not echo input
  ```
- [ ] Paste one more line:
  ```
  Link to Ex1: this validator applies the same rules as my Ex1 sync.php
  prototype (field limits, 64 KB body, type checks) and adds a date window,
  strict ID patterns, control character checks and duplicate key rejection.
  ```

## T9 Add three tests of your own (30 min)

This makes the work yours, and it is good evidence.

- [ ] Open `test_sync_validator.py` in Notepad. Scroll to the bottom.
- [ ] Copy and paste this at the bottom, then save:
  ```python
  # ---------- MY OWN TESTS ----------
  def test_mine_unicode_lookalike_in_id():
      rejects(good(client_id="dev\u0430\u0432"), "client_id")   # Cyrillic letters


  def test_mine_emoji_in_note_is_allowed():
      assert validate(good(note_text="Patient happy \U0001F600"), now=NOW)


  def test_mine_empty_json_object():
      rejects(b"{}", "missing_field")
  ```
- [ ] Run:
  ```
  python -m pytest -q
  ```
- [ ] You should see `31 passed`. If one fails, **do not panic**. Read the message. That is the process working. Write down what failed, why, and what you changed.
- [ ] Now invent **one more** test of your own. Think of a nasty request. Add it the same way. Run again.
- [ ] Screenshot the final count. Save as `A5_my_tests.png`.
- [ ] Update the log: `I added [N] tests of my own: [list them]. Result: [result].`

**Spare time (15 min).** Drink water. Stretch. Then the break.

---

## BREAK 12:30 to 13:00

Eat. Leave the screen. Check your live brief for any break rules.

---

## T10 Script B: problem, definition, pseudocode (30 min)

- [ ] Go to the other folder:
  ```
  cd ..\alert-triage
  ```
- [ ] Paste into the log. **Fill in the blanks using your own case study.**
  ```
  SCRIPT B PROBLEM
  The case study lists alert fatigue as a risk. Repeated alerts bury the real
  incidents. I built an algorithm that groups duplicates and ranks what is left.
  ```
- [ ] Paste the definition. The brief wants this written **before** the code.
  ```
  ALGORITHM DEFINITION
  Input:   list of alerts: source, type, asset, severity (1-5), time (seconds)
  Output:  the top 100 incidents ranked by score, plus a count of rejected alerts
  Group:   same (source, type, asset) within 10 minutes of the group's first alert
  Score:   severity x asset criticality x log(count + 1)
           criticality: patient-db 5, sync-api 4, laptop 2, anything else 1
  Assumptions: timestamps are trusted; the criticality table is kept up to date
  Constraint:  must cope with 10,000 alerts a minute and a deliberate flood

  PSEUDOCODE
   1. Throw out any alert that fails validation and count it.
   2. Sort the good alerts by time.
   3. For each alert, find its group (a dictionary lookup).
   4. If the group is older than 10 minutes, close it and start a new one.
   5. Otherwise add 1 to its count and keep the highest severity.
   6. If there are too many open groups, close the oldest one (flood defence).
   7. Closed groups go into a small "best 100" heap.
   8. Return the best 100, highest score first.
  ```

## T11 Two approaches (10 min)

- [ ] Paste into the log:
  ```
  ALTERNATIVES
  A. Compare every alert with every other alert: O(n squared). At 100,000
     alerts that is about 10 billion comparisons. Far too slow.
  B. Dictionary keyed by group (chosen): one lookup per alert. The time sort is
     the slowest step, so overall O(n log n). Memory is capped by
     MAX_OPEN_GROUPS (50,000) plus TOP_N (100).
  Weakness of B: an attacker can send many unique alerts to try to use up
  memory. Defence: when the limit is reached, the oldest open group is closed.
  ```

## T12 Run Script B's tests (10 min)

- [ ] Run:
  ```
  python -m pytest -v
  ```
- [ ] You should see 16 lines ending `PASSED`, then `16 passed`.
- [ ] Screenshot it. Save as `B1_tests_pass.png`.
- [ ] Paste into the log:
  ```
  SCRIPT B TEST SUMMARY (16 tests)
  Normal (3)    3 identical alerts become 1 incident; patient-db ranks above
                laptop; unsorted input still works
  Boundary (5)  empty list; single alert; exactly 600 s is one incident; 601 s
                is two; severity 1 and 5 accepted
  Error (4)     severity 0 and 9; missing field; NaN and text times; non-dict items
  Security (4)  severity as string; boolean severity; 1 MB asset name; a flood of
                20,000 unique alerts stays under 60 MB and returns only 50 incidents
  ```

## T13 Understand Script B (30 min)

Open `alert_triage.py` in Notepad.

| Part of the code | Plain English |
| --- | --- |
| `_valid` | Throws out any alert that is malformed: wrong type, severity outside 1 to 5, text too long, time not a real number. |
| `_score` | Severity, times how important the asset is, times a number that grows slowly as the count grows. Many repeats matter, but not endlessly. |
| `good.sort` | Puts alerts in time order. This is the slowest step. |
| `open_groups` | A dictionary. Each key is (source, type, asset). The value is the group being built. |
| The window check | If the new alert is more than 10 minutes after the group's first alert, the old group is closed and a new one starts. |
| The `max_open` check | The flood defence. If there are too many open groups, close the oldest one so memory can't grow without limit. |
| `best` and `heapq` | Keeps only the top 100 scored incidents. Memory stays small however many alerts arrive. |

- [ ] Write **one sentence per row in your own words** in the log under `SCRIPT B: MY UNDERSTANDING`.

## T14 Time it (15 min)

- [ ] Run:
  ```
  python timing.py
  ```
- [ ] You should see three lines like this (your numbers will differ):
  ```
      1000 alerts: 0.002 seconds
     10000 alerts: 0.018 seconds
    100000 alerts: 0.146 seconds
  ```
- [ ] Screenshot it. Save as `B2_timing.png`.
- [ ] Paste into the log **using your own numbers**:
  ```
  TIMING
  1,000 alerts     [your number] s
  10,000 alerts    [your number] s
  100,000 alerts   [your number] s
  100 times more alerts took roughly [your ratio] times longer. That is close
  to n log n, not n squared (which would be 10,000 times longer). The
  requirement of 10,000 alerts a minute is met easily.
  Improvements: skip the sort if alerts already arrive in time order; use a
  rolling window so one attack is not split at the 10 minute edge.
  ```
  (Ratio: divide the 100,000 time by the 1,000 time.)

## T15 Add two tests of your own (20 min)

- [ ] Open `test_alert_triage.py`. Paste this at the bottom and save:
  ```python
  # ---------- MY OWN TESTS ----------
  def test_mine_two_assets_do_not_merge():
      out = triage([alert(0, asset="laptop"), alert(1, asset="patient-db")])
      assert len(out["incidents"]) == 2


  def test_mine_highest_severity_is_kept():
      out = triage([alert(0, severity=2), alert(5, severity=5)])
      assert out["incidents"][0]["severity"] == 5
  ```
- [ ] Run `python -m pytest -q`. You should see `18 passed`.
- [ ] Think of **one more** of your own and add it.
- [ ] Update the log with what you added.
- [ ] Screenshot. Save as `B3_my_tests.png`.

## T16 Save and tidy (15 min)

- [ ] In Command Prompt run `cd ..` to get back to `ex4-defensive`.
- [ ] Check your log is saved in `ex4-evidence`.
- [ ] Count your screenshots. You should have `A1, A2, A3, A4, A5, B1, B2, B3`.
- [ ] **Optional:** save your changed test files to the repo:
  ```
  git add sync-validator alert-triage
  git commit -m "Ex4: my own tests"
  git push
  ```
- [ ] **Thursday is done.** Stop. Eat. Rest.

---

# FRIDAY

## F1 Setup (10 min)

- [ ] Open Command Prompt. Run:
  ```
  cd C:\path\to\EPA\ex4-defensive
  ```
- [ ] Open `ex4-evidence\log.txt` in Notepad. Check Thursday's work is all there.
- [ ] Open the v11 brief and the printed v4 pack.

## F2 The 9 secure programming pairs (30 min)

These are already in your repo. They show 9 common security flaws, each with the attack and the fix.

- [ ] Run:
  ```
  python -m pytest -v python
  ```
- [ ] You should see `9 passed`. Screenshot it. Save as `P1_nine_pairs.png`.
- [ ] Open `python\vuln_examples.py`. Each pair has a comment with the CWE (a standard number for the flaw type), the attack, and the fix. Skim all nine.
- [ ] Paste this table into the log. **Edit the last column** to match your own case study risks.

  | Pair | CWE | Case study risk it maps to |
  | --- | --- | --- |
  | Path traversal | CWE-22 | insecure sync (an attacker reads files) |
  | SQL injection | CWE-89 | insecure sync, weak API |
  | Command injection | CWE-78 | insecure sync, weak API |
  | Timing side channel | CWE-208 | weak API authentication |
  | Race condition (TOCTOU) | CWE-367 | cached records on shared devices |
  | Weak password storage | CWE-916 | strong IAM |
  | Unsafe deserialisation | CWE-502 | insecure sync |
  | Predictable tokens | CWE-338 | weak API authentication |
  | XSS | CWE-79 | staff web portal |

## F3 Principles used in Script A (15 min)

- [ ] Paste into the log:
  ```
  SECURE PROGRAMMING PRINCIPLES IN SCRIPT A
  Default deny: only explicitly allowed input passes.
  Validate early: size check before parsing; cheap checks first.
  Least information: errors name the field, never the input
    (test_security_error_never_echoes_input).
  No dangerous functions: no eval, pickle or string-built SQL.
  Fail closed: any problem raises an error; nothing partial is returned.
  ```

## F4 Secure development table (20 min)

- [ ] Paste into the log:
  ```
  METHODOLOGY: Agile with security gates
  Why: the company is replacing its system in stages, requirements will change,
  and security checks must repeat every cycle, not happen once at the end.
  ```

  | Stage | Security activity | Example from my work |
  | --- | --- | --- |
  | Requirements | Abuse cases and acceptance criteria | "Reject any note over 64 KB" |
  | Design | Threat model (STRIDE) of the sync flow | Token theft, replay, tampering |
  | Build | Code review, static analysis, version control | bandit scan; the fullmatch fix |
  | Test | Normal, boundary, error and security tests; retest after every fix | all the tests across both scripts |
  | Deploy and maintain | Token revocation, patching, monitoring | Script B reduces alert fatigue |

- [ ] If you want a different model (Waterfall, V-model, DevSecOps), change the table and the "Why" line. Pick **one**, and say why.

## F5 Gather evidence into one document (45 min)

- [ ] Open Word. Save as `Ex4_YourName.docx`.
- [ ] Add these headings: **Justification**, **Script A evidence**, **Script B evidence**, **Secure programming and methodology**, **Appendix: code**.
- [ ] Under Script A evidence, paste from your log: problem, spec, bug and fix, test summary, own tests, understanding. Insert screenshots A1 to A5. Add a one-line caption to each.
- [ ] Under Script B evidence, the same: problem, definition, pseudocode, alternatives, test summary, timing, own tests. Insert B1 to B3.
- [ ] Under Secure programming and methodology: the pairs table, the principles, the development table, and screenshot P1.
- [ ] Under Appendix: copy the code of `sync_validator.py` and `alert_triage.py` into the document (use a small font and a code font like Consolas). **Check your brief to see if code must be included.**
- [ ] Crop screenshots tight. Check any page limit in your live brief.

## F6 Justification, sections 1 and 2 (60 min)

**Target 1,000 words. Allowed 900 to 1,100.** About 200 words per section.

Your method (agreed with your assessor): get a draft, then rewrite it in your own words from your own evidence.

- [ ] In the chat, ask: "Draft section 1 and 2 of my Ex4 justification using this log" and paste the relevant parts of your log. Do **not** paste it straight into the document.
- [ ] Read the draft. Then **rewrite it** using your own words and your own numbers.

**Section 1: Why these two components (about 150 words).** Link to the case study risks. Say why Python (readable, strong libraries, quick to test). Starter sentence:
> "The case study lists [risk 1], [risk 2] and alert fatigue. I chose to build [Script A] because ... and [Script B] because ..."

**Section 2: Script A (about 250 words).** What it checks and why. One attack from the test table. The bug: what it was, how the test found it, the fix, the retest. Starter sentence:
> "My first version accepted an identifier ending in a newline because ... A test I wrote caught it ... I fixed it by ... and all [N] tests then passed."

## BREAK 12:30 to 13:00

Eat. Leave the screen.

## F7 Justification, sections 3, 4 and 5 (50 min)

**Section 3: Script B (about 250 words).** The problem. The algorithm. The two approaches and why you chose the dictionary. Your three timing numbers. The flood defence. One honest limitation. Starter sentence:
> "I compared two approaches. Comparing every alert with every other alert would take about n squared steps ... I chose ... My timings of [x], [y] and [z] seconds show ..."

**Section 4: Secure programming and methodology (about 200 words).** The 9 pairs (name two). Two principles from F3. The development model you chose and why. Starter sentence:
> "Script A applies default deny and ... I chose [model] because ..."

**Section 5: Limits and next steps (about 150 words).** What you did not test. Unit tests are not penetration tests. These are prototypes. What you would do next. Starter sentence:
> "These scripts are prototypes. I did not test ... Next I would ..."

- [ ] Add the AI reference line at the end of the justification:
  > "AI assistance (Claude) was used to draft starter code and initial text. I ran, tested, debugged and reviewed all code, and rewrote this text from my own evidence."

## F8 Word count and tidy (15 min)

- [ ] In Word, look at the word count at the bottom left. Select only the justification text to count it on its own.
- [ ] Too long? Cut the weakest sentence from each section. Too short? Add one example to section 2 or 3.
- [ ] Spell check (F7 key in Word).

## F9 Check against the v4 table (25 min)

- [ ] Open the printed v4 pack at the Ex4 table.
- [ ] For each row, write beside it **where in your document** the evidence is.
- [ ] Any row with nothing? Add one or two sentences or a screenshot.
- [ ] Anything you noted under `EXTRA FROM V4` in T2? Check it is covered.

## F10 Final checks (15 min)

- [ ] Justification word count is 900 to 1,100
- [ ] AI use is referenced
- [ ] All screenshots are in and cropped
- [ ] Bug, fix and retest are clearly shown
- [ ] Your own tests are listed
- [ ] Your name or learner number is on it (check what the brief asks for)
- [ ] File name is sensible
- [ ] Saved as **PDF** as well, if the upload accepts it (File, Save As, PDF)

## F11 Upload (15 min)

- [ ] Go to **Blackboard**. Find the Ex4 submission.
- [ ] Upload the file.
- [ ] **You cannot amend it after.** Check the file name and that the upload completed.
- [ ] Screenshot the confirmation.
- [ ] You are finished. Close the laptop. Well done.

---

## If it goes wrong

| What you see | What to do |
| --- | --- |
| `'python' is not recognized` | Try `py` instead of `python`. If that fails, install Python from python.org and tick "Add python.exe to PATH". |
| `No module named pytest` | Run `python -m pip install pytest` again. |
| `No module named sync_validator` | You are in the wrong folder. Type `dir` and check you can see `sync_validator.py`. |
| Tests fail straight away at T4 | You edited a file by accident. Run `git checkout -- .` to restore, then retry. |
| T5 shows no failure after changing to `match` | You did not save the file. Save it (Ctrl+S) and re-run. |
| `bandit` is not recognised | Use `python -m bandit -r sync_validator.py` |
| Your timing numbers differ from the guide | Normal. Use your own. |
| Word count too high or low | See F8. |
| Panicking | Stand up. Water. Say the next step aloud. |

## Questions an assessor might ask (have a short answer ready)

1. **Why reject by default?** Because anything I forgot to think of is then blocked, not allowed.
2. **What was the bug and how did you find it?** Trailing newline passed the ID check. A security test caught it. I fixed it with `fullmatch` and retested.
3. **Why a dictionary in Script B?** One lookup per alert, so it scales. Comparing every pair would be n squared.
4. **What stops an alert flood using all the memory?** The open group cap closes the oldest group, and only the top 100 incidents are kept.
5. **What did these tests not cover?** Real network attacks, real data, and integration with the live API. They are unit tests.
6. **How did you use AI?** Starter code and draft text. I ran and tested everything, added my own tests, and rewrote the text from my own evidence.
