# Ex4: START HERE (Thursday and Friday, one small step at a time)

Open this file and nothing else. Do one box. Tick it. Next box.

**Deadline: Friday 16:00. Aim to upload by 15:15.** That leaves a safety gap.

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

- Open book. Individual test. **No AI during test hours.** AI is for preparing beforehand only. Prepared material may be brought in. The v4 pack also bans personal communication and online asynchronous interaction.
- The starter code and notes in this folder were prepared before the test, with AI. **Reference that** the way your assessor said. You run it, test it, debug it, review it, and write the justification in **your own words from your own evidence**.
- **Screenshots: 5 pages of A4 maximum.** Crop tightly.
- Break: 30 minutes. v4 says to email your supervisor when it starts and ends. Other exercises have said not to. **Check your live v11 brief.**
- Submission to Blackboard is final. You cannot change it after.

## What Ex4 asks for

The v11 brief has five circle topics. The v4 pack grades them against these rows. Marking uses the **v4 grade tables**. Keep the printed v4 pack open beside you.

| # | v11 topic | v4 rows | Your evidence | Where |
| --- | --- | --- | --- | --- |
| 1 | Defensive programming | TC6, TKU10 | Script A, defects, fuzzing, CLI script, assembler, language levels | `sync-validator/`, `mips/` |
| 2 | Algorithms | TC7, TKU6, TKU7 | Script B, complexity, discrete maths | `alert-triage/` |
| 3 | Secure programming principles | TC10, TKU10 | Vulnerability review, nine pairs, patterns, compiler features, OWASP/CERT, formal method | `python/`, Friday |
| 4 | Methodology | TC11, TKU11 | System description, lifecycle, sequential versus agile | Friday |
| 5 | Written justification | all | 1,000 words (900 to 1,100) | Friday |

**Only TC10 and TKU10 can earn Merit or Distinction in Ex4.** Every other Ex4 row is pass only. A fail on any row fails the exercise, so cover every row first, then spend spare time on TC10.

## Time tables

**Thursday (09:30 to 16:00)**

| Clock | Task | Minutes |
| --- | --- | --- |
| 09:30 | T1 Setup | 10 |
| 09:40 | T2 Read the brief | 10 |
| 09:50 | T3 Script A: problem and spec | 15 |
| 10:05 | T4 Run Script A tests | 10 |
| 10:15 | T5 Defect hunt (three defects) | 40 |
| 10:55 | T6 Static analysis | 5 |
| 11:00 | T7 Dynamic analysis (fuzzing) | 15 |
| 11:15 | T8 Understand Script A | 25 |
| 11:40 | T9 Scripting: command-line tool | 10 |
| 11:50 | T10 Test table and Ex1 link | 10 |
| 12:00 | T11 Three tests of your own | 20 |
| 12:20 | Spare | 10 |
| 12:30 | **Break** | 30 |
| 13:00 | T12 Script B: problem and definition | 25 |
| 13:25 | T13 Approaches, complexity, discrete maths | 25 |
| 13:50 | T14 Run Script B tests | 10 |
| 14:00 | T15 Understand Script B | 20 |
| 14:20 | T16 Time it | 10 |
| 14:30 | T17 Two tests of your own | 15 |
| 14:45 | T18 Assembler | 25 |
| 15:10 | T19 High-level to low-level | 20 |
| 15:30 | T20 Save and tidy | 10 |
| 15:40 | Spare | 20 |

Behind? Cut in this order: T11 and T17 extra tests, T10 Ex1 link, T13 automaton. **Never cut:** T5, T12, T18, T19 and the screenshots.

**Friday (09:30 to 16:00)**

| Clock | Task | Minutes |
| --- | --- | --- |
| 09:30 | F1 Setup | 10 |
| 09:40 | F2 Nine secure programming pairs | 10 |
| 09:50 | F3 Vulnerability review table | 40 |
| 10:30 | F4 Principles and patterns | 15 |
| 10:45 | F5 Compiler features, static and dynamic analysis | 15 |
| 11:00 | F6 Sources and a formal method | 25 |
| 11:25 | F7 System description, lifecycle, methodology | 35 |
| 12:00 | F8 Gather evidence into one document | 25 |
| 12:25 | Spare | 5 |
| 12:30 | **Break** | 30 |
| 13:00 | F9 The justification | 90 |
| 14:30 | F10 Check against the v4 table | 20 |
| 14:50 | F11 Final checks | 10 |
| 15:00 | F12 **Upload** | 15 |
| 15:15 | Spare (do not use it unless you must) | 45 |

---

# WEDNESDAY NIGHT (10 minutes, optional)

Do T1 now if you can. Then stop.

---

# THURSDAY

## T1 Setup (10 min)

- [ ] Open **Command Prompt** (Windows key, type `cmd`, Enter).
- [ ] Go to the folder (change the path to where your EPA folder is):
    ```
    cd C:\path\to\EPA\ex4-defensive
    ```
- [ ] Check the files are there. Type `dir`. You should see `sync-validator`, `alert-triage`, `mips`, `python`.
- [ ] Check Python. You should see `Python 3.` and a number. If it errors, try `py --version` and use `py` instead of `python` for every command today:
    ```
    python --version
    ```
- [ ] Install the tools. You should see `Successfully installed` or `already satisfied`:
    ```
    pip install pytest bandit
    ```
- [ ] On the Desktop make a folder `ex4-evidence`. Screenshots go here.
- [ ] In Notepad save `ex4-evidence\log.txt`. Paste this at the top:
    ```
    EX4 LOG

    NOTE ON AI USE: The starter code and notes for this exercise were prepared
    with AI assistance (Claude) BEFORE the test. During the test I ran, tested,
    debugged and reviewed the code myself and wrote my own evidence and text.
    ```

**Screenshot budget.** The rules allow **5 pages of A4 for screenshots**. Crop tightly. Take only the screenshots named in this guide. Each is labelled so you can place 2 to 4 on a page.

## T2 Read the brief (10 min)

- [ ] Open the v11 brief at Exercise 4. Read the five circle bullets.
- [ ] Open the printed v4 pack at the Ex4 rows. Tick each one against this table:

| v4 row | What it wants (pass level) | Where you cover it |
| --- | --- | --- |
| TC6 | A program in a high-level language, mapped to low-level code, a simple assembler solution, a scripting solution | Script A (T3 to T11), CLI (T9), assembler and language levels (T18, T19) |
| TC7 | Design, implement and analyse an algorithm | Script B (T12 to T17) |
| TC10 | Secure programming principles and design patterns, with evidence. **Merit:** more subtle vulnerabilities. **Distinction:** mitigations for them | Defects (T5), fuzzing (T7), review table (Friday F3) |
| TC11 | A systematic methodology, whole lifecycle, a system description | Friday F7 |
| TKU6, TKU7 | Languages, translation, algorithms, complexity, discrete maths | T13, T19 |
| TKU10 | Defensive programming, malware resistance, patterns, compiler features, static and dynamic analysis, OWASP/CERT, one formal method | T5 to T7, Friday F4 to F6 |
| TKU11 | Lifecycle, sequential versus agile, tools, systems engineering | Friday F7 |

- [ ] **Only TC10 and TKU10 can earn Merit or Distinction in Ex4.** Put your extra effort there.
- [ ] Anything the v11 brief or v4 table asks for that is not here? Write it in the log under `EXTRA`.

## T3 Log: Script A problem and spec (15 min)

- [ ] Paste into the log:
    ```
    SCRIPT A PROBLEM
    The company's sync API takes visit notes from staff devices. A weak or unchecked
    request could store bad data, crash the service or leak patient records. I built a
    validator that rejects bad requests before they reach the database.
    Risks from the case study this addresses: [the case study risks this addresses, for example weak API authentication, insecure sync]
    ```
- [ ] Paste the spec. The brief wants inputs, outputs and constraints.
    ```
    SCRIPT A SPEC
    client_id, staff_id, patient_ref: text, 1-64 chars, letters digits _ - only
    note_text: text, 1-20,000 chars, not blank, no control characters,
               must be storable as UTF-8
    created_at: valid date, max 5 min in future, max 30 days old
    whole request: valid JSON object, max 64 KB, must not crash the parser
    extra fields: rejected.  duplicate JSON keys: rejected.
    Input:  raw request body (bytes)
    Output: clean dictionary, or an error naming only the bad field
    Rule:   reject everything unless explicitly allowed
    Order:  cheapest checks first (size, JSON, then fields)
    ```

## T4 Run Script A's tests (10 min)

- [ ] Go into the folder:
    ```
    cd sync-validator
    ```
- [ ] Run. You should see 31 lines ending `PASSED`, then `31 passed`:
    ```
    python -m pytest -v test_sync_validator.py
    ```
- [ ] Screenshot it. Save as `A1_tests_pass.png`.

## T5 Defect hunt: three defects (40 min)

The starter code already has three fixes. Each one closes a real, subtle defect. You will remove each fix, **watch the tests catch it**, then put it back. This is your **debug and retest** evidence, and your **subtle vulnerabilities and mitigations** evidence for TC10.

**Method for each defect:** edit, save, run, screenshot, restore, run again.

**Restore tip:** if you lose track, run `git checkout -- sync_validator.py` to reset the file.

### D1: trailing newline in an ID (10 min)

`$` in a Python pattern also matches just before a final newline, so `abc` plus a newline looked valid.

- [ ] Open the file: `notepad sync_validator.py`
- [ ] Ctrl+F `fullmatch`. You will find: `if not ID_PATTERN.fullmatch(data[name]):`
- [ ] Change `fullmatch` to `match`. Save.
- [ ] Run `python -m pytest -q test_sync_validator.py`. You should see `1 failed, 30 passed` (failing: `test_security_trailing_newline_in_id`).
- [ ] Screenshot: `A2_D1_found.png`
- [ ] Change `match` back to `fullmatch`. Save. Run again: `31 passed`.

### D2: a character that cannot be stored (15 min)

A JSON escape like `\ud800` becomes a lone surrogate. It looks like text but cannot be written as UTF-8, so storing or logging the note would crash.

- [ ] Ctrl+F `_is_utf8_safe(value)`. You will find the line ending `or not _is_utf8_safe(value):`
- [ ] Delete ` or not _is_utf8_safe(value)` so the line ends `len(value) > max_len:`. Save.
- [ ] Run `python -m pytest -q test_sync_validator.py`. You should see `1 failed, 30 passed` (failing: `test_security_lone_surrogate_in_note`).
- [ ] Screenshot: `A3_D2_found.png`
- [ ] Put ` or not _is_utf8_safe(value)` back. Save. Run again: `31 passed`.

### D3: JSON nested so deeply it crashes the parser (15 min)

30,000 nested brackets fit inside the 64 KB limit but make Python's parser raise `RecursionError`. Unhandled, that crashes the request.

- [ ] Ctrl+F `RecursionError`. You will find: `except (UnicodeDecodeError, ValueError, RecursionError):`
- [ ] Delete `, RecursionError` so it reads `except (UnicodeDecodeError, ValueError):`. Save.
- [ ] Run `python -m pytest -q test_sync_validator.py`. You should see `2 failed, 29 passed` (the two `deeply_nested` tests).
- [ ] Screenshot: `A4_D3_found.png`
- [ ] Put `, RecursionError` back. Save. Run the tests again: `31 passed`. Screenshot: `A5_all_fixed.png`

- [ ] Paste into the log:
    ```
    DEFECTS FOUND, FIXED AND RETESTED
    How: these three defects were found while preparing the code (with AI
    assistance) and fixed in the starter code. During the test I reproduced each
    one by removing its fix, confirmed the tests catch it, restored the fix and
    retested. Final result: 31 passed.

    D1 Trailing newline accepted in IDs (CWE-20)
       Why subtle: the pattern looks right; "$" matches before a final newline.
       Impact: newline in an ID can split log lines or bypass filters.
       Fix: fullmatch, so the whole string must match.
       Evidence: test_security_trailing_newline_in_id (1 failed, 30 passed).

    D2 Lone surrogate accepted in text (CWE-176, CWE-755)
       Why subtle: it is valid JSON and looks like text; it only fails later at storage.
       Impact: a crash when saving or logging the note (denial of service, lost data).
       Fix: _is_utf8_safe check on every text field.
       Evidence: test_security_lone_surrogate_in_note (1 failed, 30 passed).

    D3 Deeply nested JSON crashes the parser (CWE-674, CWE-248)
       Why subtle: the body is under the 64 KB size limit, so the size check passes.
       Impact: unhandled RecursionError, request crashes (denial of service).
       Fix: catch RecursionError and reject as invalid_json.
       Evidence: two deeply_nested tests (2 failed, 29 passed).
    ```

## T6 Static analysis (5 min)

Static analysis reads the code without running it.

- [ ] Run (still in `sync-validator`). Scan only the real code, not the tests:
    ```
    python -m bandit -r sync_validator.py validate_file.py
    ```
- [ ] You should see `No issues identified.` Screenshot: `A6_bandit.png`
- [ ] Log: `Static analysis: bandit found no issues in sync_validator.py and validate_file.py.`

## T7 Dynamic analysis: fuzzing (15 min)

Dynamic analysis runs the code. A fuzzer throws thousands of odd requests at it and checks two rules: it never crashes, and anything it accepts is really safe.

- [ ] Run:
    ```
    python fuzz_validator.py
    ```
- [ ] You should see:
    ```
    requests: 20000   accepted: 804   rejected: 19196   failures: 0
    ```
  Screenshot: `A7_fuzz_clean.png`
- [ ] **Show that it can catch a bug.** Repeat the D2 edit (delete ` or not _is_utf8_safe(value)`). Save. Run `python fuzz_validator.py`.
  You should see `failures:` with a number above 0 and a line `FAILURE type=UnicodeEncodeError`. Screenshot: `A8_fuzz_finds_D2.png`
- [ ] Put the code back. Save. Run the fuzzer again: `failures: 0`.
- [ ] Paste into the log:
    ```
    DYNAMIC ANALYSIS
    fuzz_validator.py sends 20,000 random and mutated requests (nested JSON,
    flipped bytes, odd Unicode, wrong types). Rule 1: only a result or a
    ValidationError is allowed. Rule 2: anything accepted must be safe.
    With the fixes: 0 failures. With the D2 fix removed: failures with
    UnicodeEncodeError, so the fuzzer finds this class of defect.
    ```

## T8 Understand Script A (25 min)

You must be able to explain this code. Open `sync_validator.py` in Notepad.

| Part of the code | Plain English |
| --- | --- |
| `MAX_BODY`, `FIELDS` | The limits: 64 KB total, a maximum length per field |
| `ValidationError` | Carries only a field name, never what the user sent, so nothing leaks |
| `_is_utf8_safe` | Checks text can be stored as UTF-8 (fix D2) |
| `_no_duplicate_keys` | Rejects a repeated key, so two checks can't see different values |
| `_parse_date` | Real date, not over 5 min ahead, not over 30 days old |
| `validate` step 1 | Size check first, so a huge body can't tie up the server |
| step 2 | Parse JSON. Broken JSON, invalid text and nesting that is too deep are rejected (fix D3) |
| step 3 | Exactly the expected fields. No extras like `is_admin`, none missing |
| step 4 | Each field is text, not blank, not too long, storable |
| step 5 | IDs use safe characters only (fix D1). No control characters in notes |
| step 6 | Final date check |

- [ ] One sentence per row, **in your own words**, in the log under `SCRIPT A: MY UNDERSTANDING`.

## T9 Scripting: a command-line tool (10 min)

`validate_file.py` is a small script that checks a request file from the command line. It treats the file as untrusted: only a normal file, and it never reads more than the size limit.

- [ ] Run these two:
    ```
    python validate_file.py samples\good.json
    python validate_file.py samples\bad_injection.json
    ```
- [ ] You should see `OK`, then `REJECTED: patient_ref`. If the first says `REJECTED: created_at`, open `samples\good.json` and change the date to today's date (the date must be within 30 days).
- [ ] Run its tests. You should see `6 passed`:
    ```
    python -m pytest -q test_validate_file.py
    ```
- [ ] Screenshot both together: `A9_cli.png`
- [ ] Paste into the log:
    ```
    SCRIPTING
    validate_file.py is a command-line script around validate(). It returns exit
    code 0 (accepted), 1 (rejected) or 2 (file problem), so it can be used in
    automation. It refuses folders and missing files, and reads at most
    MAX_BODY + 1 bytes, so a huge file cannot use up memory (tested with 5 MB).
    ```

## T10 Test table and Ex1 link (10 min)

- [ ] Paste into the log:
    ```
    SCRIPT A TEST SUMMARY (31 tests, plus 6 for the CLI)
    Normal (2)     good note; multi-line note with a tab
    Boundary (8)   64/65 char IDs; 20,000/20,001 char note; 29d23h old OK and
                   31d old rejected; 4 min future OK and 10 min future rejected
    Error (9)      empty body; not JSON; JSON list; missing field; number for
                   string; blank note; bad date; date as number; text not bytes
    Security (12)  SQL injection; path traversal; trailing newline; null byte;
                   10 MB body; duplicate keys; extra "is_admin" field; invalid
                   UTF-8; lone surrogate; two deep-nesting tests; error does
                   not echo input

    Link to Ex1: this validator applies the same rules as my Ex1 sync.php
    prototype (field limits, 64 KB body, type checks) and adds a date window,
    strict ID patterns, control character and encoding checks, duplicate key
    rejection and crash-proof parsing.
    ```

## T11 Three tests of your own (20 min)

- [ ] `notepad test_sync_validator.py`. Scroll to the very bottom. Paste, then save:
    ```python
    # ---------- MY OWN TESTS ----------
    def test_mine_unicode_lookalike_in_id():
        rejects(good(client_id="dev\u0430\u0432"), "client_id")


    def test_mine_emoji_in_note_is_allowed():
        assert validate(good(note_text="Patient happy \U0001F600"), now=NOW)


    def test_mine_empty_json_object():
        rejects(b"{}", "missing_field")
    ```
- [ ] Run `python -m pytest -q test_sync_validator.py`. You should see `34 passed`. If one fails, that is the process working: log what failed, why, and the fix.
- [ ] Invent **one more** nasty request of your own. Add it. Run again.
- [ ] Log: `I added [N] tests of my own: [list]. Result: [result].`

**Spare 10 min. Then BREAK 12:30 to 13:00.** Eat. Leave the screen. Check your live brief for what to do about the break.

---

## T12 Script B: problem and definition (25 min)

- [ ] Go to the other folder:
    ```
    cd ..\alert-triage
    ```
- [ ] Paste into the log:
    ```
    SCRIPT B PROBLEM
    The case study lists alert fatigue as a risk. Repeated alerts bury the real
    incidents. I built an algorithm that groups duplicates and ranks what is left.
    ```
- [ ] Paste the definition. The brief wants it **before** the code.
    ```
    ALGORITHM DEFINITION
    Input:   list of alerts: source, type, asset, severity (1-5), time (seconds)
    Output:  top 100 incidents ranked by score, plus a count of rejected alerts
    Group:   same (source, type, asset) within 10 min of the group's first alert
    Score:   severity x asset criticality x log(count + 1)
             criticality: patient-db 5, sync-api 4, laptop 2, anything else 1
    Assumptions: timestamps are trusted; the criticality table is kept up to date
    Constraint:  cope with a deliberate flood of unique alerts without running
                 out of memory

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

## T13 Approaches, complexity and discrete maths (25 min)

The v4 table wants algorithm analysis, strategies, data structures, complexity and discrete maths.

- [ ] Paste into the log:
    ```
    ALTERNATIVES
    A. Compare every alert with every other alert: O(n squared). At 100,000
       alerts that is about 10 billion comparisons. Far too slow.
    B. Dictionary keyed by group (chosen): one lookup per alert.
    Weakness of B: an attacker can send many unique alerts to use up memory.
    Defence: at the limit, the oldest open group is closed.

    STRATEGY AND DATA STRUCTURES
    Strategy: hashing (group by key) plus a greedy "keep only the best 100".
    List: holds the valid alerts. Sorting costs O(n log n).
    Dictionary (hash table): O(1) average lookup per alert. Python randomises
      string hashing, which stops an attacker engineering collisions.
    Heap (a binary tree stored in a list): each push O(log 100), memory fixed at 100.

    COMPLEXITY
    Time: O(n log n) for the sort, plus O(n) grouping, plus O(g log 100) for the
    heap, where g is the number of groups (g <= n). Overall O(n log n).
    Working memory beyond the input list: O(MAX_OPEN_GROUPS + TOP_N), fixed however
    many alerts arrive. (The list of valid alerts itself grows with the input.)

    DISCRETE MATHS
    Sets and relations: "same (source, type, asset)" is an equivalence relation
      (reflexive, symmetric, transitive), so it partitions the alerts into classes.
      The 10 minute window then splits each class into consecutive groups
      anchored on the first alert.
    Logic: an alert is valid when ALL of these hold (a conjunction): text fields
      non-empty and short, severity an integer in 1..5, time a finite number.
    Correctness argument (loop invariant): after processing k alerts, every valid
      alert so far is counted in exactly one group, open or closed.
    Graphs and trees: the heap is a binary tree.
    Automaton: each group is a small state machine.
      OPEN --(alert within window)--> OPEN (count + 1)
      OPEN --(alert after window, or group cap reached)--> CLOSED
      CLOSED --(score in top 100)--> KEPT      CLOSED --(otherwise)--> DROPPED
    ```

## T14 Run Script B's tests (10 min)

- [ ] Run. You should see 16 lines ending `PASSED`, then `16 passed`:
    ```
    python -m pytest -v
    ```
- [ ] Screenshot: `B1_tests_pass.png`
- [ ] Paste into the log:
    ```
    SCRIPT B TEST SUMMARY (16 tests)
    Normal (3)    3 identical alerts become 1 incident; patient-db ranks above
                  laptop; unsorted input still works
    Boundary (5)  empty list; single alert; exactly 600 s is one incident; 601 s
                  is two; severity 1 and 5 accepted
    Error (4)     severity 0 and 9; missing field; NaN and text times; non-dict items
    Security (4)  severity as string; boolean severity; 1 MB asset name; a flood of
                  20,000 unique alerts stays under 60 MB, returns only 50 incidents (the test asks for top_n=50)
    ```

## T15 Understand Script B (20 min)

- [ ] Open `alert_triage.py` in Notepad. One sentence per row, **your own words**, in the log under `SCRIPT B: MY UNDERSTANDING`.

| Part of the code | Plain English |
| --- | --- |
| `_valid` | Throws out malformed alerts: wrong type, severity outside 1 to 5, text too long, bad time |
| `_score` | Severity x asset importance x a number that grows slowly with the count |
| `good.sort` | Puts alerts in time order. The slowest step |
| `open_groups` | Dictionary. Key is (source, type, asset). Value is the group being built |
| window check | More than 10 min after the group's first alert: close it, start a new one |
| `max_open` check | Flood defence: too many open groups, close the oldest so memory can't grow without limit |
| `best` and `heapq` | Keeps only the top 100 incidents, so memory stays small |

## T16 Time it (10 min)

- [ ] Run (your numbers will differ):
    ```
    python timing.py
    ```
  Example: `1000 alerts: 0.002 seconds`, `10000: 0.018`, `100000: 0.146`
- [ ] Screenshot: `B2_timing.png`
- [ ] Paste into the log with **your own numbers** (ratio = the 100,000 time divided by the 1,000 time):
    ```
    TIMING
    1,000 alerts     [yours] s
    10,000 alerts    [yours] s
    100,000 alerts   [yours] s
    100 times more alerts took roughly [ratio] times longer. That is close to
    near-linear, nowhere near n squared (which would be 10,000 times longer).
    Improvements: skip the sort if alerts already arrive in time order; use a
    rolling window so one attack is not split at the 10 minute edge. Both keep
    the validation and the memory cap, so the security properties are unchanged.
    Limitation: closing the oldest group at the cap means a flood can force a real
    incident to close early and split in two.
    ```

## T17 Two tests of your own (15 min)

- [ ] `notepad test_alert_triage.py`. Paste at the very bottom, then save:
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
- [ ] Add **one more** of your own. Run again. Log what you added.
- [ ] Screenshot: `B3_my_tests.png`

## T18 Assembler: write and run a low-level check (25 min)

`size_check.asm` is the first check of Script A (reject empty, negative or over-size) written directly in MIPS assembler. It checks **both ends** of the range, because a one-sided "too big" test lets a negative length through (a classic integer bug).

- [ ] Go to the folder:
    ```
    cd ..\mips
    ```
- [ ] Run it with the practice simulator. You should see 6 lines:
    ```
    python mips_mini.py size_check.asm
    ```
    ```
    -1 REJECT
    0 REJECT
    1 ACCEPT
    65536 ACCEPT
    65537 REJECT
    2147483647 REJECT
    ```
- [ ] **Run it in the real tool, MARS** (it is on the software list). Open MARS. File, Open, choose `size_check.asm`. Run, Assemble (F3). Run, Go (F5). The output appears in the bottom pane. It should match.
- [ ] After F3, the **Text Segment** shows each instruction with its **machine code in hex**. Screenshot a few lines with the output pane: `C1_mars.png`
- [ ] **Change one thing, and predict first.** In `check_size`, change `li $t0, 65536` to `li $t0, 1000`. Write your prediction in the log (65536 should become REJECT). Run it. Did it match?
- [ ] Put it back to `65536`.
- [ ] Paste into the log:
    ```
    ASSEMBLER (low-level language)
    size_check.asm implements Script A's body-size rule in MIPS: a function
    (jal / jr), argument in $a0, result in $v0, reject by default, and a check at
    both ends of the range (blez for zero or negative, bgt for too big).
    Run in MARS (hex machine code shown after assembling) and in a Python
    simulator: identical output. Prediction test: [what I changed, what I
    predicted, what happened].
    ```

## T19 High-level to low-level (20 min)

The v4 table wants you to **map a high-level expression to its low-level code**. Take this line from Script A's logic: `0 < n <= 65536`.

- [ ] Go back to the validator folder: `cd ..\sync-validator`
- [ ] Show how Python reads it (syntax analysis). You should see a `Compare` node with ops `Lt` and `LtE`:
    ```
    python -c "import ast; print(ast.dump(ast.parse('0 < n <= 65536'), indent=1))"
    ```
- [ ] Show the bytecode it compiles to. Look for `LOAD_CONST`, `LOAD_NAME`, two `COMPARE_OP` lines and a jump (names vary a little between Python versions):
    ```
    python -c "import dis; dis.dis('0 < n <= 65536')"
    ```
- [ ] Screenshot both outputs: `C2_ast_bytecode.png`
- [ ] Paste into the log:
    ```
    HIGH-LEVEL TO LOW-LEVEL MAPPING
    Python source:   0 < n <= 65536   (accept only if both comparisons are true)
    Syntax tree:     one Compare node with two operators, Lt then LtE
    Python bytecode: loads 0 and n, COMPARE_OP <, a conditional jump, loads
                     65536, COMPARE_OP <=. Run by the Python virtual machine.
    MIPS assembler:  blez $a0 (reject if n <= 0), bgt $a0,$t0 (reject if n > 65536)
                     where $t0 holds 65536. Assembled by MARS to machine code.
    Translation:     source -> syntax tree -> bytecode -> executed by a virtual
                     machine (Python). Assembly -> machine code by an assembler
                     (MIPS). C would be compiled straight to machine code.
    Same logic, three levels. The assembler version is written "reject by
    default", the Python one "accept if true"; both reject the same inputs.
    ```

## T20 Save and tidy (10 min)

- [ ] Go back up: `cd ..`
- [ ] Your log is saved in `ex4-evidence`.
- [ ] Screenshots present: A1 to A9, B1 to B3, C1, C2. That is 14. You will crop and combine them onto **5 pages** on Friday.
- [ ] **Thursday is done.** Stop. Eat. Rest. Friday: open `EX4_START_HERE.md`, Friday section.

---

# FRIDAY

## F1 Setup (10 min)

- [ ] Open Command Prompt. Run:
    ```
    cd C:\path\to\EPA\ex4-defensive
    ```
- [ ] Open `ex4-evidence\log.txt` in Notepad. Check Thursday's work is all there.
- [ ] Open the v11 brief, the printed v4 pack, and the T2 table from Thursday (in this file).
- [ ] Remember: **only TC10 and TKU10 can earn Merit or Distinction.** F3 to F6 are where you earn it.

## F2 The nine secure programming pairs (10 min)

- [ ] Run:
    ```
    python -m pytest -v python
    ```
- [ ] You should see `9 passed`. Screenshot: `P1_nine_pairs.png`
- [ ] Open `python\vuln_examples.py`. Skim all nine. Each has a comment with the CWE (a standard number for the flaw type), the attack and the fix.

## F3 Vulnerability review table (40 min). This is the Merit and Distinction evidence.

TC10 **Merit** = identify *more subtle* vulnerabilities in code examples. **Distinction** = develop mitigations for them. This table does both: each row names the flaw, why it is subtle, how you showed it, and the fix.

- [ ] Paste into the log, then **tidy each row in your own words**:
    ```
    VULNERABILITY REVIEW (code examples reviewed: sync_validator.py and vuln_examples.py)

    Where        | Weakness (CWE)               | Why it is subtle                    | Mitigation                          | Evidence
    -------------+------------------------------+-------------------------------------+-------------------------------------+----------------------------
    Script A D1  | Input validation (CWE-20)    | Pattern looks right; $ allows a     | fullmatch                           | A2 screenshot, test passes
                 |                              | trailing newline                    |                                     |
    Script A D2  | Unicode handling (CWE-176,   | Valid JSON, only fails at storage   | _is_utf8_safe check                 | A3, A8 (fuzz)
                 | CWE-755)                     |                                     |                                     |
    Script A D3  | Uncontrolled recursion       | Under the size limit, so the size   | Catch RecursionError, reject        | A4, fuzz
                 | (CWE-674, CWE-248)           | check passes                        |                                     |
    Pair: file   | Path traversal (CWE-22)      | ../ escapes a "safe" folder         | realpath plus commonpath check      | P1 (test_path_traversal)
    Pair: SQL    | SQL injection (CWE-89)       | Works when input is "just a name"   | Parameterised query                 | P1 (test_sql_injection)
    Pair: command| OS command injection (CWE-78)| Shell reads ; as a new command      | No shell, argument list, validate   | P1 (test_command_injection)
    Pair: timing | Timing side channel (CWE-208)| == stops at first wrong byte,       | hmac.compare_digest                 | P1 (timing test)
                 |                              | leaking how close a guess is        |                                     |
    Pair: TOCTOU | Race condition (CWE-367)     | Safe at the check, unsafe at the    | Open once, O_EXCL, no symlinks      | P1 (test_toctou)
                 |                              | use                                 |                                     |
    Pair: hash   | Weak password hash (CWE-916) | Hashing looks like protection       | Salt plus slow KDF (scrypt)         | P1 (test_password_hashing)
    Pair: pickle | Unsafe deserialisation       | Loading data runs code              | Safe format (JSON), never pickle    | P1 (test_deserialisation)
                 | (CWE-502)                    |                                     | untrusted data                      |
    Pair: token  | Predictable token (CWE-338)  | Looks random but is seeded          | secrets module                      | P1 (test_predictable_token)
    Pair: XSS    | Cross-site scripting (CWE-79)| Output is trusted by the browser    | Encode output (html.escape)         | P1 (test_xss)
    ```
- [ ] Add one line under it:
    ```
    Why these matter for the company: [pick the two or three that matter most to the
    case study, for example input from staff devices reaching the sync API, and
    say what an attacker or a bad device could do with each].
    ```
- [ ] **Optional, only if you have Linux or WSL with gcc (not needed for a pass):** the C examples in `c-debug` show memory corruption, the malware technique the v4 table names. Run `make`, then `valgrind --leak-check=full ./memory_bugs 2` and see `Invalid read of size 4` (use-after-free, CWE-416). Add a row for it.

## F4 Principles and secure design patterns (15 min)

- [ ] Paste into the log, then edit in your own words:
    ```
    SECURE PROGRAMMING PRINCIPLES (Script A and Ex1 sync.php)
    Allow-list (default deny): only explicitly allowed input passes.
    Defence in depth: size limit, parse, schema, character set, date window
      (Script A), then token and scope check and parameterised SQL (Ex1).
    Least privilege: read and write tokens are separate scopes (Ex1).
    Least information: errors name the field, never the input
      (test_security_error_never_echoes_input).
    Sanitisation and validation at the boundary: one entry point, validate().
    Sensitive data: tokens stored only as hashes (Ex1); note text is never put in
      an error message or a log line.

    SECURE DESIGN PATTERNS USED
    Validation gateway: all input passes through one function before use.
    Fail closed: any problem raises an error; nothing partial is returned.
    Parse, don't pass through: the function returns a clean new dictionary, not
      the raw input.
    Resource limits: body size, field length, nesting depth, group cap.
    Opaque errors: the client learns which field failed and nothing else.
    How these reduce the company's risks: [link each to a case study risk, for
    example validation gateway and resource limits to [the case study risks]].
    ```

## F5 Compiler and interpreter features, static and dynamic analysis (15 min)

- [ ] Run Python in developer mode with warnings treated as errors. You should see `31 passed` (or 34 with your own tests):
    ```
    python -X dev -W error -m pytest -q sync-validator\test_sync_validator.py
    ```
  Screenshot: `P2_dev_mode.png`
- [ ] Paste into the log:
    ```
    COMPILER AND INTERPRETER FEATURES THAT SUPPORT SECURE CODE
    Python: -X dev (extra runtime checks) and -W error (warnings become errors)
      catch unclosed files, bad escapes and deprecated calls. Ran the tests this way: pass.
    C (gcc): -Wall -Wextra warn about risky code; -fstack-protector-strong puts a
      canary on the stack to detect overwrites; -D_FORTIFY_SOURCE=2 checks sizes in
      string and memory functions; -fPIE -pie lets the OS randomise the program's
      address (ASLR); -Wl,-z,relro,-z,now and -Wl,-z,noexecstack harden the loader and
      mark the stack non-executable; -fsanitize=address,undefined finds memory bugs at run time.
    Visual C++: /GS (buffer security check), /DYNAMICBASE (ASLR), /NXCOMPAT (no execute), /guard:cf.
    Why they matter: they turn a silent memory corruption into a clear stop.

    STATIC ANALYSIS (code not run): bandit on sync_validator.py and validate_file.py: no issues.
    DYNAMIC ANALYSIS (code run): unit tests (31), fuzzing (20,000 requests), Python dev mode.
      For C, Valgrind and AddressSanitizer.
    ```
- [ ] **Optional (Linux or WSL):** `gcc -O2 -fstack-protector-strong -D_FORTIFY_SOURCE=2 -o hard c-debug/memory_bugs.c`, then `./hard 6`. It stops with `*** buffer overflow detected ***: terminated`. The plain build (`-fno-stack-protector`) overflows silently. Screenshot if done.

## F6 Sources and one formal method (25 min)

- [ ] Open owasp.org and check the OWASP Top 10 category numbers. At the time of writing the current edition is **OWASP Top 10:2025** (final January 2026). **Check the numbers on the site before you rely on them.**
- [ ] Paste into the log:
    ```
    SOURCES OF SECURE PROGRAMMING PRACTICE APPLIED
    OWASP Top 10:2025: Injection (SQL and command injection pairs, D1);
      Mishandling of Exceptional Conditions (D2 and D3: crashes on unusual input);
      Broken Access Control and Authentication Failures (token scope in Ex1).
    OWASP ASVS and the OWASP Input Validation Cheat Sheet: allow-list validation,
      validate on the server side, limit size, canonicalise before validating.
    SEI CERT C Coding Standard: memory rules behind the C examples (bounds,
      use-after-free, double free).
    NCSC secure development and deployment guidance: security at every lifecycle stage.
    CWE: the standard names used in the vulnerability review.
    Organisational coding standard (what I applied): allow-list, fail closed,
      opaque errors, resource limits, no eval or pickle, tests for every rule.
    ```
- [ ] Paste the formal method:
    ```
    FORMAL METHOD: CSP (Communicating Sequential Processes)
    What it is: a process algebra (C.A.R. Hoare) that describes systems as processes
    that communicate by events, and proves properties about every possible sequence
    of events using a model checker such as FDR.
    Small model of the validator gate:
      GATE = request.valid -> store -> GATE  []  request.invalid -> reject -> GATE
    Security property: "nothing is stored unless the request was valid".
    Check: assert SAFE [T= GATE (trace refinement: every behaviour of GATE is allowed by SAFE).
    Strengths: covers ALL behaviours of the model, not just the ones I tested; finds
      deadlocks, races and replay or duplicate-store errors in the whole sync flow
      (device, network, retries); forces a precise statement of the security property.
    Weaknesses: it checks the model, not the Python code, so a wrong model proves
      nothing; large systems cause state explosion; needs specialist skill and tools;
      it does not see low-level issues such as timing leaks unless modelled.
    Link to my work: the sequential counterpart is a pre- and post-condition on
      validate(): given bytes, it returns a dict whose IDs match the pattern and whose
      note can be stored as UTF-8, or it raises ValidationError. My fuzz script checks
      that post-condition on 20,000 inputs; a formal proof would cover all inputs.
    ```

## F7 System description, lifecycle and methodology (35 min)

TC11 wants a **system description** (people, culture, technology, process, environment) and a **methodology that covers the whole lifecycle**. TKU11 wants sequential versus agile compared.

- [ ] Paste into the log and fill every `[ ]` from your case study:
    ```
    SYSTEM OF INTEREST: [name your system of interest]
    People:      [who uses and runs it: roles, numbers, skills]
    Culture:     [how they work: time pressure, workarounds, trust, training]
    Technology:  [devices, cloud service, API, local cache, my two scripts]
    Process:     [visit, write note, cache, sync, review, incident response, joiners and leavers]
    Environment: [networks in the field, law and regulation, funding, suppliers]
    Security aspects found from this description: [one per row, for example:
      people: lost or shared devices; process: cached records not wiped; ...]

    DATA FLOW AND TRUST BOUNDARIES
      [Staff device + local cache] --TLS--> [Sync API + validator] --SQL--> [Records database]
       boundary 1: device to network       boundary 2: API to database
      [Alert sources] --> [Alert triage] --> [Analyst]
    ```
- [ ] Paste the methodology:
    ```
    METHODOLOGY CHOSEN: [Agile with security gates, or V-model, or other. Pick ONE]
    Why: [link to the case study: changing requirements, rollout in stages,
    regulatory evidence needed].

    SEQUENTIAL VERSUS ITERATIVE
    Waterfall / V-model (sequential): + clear stages, full documentation, easy audit
      trail, suits fixed requirements; - late feedback, costly change.
    Agile (iterative): + early feedback, copes with change, security re-checked every
      cycle; - lighter documentation, security tasks can be skipped under time
      pressure unless they are in the "definition of done".
    Secure SDLC (for example NCSC or Microsoft SDL): adds security activities to every stage.
    Context decides: [one sentence on why my choice suits this case study].

    WHOLE LIFECYCLE
    Meeting a need:  [the case study risks become security requirements and acceptance tests]
    Design:          [data flow diagram, trust boundaries, threat model]
    Trade-offs:      [strict validation versus staff usability; fixed memory cap versus losing low-score alerts]
    Implementation:  [Python scripts, Git for version control, code review]
    Deployment:      [how the validator sits in front of the API; configuration and token handling]
    Support:         [monitoring with Script B, patching, incident response]
    Evolution:       [rolling window; more checks as new attacks appear; every change re-runs the tests]
    Validation:      [are we building the right thing? checks with users and the case study needs]
    Verification:    [are we building it right? 31 tests, 20,000 fuzz requests, bandit]
    Assurance:       [evidence the system meets its security objectives: this log, test results]

    TOOLS BY STAGE
    Requirements: user stories and abuse cases.   Design: data flow diagram, STRIDE.
    Build: Python, Notepad or an editor, Git.     Test: pytest, fuzz script, bandit, MARS.
    Deploy and maintain: configuration, token revocation, Script B monitoring.
    ```

## F8 Gather the evidence into one document (25 min)

- [ ] Open Word. Save as `Ex4_YourName.docx`.
- [ ] Add these headings: **Justification**, **Script A**, **Script B**, **Low-level and language levels**, **Secure programming and methodology**, **Screenshots (5 pages)**, **Appendix: code**.
- [ ] Under each heading, paste the matching log text. Tidy it. Keep the tables readable (use a code font such as Consolas, 8 pt).
- [ ] **Screenshot pages (maximum 5 pages of A4).** Crop each tight. Resize and arrange like this:

| Page | Screenshots |
| --- | --- |
| 1 | A1 tests pass, A2 D1, A3 D2, A4 D3, A5 all fixed |
| 2 | A6 bandit, A7 fuzz clean, A8 fuzz finds D2, A9 command-line tool |
| 3 | B1 Script B tests, B2 timing, B3 my own tests |
| 4 | C1 MARS, C2 syntax tree and bytecode |
| 5 | P1 nine pairs, P2 dev mode (and any optional C screenshot) |

- [ ] Appendix: paste `sync_validator.py`, `alert_triage.py` and `size_check.asm` in a small code font. **Check your live brief to see whether code must be included.**

## BREAK 12:30 to 13:00

Eat. Leave the screen.

## F9 The justification (90 min)

**Target 1,000 words. Allowed 900 to 1,100.** Count only the justification text. Your tables are the supporting notes (v4 calls them "screenshots and or associated data that may contribute to the written justification"). Check your live brief if unsure.

Your method (agreed with your assessor): a draft prepared **before** the test, rewritten in your own words from your own evidence. No AI during test hours.

- [ ] Open your prepared draft or outline (made before the test). A prepared draft is in `justification_draft.md` in this folder: read its "Fix these in your log" list first. If you have none, write from the starter sentences below.
- [ ] Fill every blank from your own log: your numbers, your defects, your tests. Then **rewrite** each sentence in your own words.

| Section | Words | What goes in it |
| --- | --- | --- |
| 1 Why these components | 150 | Link to the company's risks. Why Python. What the two scripts and the assembler are for |
| 2 Script A and the languages | 200 | What it checks and why; high-level, scripting (CLI) and assembler; the three levels of the same check |
| 3 Secure programming | 200 | D1 to D3, why subtle, the fixes, the fuzzer; two or three pairs; principles and patterns; OWASP; the formal method in one sentence |
| 4 Script B and the algorithm | 200 | The algorithm; two approaches; complexity; your timings; the flood defence; one limitation |
| 5 Methodology and lifecycle | 150 | Your chosen model, why, sequential versus agile in two sentences, security at each stage |
| 6 Limits, next steps, AI | 100 | What you did not test; next steps; the AI reference line |

Starter sentences:
> 1: "The case study lists [the case study risks] and alert fatigue. I chose ... because ..."
> 2: "Script A refuses everything not explicitly allowed. The same size rule exists at three levels: Python, bytecode and MIPS assembler, which I mapped ..."
> 3: "My review found three subtle defects. [D1] looked correct because ... I found [D3] when ... I fixed it by ... and retested. A fuzzer ran 20,000 requests ..."
> 4: "I compared two approaches. Comparing every pair would take about n squared steps ... My timings of [x], [y] and [z] seconds show ..."
> 5: "I chose [model] because ... Compared with [other model], it ... Security activities at each stage were ..."
> 6: "These are prototypes. I did not test ... Next I would ..."

- [ ] Add the AI reference line at the end:
  > "AI assistance (Claude) was used before the test to prepare starter code and an outline. During the test I ran, tested, debugged and reviewed all code, and wrote this text from my own evidence."

## F10 Check against the v4 table (20 min)

- [ ] Open the printed v4 pack at the Ex4 rows. For each row, write beside it **where in your document** the evidence is. Tick when found.

| Row | Evidence in my document | Done |
| --- | --- | --- |
| TC6 high-level program to a specification | Script A, tests | [ ] |
| TC6 map high-level to low-level | T19 mapping, MARS machine code | [ ] |
| TC6 assembler solution | `size_check.asm`, MARS screenshot, prediction test | [ ] |
| TC6 scripting solution | `validate_file.py` | [ ] |
| TC6 variety of programming styles | Procedural, exception classes, functional-style (predicate, sort key, heap), assembler | [ ] |
| TC7 design, implement, analyse an algorithm | Script B, definition, two approaches, complexity, timings | [ ] |
| TC10 pass: apply principles, patterns, with evidence | F4, defects, tests | [ ] |
| TC10 merit: more subtle vulnerabilities | F3 table, D1 to D3, fuzzing | [ ] |
| TC10 distinction: mitigations | F3 mitigation column, retests | [ ] |
| TC11 methodology, lifecycle, system description | F7 | [ ] |
| TKU6 languages and translation | T19 | [ ] |
| TKU7 algorithms, complexity, discrete maths | T13 | [ ] |
| TKU10 defensive programming, patterns, compiler features, static and dynamic analysis, OWASP/CERT, formal method | F4 to F6, T6, T7 | [ ] |
| TKU11 lifecycle, sequential versus agile, tools | F7 | [ ] |

- [ ] Any row blank? Add a line or a screenshot.

## F11 Final checks (10 min)

- [ ] Justification word count 900 to 1,100
- [ ] AI use referenced
- [ ] Screenshots: no more than 5 pages, cropped
- [ ] The three defects, fixes and retests are clear
- [ ] Your own tests are listed
- [ ] Your name or learner number is on it (check what the brief asks for)
- [ ] File name sensible. Saved as **PDF** too, if the upload accepts it
- [ ] Break emails: check your live brief for whether they are needed

## F12 Upload (15 min)

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
| T5: no failure after your edit | You did not save the file. Save (Ctrl+S) and re-run. |
| `bandit` is not recognised | Use `python -m bandit -r sync_validator.py validate_file.py` |
| `validate_file` says `REJECTED: created_at` for the good sample | Open `samples\good.json` and change the date to today (it must be within 30 days). |
| MARS will not open | Run `java -jar Mars.jar` from its folder, or use `python mips_mini.py size_check.asm` and say in the log that MARS was unavailable. |
| Timing numbers differ from the example | Normal. Use your own. |
| Bytecode output looks different | Normal. Python versions differ. Look for the `COMPARE_OP` lines and a jump. |
| Word count too high or low | See F9. Cut the weakest sentence from each section, or add one example. |
| Panicking | Stand up. Water. Say the next step aloud. |

## Questions an assessor might ask (have a short answer ready)

1. **Why reject by default?** Because anything I forgot to think of is then blocked, not allowed.
2. **Tell me about one defect you found.** D1: `$` let a trailing newline through. A test caught it. I fixed it with `fullmatch` and retested. D3 is more interesting: the size check passed but deep nesting crashed the parser.
3. **Why a dictionary in Script B?** One lookup per alert, so it scales. Comparing every pair is n squared.
4. **What stops an alert flood using all the memory?** The open-group cap closes the oldest group, and only the top 100 incidents are kept.
5. **Why write a check in assembler?** To show I understand the low-level view: the same rule at three levels, and the classic negative-number bug that a one-sided check misses.
6. **What can a formal method give you that tests cannot?** A proof over every behaviour of the model. Its weakness is that it proves the model, not the code.
7. **What did these tests not cover?** Real network attacks, real data, integration with the live API, and the controls outside code (encryption, segmentation). They are unit tests and a fuzzer.
8. **How did you use AI?** Starter code and notes, prepared before the test. I ran and tested everything, reproduced each defect myself, added my own tests, and wrote the evidence and text from my own work.
