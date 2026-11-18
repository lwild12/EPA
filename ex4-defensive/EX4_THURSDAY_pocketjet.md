# Ex4 Thursday: PocketJet tick-list

Everything for today is on these pages. Tick each box. One small step at a time. Folder: `ex4-defensive`. Full guide for both days: `EX4_START_HERE.md`.

**Rules**

1. 15 minutes over a box? Stop. Move on. Come back at the end.
2. Screenshot straight after each step. Windows key + Shift + S. Save into the Desktop folder `ex4-evidence`.
3. A test fails? That is the process working. Note what failed, why, and what you changed.
4. Check your live brief for test-hour and break rules. Submission is Friday, not today.

**Schedule (09:30 to 15:30)**

| Task | Mins | Clock | Done |
| --- | --- | --- | --- |
| T1 Setup | 15 | 09:30 | ☐ |
| T2 Read brief and v4 table | 15 | 09:45 | ☐ |
| T3 Log: Script A problem and spec | 20 | 10:00 | ☐ |
| T4 Run Script A tests | 10 | 10:20 | ☐ |
| T5 Bug: show, fix, retest | 20 | 10:30 | ☐ |
| T6 Static scan | 10 | 10:50 | ☐ |
| T7 Understand Script A | 30 | 11:00 | ☐ |
| T8 Test table, link to Ex1 | 15 | 11:30 | ☐ |
| T9 Three tests of your own | 30 | 11:45 | ☐ |
| Spare | 15 | 12:15 | ☐ |
| **Break** | 30 | 12:30 | ☐ |
| T10 Script B: problem, definition | 30 | 13:00 | ☐ |
| T11 Two approaches | 10 | 13:30 | ☐ |
| T12 Run Script B tests | 10 | 13:40 | ☐ |
| T13 Understand Script B | 30 | 13:50 | ☐ |
| T14 Time it | 15 | 14:20 | ☐ |
| T15 Two tests of your own | 20 | 14:35 | ☐ |
| T16 Save and tidy | 15 | 14:55 | ☐ |
| Spare, then stop | 20 | 15:10 | ☐ |

Behind? Cut in this order: T9 extra test, T15 extra test, T8 Ex1 link. **Never cut:** T5 (bug and retest), T10 (definition) and the screenshots.

**Stuck?** Stand up. Water. Say aloud: "The next step is ____." Write one rough line. Move on.

## T1 Setup (15)

☐ Open Command Prompt (Windows key, type `cmd`, Enter).

☐ Go to the repo (change the path):
```
cd C:\path\to\EPA\ex4-defensive
```

☐ Get the latest files. See `Already up to date` or new files:
```
git pull
```

☐ Check Python. See `Python 3.x`. If it errors, try `py --version` and use `py` for every command today:
```
python --version
```

☐ Install tools. See `Successfully installed` or `already satisfied`:
```
pip install pytest bandit
```

☐ On the Desktop make a folder `ex4-evidence`. Screenshots go here.

☐ In Notepad save `ex4-evidence\log.txt`. Paste this at the top:
```
EX4 LOG

NOTE ON AI USE: The starter code for both scripts was drafted with AI
assistance (Claude). I ran, tested, debugged and reviewed it myself.
```

## T2 Read the brief (15)

☐ Open the v11 brief at Exercise 4. Read the five circle bullets.

☐ Open the printed v4 pack at the Ex4 table.

☐ Anything the v4 table wants that is not in this sheet? Log it under `EXTRA FROM V4`.

## T3 Log: Script A problem and spec (20)

☐ Paste, and fill the blank from your case study:
```
SCRIPT A PROBLEM
The company's sync API takes visit notes from staff devices. A weak or
unchecked request could store bad data or leak patient records. I built a
validator that rejects bad requests before they reach the database.
Risks from the case study this addresses: [fill in]
```

☐ Paste the spec:
```
SCRIPT A SPEC
client_id, staff_id, patient_ref: text, 1-64 chars, letters digits _ - only
note_text: text, 1-20,000 chars, not blank, no control characters
created_at: valid date, max 5 min in future, max 30 days old
whole request: valid JSON object, max 64 KB
extra fields: rejected.  duplicate JSON keys: rejected.
Input:  raw request body (bytes)
Output: clean dictionary, or an error naming only the bad field
Rule:   reject everything unless explicitly allowed
Order:  cheapest checks first (size, JSON, then fields)
```

## T4 Run Script A tests (10)

☐ Go into the folder:
```
cd sync-validator
```

☐ Run. See 28 lines ending `PASSED`, then `28 passed`:
```
python -m pytest -v
```

☐ Screenshot: `A1_tests_pass.png`

## T5 Bug: show, fix, retest (20)

The first draft let an ID ending in a newline through (Python `$` matches before a trailing newline). Fix: `fullmatch`.

☐ Open the file:
```
notepad sync_validator.py
```

☐ Ctrl+F `fullmatch`. Find this line:
```
if not ID_PATTERN.fullmatch(data[name]):
```

☐ Change `fullmatch` to `match`. Save (Ctrl+S).

☐ Run. See `1 failed, 27 passed`, failing `test_security_trailing_newline_in_id`:
```
python -m pytest -q
```

☐ Screenshot: `A2_bug_found.png`

☐ Change `match` back to `fullmatch`. Save.

☐ Run again. See `28 passed`:
```
python -m pytest -q
```

☐ Screenshot: `A3_fixed_retest.png`

☐ Paste into the log:
```
BUG FOUND AND FIXED
Defect: ID_PATTERN.match with "$" accepts an ID with a trailing newline.
Found by: test_security_trailing_newline_in_id (1 failed, 27 passed).
Why it matters: a newline in an ID could split log lines or bypass filters.
Fix: use fullmatch so the whole string must match.
Retest: 28 passed. No other test affected.
```

File messed up? Restore it: `git checkout -- sync_validator.py`

## T6 Static scan (10)

☐ Run. See `No issues identified.`:
```
python -m bandit -r sync_validator.py
```

☐ Screenshot: `A4_bandit.png`

☐ Log: `Static analysis (bandit) found no issues in Script A.`

## T7 Understand Script A (30)

☐ Open `sync_validator.py` in Notepad. For each row, write **one sentence in your own words** in the log under `SCRIPT A: MY UNDERSTANDING`.

| Code | Plain English |
| --- | --- |
| `MAX_BODY`, `FIELDS` | The limits: 64 KB total, a maximum length per field |
| `ValidationError` | Carries only a field name, never what the user sent, so nothing leaks |
| `_no_duplicate_keys` | Rejects a repeated key, so two checks can't see different values |
| `_parse_date` | Real date, not over 5 min ahead, not over 30 days old |
| `validate` step 1 | Check size first so a huge body can't tie up the server |
| step 2 | Parse JSON. Broken or invalid text is rejected |
| step 3 | Exactly the expected fields. No extras like `is_admin`, none missing |
| step 4 | Each field is text, not blank, not too long |
| step 5 | IDs use safe characters only. No control characters in notes |
| step 6 | Final date check |

## T8 Test table and Ex1 link (15)

☐ Paste into the log:
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

Link to Ex1: this validator applies the same rules as my Ex1 sync.php
prototype (field limits, 64 KB body, type checks) and adds a date window,
strict ID patterns, control character checks and duplicate key rejection.
```

## T9 Three tests of your own (30)

☐ `notepad test_sync_validator.py`. Scroll to the very bottom. Paste, then save:
```python
# ---------- MY OWN TESTS ----------
def test_mine_unicode_lookalike_in_id():
    rejects(good(client_id="dev\u0430\u0432"), "client_id")


def test_mine_emoji_in_note_is_allowed():
    assert validate(good(note_text="Patient happy \U0001F600"), now=NOW)


def test_mine_empty_json_object():
    rejects(b"{}", "missing_field")
```

☐ Run. See `31 passed`:
```
python -m pytest -q
```

☐ Invent **one more** nasty request of your own. Add it the same way. Run again.

☐ Screenshot: `A5_my_tests.png`

☐ Log: `I added [N] tests of my own: [list]. Result: [result].`

**Spare 15 min. Then BREAK 12:30 to 13:00. Eat. Leave the screen.**

## T10 Script B: problem, definition (30)

☐ Go to the other folder:
```
cd ..\alert-triage
```

☐ Paste into the log (fill the blank):
```
SCRIPT B PROBLEM
The case study lists alert fatigue as a risk. Repeated alerts bury the real
incidents. I built an algorithm that groups duplicates and ranks what is left.
```

☐ Paste the definition (the brief wants it before the code):
```
ALGORITHM DEFINITION
Input:   list of alerts: source, type, asset, severity (1-5), time (seconds)
Output:  top 100 incidents ranked by score, plus a count of rejected alerts
Group:   same (source, type, asset) within 10 min of the group's first alert
Score:   severity x asset criticality x log(count + 1)
         criticality: patient-db 5, sync-api 4, laptop 2, anything else 1
Assumptions: timestamps are trusted; the criticality table is kept up to date
Constraint:  cope with 10,000 alerts a minute and a deliberate flood

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

## T11 Two approaches (10)

☐ Paste into the log:
```
ALTERNATIVES
A. Compare every alert with every other alert: O(n squared). At 100,000
   alerts that is about 10 billion comparisons. Far too slow.
B. Dictionary keyed by group (chosen): one lookup per alert. The time sort is
   the slowest step, so overall O(n log n). Memory is capped by
   MAX_OPEN_GROUPS (50,000) plus TOP_N (100).
Weakness of B: an attacker can send many unique alerts to try to use up
memory. Defence: at the limit, the oldest open group is closed.
```

## T12 Run Script B tests (10)

☐ Run. See 16 lines ending `PASSED`, then `16 passed`:
```
python -m pytest -v
```

☐ Screenshot: `B1_tests_pass.png`

☐ Paste into the log:
```
SCRIPT B TEST SUMMARY (16 tests)
Normal (3)    3 identical alerts become 1 incident; patient-db ranks above
              laptop; unsorted input still works
Boundary (5)  empty list; single alert; exactly 600 s is one incident; 601 s
              is two; severity 1 and 5 accepted
Error (4)     severity 0 and 9; missing field; NaN and text times; non-dict items
Security (4)  severity as string; boolean severity; 1 MB asset name; a flood of
              20,000 unique alerts stays under 60 MB, returns only 50 incidents
```

## T13 Understand Script B (30)

☐ Open `alert_triage.py` in Notepad. One sentence per row, your own words, in the log under `SCRIPT B: MY UNDERSTANDING`.

| Code | Plain English |
| --- | --- |
| `_valid` | Throws out malformed alerts: wrong type, severity outside 1 to 5, text too long, bad time |
| `_score` | Severity x asset importance x a number that grows slowly with the count |
| `good.sort` | Puts alerts in time order. The slowest step |
| `open_groups` | Dictionary. Key is (source, type, asset). Value is the group being built |
| window check | More than 10 min after the group's first alert: close it, start a new one |
| `max_open` check | Flood defence: too many open groups, close the oldest so memory can't grow without limit |
| `best` and `heapq` | Keeps only the top 100 incidents, so memory stays small |

## T14 Time it (15)

☐ Run. See three lines (your numbers will differ):
```
python timing.py
```
Example: `1000 alerts: 0.002 s`, `10000: 0.018 s`, `100000: 0.146 s`

☐ Screenshot: `B2_timing.png`

☐ Paste into the log with **your own numbers** (ratio = the 100,000 time divided by the 1,000 time):
```
TIMING
1,000 alerts     [yours] s
10,000 alerts    [yours] s
100,000 alerts   [yours] s
100 times more alerts took roughly [ratio] times longer. That is close to
n log n, not n squared (10,000 times longer). 10,000 alerts a minute is
met easily.
Improvements: skip the sort if alerts already arrive in time order; use a
rolling window so one attack is not split at the 10 minute edge.
```

## T15 Two tests of your own (20)

☐ `notepad test_alert_triage.py`. Paste at the very bottom, then save:
```python
# ---------- MY OWN TESTS ----------
def test_mine_two_assets_do_not_merge():
    out = triage([alert(0, asset="laptop"), alert(1, asset="patient-db")])
    assert len(out["incidents"]) == 2


def test_mine_highest_severity_is_kept():
    out = triage([alert(0, severity=2), alert(5, severity=5)])
    assert out["incidents"][0]["severity"] == 5
```

☐ Run. See `18 passed`:
```
python -m pytest -q
```

☐ Invent **one more** of your own. Add it. Run again.

☐ Screenshot: `B3_my_tests.png`

☐ Log what you added.

## T16 Save and tidy (15)

☐ Go back up: `cd ..`

☐ Log is saved in `ex4-evidence`.

☐ Screenshots present: A1, A2, A3, A4, A5, B1, B2, B3.

☐ Optional, save your tests to the repo:
```
git add sync-validator alert-triage
git commit -m "Ex4: my own tests"
git push
```

☐ **Thursday is done.** Stop. Eat. Rest. Friday: open `EX4_START_HERE.md`.

## If it goes wrong

| You see | Do |
| --- | --- |
| `'python' is not recognized` | Use `py` instead. Else install Python, tick "Add to PATH" |
| `No module named pytest` | `python -m pip install pytest` |
| `No module named sync_validator` | Wrong folder. `dir` must show `sync_validator.py` |
| Tests fail at T4 | You edited a file by accident: `git checkout -- .` |
| No failure at T5 | You didn't save. Ctrl+S, re-run |
| `bandit` not found | `python -m bandit -r sync_validator.py` |
| `git pull` complains | `git stash`, `git pull`, `git stash pop` |
