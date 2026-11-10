#!/usr/bin/env bash
# Runs the 10 tests from the spec table (2c) against YOUR sync endpoint.
# Usage:
#   URL=http://localhost/sync.php TOKEN_OK=<write token> TOKEN_READONLY=<read-only token> bash test_sync.sh
# Prints PASS/FAIL and the actual status code, so you can paste results into the "Actual" column.
# Only run against your own system on your own machine.
set -u
URL=${URL:-http://localhost/sync.php}
TOKEN_OK=${TOKEN_OK:?set TOKEN_OK}
TOKEN_READONLY=${TOKEN_READONLY:-}
ID1="test-$(date +%s)-a"
BODY=$(mktemp); OUT=$(mktemp)
trap 'rm -f "$BODY" "$OUT"' EXIT

# note CLIENT_ID TEXT [PATIENT_REF]  -> writes the JSON body to $BODY (a file avoids shell argument-size limits)
note() {
  printf '{"client_id":"%s","staff_id":"s1","patient_ref":"%s","note_text":"' "$1" "${3:-P123}" > "$BODY"
  if [ "$2" = "@big" ]; then head -c 3000000 /dev/zero | tr '\0' 'A' >> "$BODY"; else printf '%s' "$2" >> "$BODY"; fi
  printf '","created_at":"2026-11-10T09:00:00Z"}' >> "$BODY"
}
# check LABEL EXPECTED_CODES [curl args...]   (body is sent from $BODY when -X POST is used with --data-binary)
check() {
  local label=$1 expect=$2; shift 2
  local code; code=$(curl -s -o "$OUT" -w '%{http_code}' "$@" "$URL")
  local v=FAIL; case " $expect " in *" $code "*) v=PASS;; esac
  printf '%-4s| expect %-8s| got %-4s| %s\n' "$v" "$expect" "$code" "$label"
  if grep -qiE 'stack trace|PDOException|mysqli|SQLSTATE|Fatal error|syntax to use' "$OUT"; then
    echo "      ^ WARNING: response leaks an error or SQL detail"
  fi
}
J=(-H 'Content-Type: application/json'); A=(-H "Authorization: Bearer $TOKEN_OK"); P=(-X POST --data-binary @"$BODY")

note "$ID1" 'visit note';       check "1  valid note, valid token"       201 "${J[@]}" "${A[@]}" "${P[@]}"
note "$ID1" 'visit note';       check "2  same note again (idempotent)"  200 "${J[@]}" "${A[@]}" "${P[@]}"
note x1 'n';                    check "3  no token"                      401 "${J[@]}" "${P[@]}"
note x2 'n';                    check "4  wrong token"                   401 "${J[@]}" -H 'Authorization: Bearer not-a-real-token-123456' "${P[@]}"
if [ -n "$TOKEN_READONLY" ]; then
  note x3 'n';                  check "5  token without write scope"     403 "${J[@]}" -H "Authorization: Bearer $TOKEN_READONLY" "${P[@]}"
else echo "SKIP| 5  (set TOKEN_READONLY to run)"; fi
note x4 '';                     check "6  empty note_text"               400 "${J[@]}" "${A[@]}" "${P[@]}"
printf '{not json' > "$BODY";   check "7  invalid JSON"                  400 "${J[@]}" "${A[@]}" "${P[@]}"
                                check "8  GET instead of POST"           405 "${A[@]}" -X GET
note x5 '@big';                 check "9  very large note_text (3 MB)"   "400 413" "${J[@]}" "${A[@]}" "${P[@]}"
note "x6-$ID1" 'n' "' OR 1=1 --"; check "10 SQL-looking patient_ref"     "201 400" "${J[@]}" "${A[@]}" "${P[@]}"
echo "Also check by hand: only one row exists for client_id $ID1 in the notes table."
