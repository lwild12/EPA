# Prototype (topics 2 and 4)

Visit-note sync endpoint, version 1, built to the Part B spec (2a).

| File | Purpose |
| --- | --- |
| `schema.sql` | Creates the database, `notes` (unique `client_id`) and `api_tokens` (SHA-256 hashes only) |
| `db.php` | PDO connection (XAMPP defaults; override with `DB_DSN`, `DB_USER`, `DB_PASS`) |
| `make_token.php` | `php make_token.php <label> <write\|read>` prints a token once and stores its hash |
| `sync.php` | The endpoint: POST only, bearer token, scope check, validation, store once |
| `test_sync.sh` | Runs the 10 spec tests (2c) and prints PASS/FAIL with actual status codes |

## Run it (XAMPP)

1. Start Apache and MySQL. Put this folder under `htdocs`.
2. Import `schema.sql`.
3. `php make_token.php clinician write` and `php make_token.php auditor read`. Save both tokens.
4. `URL=http://localhost/prototype/sync.php TOKEN_OK=<write> TOKEN_READONLY=<read> bash test_sync.sh`

## Notes

- `REQUIRE_HTTPS` in `sync.php` is `false` on purpose. Turn it on in topic 5 once TLS works, then retest.
- Version 1 passed all 10 tests against SQLite on PHP 8.3. It has not been run on MySQL or attacked with Burp or SQLMap yet. Any finding there is yours to record.
- Only test your own system on your own machine.
