## Appendix: `sync.php` explained

You do not need to know PHP well. Read this once, then open `sync.php` beside it.

**PHP basics you need**

- PHP code sits between `<?php` and the end of the file. Everything runs top to bottom on each request.
- `$name` is a variable. `$d['note_text']` is the item called `note_text` in the array `$d`.
- `[...]` is a list or a lookup table (an array). `=>` pairs a name with a value.
- `;` ends a statement. `//` starts a comment.
- `function name(...) { ... }` defines a reusable block. `const X = 5;` defines a fixed value.
- `if (...) { ... }` runs code only when the test is true. `!` means "not". `===` means "exactly equal".
- `exit;` stops the script. `require` pulls in another file.

**What the file does, in order**

| Block | What it does | Why it matters |
| --- | --- | --- |
| `declare(strict_types=1)` | Makes PHP strict about types (text versus number) | Fewer surprises from wrong types |
| `const MAX_BODY`, `REQUIRE_HTTPS` | Settings at the top | Easy to change. HTTPS is switched on later (topic 5) |
| `ini_set('display_errors','0')` | Hides PHP error messages from the browser | No stack traces leaked (test 7) |
| `respond(code, body)` | Sets the status code, prints JSON, stops | One place that answers every request |
| `set_exception_handler(...)` | If anything crashes, send a plain 500 and log only the error type | No SQL or note text in errors or logs |
| Method check | Anything but POST gets 405 | Test 8 |
| Authenticate | Reads the `Authorization: Bearer ...` header, hashes the token with SHA-256, looks the hash up in `api_tokens` | Tokens are never stored. A stolen database does not give working tokens. 401 if missing, unknown, expired or revoked (tests 3 and 4) |
| Authorise | Token must have the `write` scope, otherwise 403 | Test 5. Logged in is not the same as allowed |
| Validate | Reads at most 64 KB, decodes the JSON, checks each field is text, not empty and not too long, and that the date parses | Tests 6, 7, 9. 400 for bad input, 413 for too large |
| Store once | Inserts the note with a prepared statement. If `client_id` already exists the database refuses it and we answer 200 | Test 2. Safe to repeat |
| Final `respond(201,...)` | Acknowledges a new note | Test 1 |

**The three ideas to be able to explain**

1. **Prepared statements.** The line `INSERT INTO notes (...) VALUES (?, ?, ?, ?, ?)` has `?` placeholders. The values are sent separately, so the database never treats them as SQL. That is what stops `' OR 1=1 --` (test 10) and what SQLMap will probe.
2. **Hash the token.** `hash('sha256', $token)` turns the token into a fixed fingerprint. We compare fingerprints, never tokens.
3. **Idempotent sync.** The unique `client_id` column makes the database reject a second copy, which is how a dropped mobile connection can safely retry.

**Things to say if a marker asks "what would you improve?"**

- Add HTTPS only (`REQUIRE_HTTPS`), then retest.
- Rate-limit requests per token, so a leaked token or a loop cannot flood the database.
- Add an audit log of who synced what, without storing note text in it.
- Encrypt `note_text` at rest, and keep the key outside the database.

**Try it and break it (your findings, not mine)**

- Change one thing, re-run `test_sync.sh`, and see which test fails. That shows you what each line does.
- For example, remove the `trim(...)` check and send a note of spaces only.
