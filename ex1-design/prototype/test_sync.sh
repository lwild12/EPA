#!/usr/bin/env bash
# Runs the 10 tests from the spec table (2c) against YOUR sync endpoint.
# Usage:
#   URL=http://localhost/sync.php TOKEN_OK=<write-scope token> TOKEN_READONLY=<token without write scope> bash test_sync.sh
# Prints actual status codes so you can paste them into the "Actual" column.
# Only run against your own system on your own machine.
set -u
URL=${URL:-http://localhost/sync.php}
TOKEN_OK=${TOKEN_OK:?set TOKEN_OK}
TOKEN_READONLY=${TOKEN_READONLY:-}
ID1="test-$(date +%s)-a"

note() {  # $1=client_id  $2=note_text  $3=patient_ref
  printf '{"client_id":"%s","staff_id":"s1","patient_ref":"%s","note_text":"%s","created_at":"2026-11-10T09:00:00Z"}' "$1" "${3:-P123}" "$2"
}
req() {   # $1=label $2=expected $3...=curl args
  local label=$1 expect=$2; shift 2
  local out code
  out=$(curl -s -o /tmp/sync_body.$$ -w '%{http_code}' "$@" "$URL"); code=$out
  local verdict="FAIL"; case " $expect " in *" $code "*) verdict="PASS";; esac
  printf '%-3s | expect %-8s | got %-3s | %s\n' "$verdict" "$expect" "$code" "$label"
  # leak check: stack traces / SQL in body
  if grep -qiE 'stack trace|PDOException|mysqli|SQLSTATE|Fatal error|syntax to use' /tmp/sync_body.$$; then
    echo "     ^ WARNING: response body leaks an error/SQL detail"
  fi
}
H=(-H 'Content-Type: application/json')
AUTH=(-H "Authorization: Bearer $TOKEN_OK")

req "1  valid note, valid token"        "201"     -X POST "${H[@]}" "${AUTH[@]}" -d "$(note "$ID1" 'visit note')"
req "2  same note again (idempotent)"   "200"     -X POST "${H[@]}" "${AUTH[@]}" -d "$(note "$ID1" 'visit note')"
req "3  no token"                       "401"     -X POST "${H[@]}" -d "$(note x1 'n')"
req "4  wrong token"                    "401"     -X POST "${H[@]}" -H 'Authorization: Bearer not-a-real-token' -d "$(note x2 'n')"
if [ -n "$TOKEN_READONLY" ]; then
req "5  token without write scope"      "403"     -X POST "${H[@]}" -H "Authorization: Bearer $TOKEN_READONLY" -d "$(note x3 'n')"
else echo "SKIP| 5  (set TOKEN_READONLY to run)"; fi
req "6  empty note_text"                "400"     -X POST "${H[@]}" "${AUTH[@]}" -d "$(note x4 '')"
req "7  invalid JSON"                   "400"     -X POST "${H[@]}" "${AUTH[@]}" -d '{not json'
req "8  GET instead of POST"            "405"     -X GET "${AUTH[@]}"
BIG=$(head -c 3000000 /dev/zero | tr '\0' 'A')
req "9  very large note_text (3 MB)"    "400 413" -X POST "${H[@]}" "${AUTH[@]}" -d "$(note x5 "$BIG")"
req "10 SQL-looking patient_ref"        "201 400" -X POST "${H[@]}" "${AUTH[@]}" -d "$(note "x6-$ID1" 'n' "' OR 1=1 --")"
rm -f /tmp/sync_body.$$
echo "Re-run after each fix. Also check: row count for $ID1 is 1 in the notes table."
