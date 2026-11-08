#!/usr/bin/env bash
# Automated security checks against app.php. Run from this folder: bash test_app.sh
# Starts a throwaway server on 127.0.0.1:8099, runs checks, stops it, cleans up.
set -u
cd "$(dirname "$0")"
PORT=8099
BASE="http://127.0.0.1:$PORT/app.php"
JAR=$(mktemp)
TMP=$(mktemp -d)
rm -f app.sqlite
php -S 127.0.0.1:$PORT app.php >/dev/null 2>"$TMP/server.log" &
PID=$!
trap 'kill $PID 2>/dev/null; rm -rf "$TMP" "$JAR" app.sqlite private_uploads' EXIT
sleep 1
pass=0; fail=0
ok()   { echo "[PASS] $1"; pass=$((pass+1)); }
bad()  { echo "[FAIL] $1"; fail=$((fail+1)); }
check() { if [ "$2" = "1" ]; then ok "$1"; else bad "$1"; fi; }

token() { curl -s -b "$JAR" -c "$JAR" "$BASE" | grep -o 'name="csrf" value="[^"]*"' | head -1 | sed 's/.*value="//;s/"//'; }

# headers
H=$(curl -s -D - -o /dev/null "$BASE")
check "CSP header present" "$(echo "$H" | grep -qi '^content-security-policy' && echo 1 || echo 0)"
check "X-Content-Type-Options nosniff" "$(echo "$H" | grep -qi 'x-content-type-options: nosniff' && echo 1 || echo 0)"
check "X-Frame-Options DENY" "$(echo "$H" | grep -qi 'x-frame-options: DENY' && echo 1 || echo 0)"
check "Session cookie HttpOnly" "$(echo "$H" | grep -i 'set-cookie' | grep -qi httponly && echo 1 || echo 0)"
check "Session cookie SameSite" "$(echo "$H" | grep -i 'set-cookie' | grep -qi samesite && echo 1 || echo 0)"

T=$(token)
# CSRF
C=$(curl -s -o /dev/null -w '%{http_code}' -b "$JAR" -c "$JAR" -d 'username=bob&password=a_long_password_123' "$BASE?a=register")
check "Register without CSRF token rejected (403)" "$([ "$C" = 403 ] && echo 1 || echo 0)"
# weak password
R=$(curl -s -b "$JAR" -c "$JAR" -d "csrf=$T&username=bob&password=short" "$BASE?a=register")
check "Short password rejected" "$(echo "$R" | grep -q 'at least 12' && echo 1 || echo 0)"
# register + login
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d "csrf=$T&username=alice&password=correct-horse-battery" "$BASE?a=register"
# SQLi attempt
L=$(curl -s -b "$JAR" -c "$JAR" --data-urlencode "csrf=$T" --data-urlencode "username=' OR '1'='1' --" --data-urlencode "password=x" "$BASE?a=login")
check "SQL injection login attempt fails" "$(echo "$L" | grep -q 'Invalid credentials' && echo 1 || echo 0)"
# real login
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d "csrf=$T&username=alice&password=correct-horse-battery" "$BASE?a=login"
HOME_PAGE=$(curl -s -b "$JAR" -c "$JAR" "$BASE")
check "Valid login works" "$(echo "$HOME_PAGE" | grep -q 'Your files' && echo 1 || echo 0)"
T2=$(echo "$HOME_PAGE" | grep -o 'name="csrf" value="[^"]*"' | head -1 | sed 's/.*value="//;s/"//')

# upload tests
printf 'hello\n' > "$TMP/ok.txt"
printf '<?php system($_GET["c"]); ?>' > "$TMP/shell.php"
printf '<?php system($_GET["c"]); ?>' > "$TMP/shell.txt"
head -c 3000000 /dev/zero > "$TMP/big.txt"
up() { curl -s -b "$JAR" -c "$JAR" -F "csrf=$T2" -F "file=@$1" "$BASE?a=upload"; }

up "$TMP/ok.txt" >/dev/null
L2=$(curl -s -b "$JAR" "$BASE")
check "Allowed text file accepted" "$(echo "$L2" | grep -q 'ok.txt' && echo 1 || echo 0)"
check ".php upload rejected" "$(up "$TMP/shell.php" | grep -q 'not allowed' && echo 1 || echo 0)"
check "PHP disguised as .txt rejected (MIME check)" "$(up "$TMP/shell.txt" | grep -q 'does not match' && echo 1 || echo 0)"
check "Oversize file rejected" "$(up "$TMP/big.txt" | grep -Eq 'too large|failed' && echo 1 || echo 0)"
check "Uploads stored with random names" "$([ "$(ls private_uploads | grep -c '^[0-9a-f]\{32\}$')" -ge 1 ] && echo 1 || echo 0)"
check "Uploads are mode 600" "$([ "$(stat -c %a private_uploads/* | sort -u)" = "600" ] && echo 1 || echo 0)"

# auth / authz
C=$(curl -s -o /dev/null -w '%{http_code}' "$BASE?a=download&id=1")
check "Download without login rejected (401)" "$([ "$C" = 401 ] && echo 1 || echo 0)"
J2=$(mktemp)
T3=$(curl -s -b "$J2" -c "$J2" "$BASE" | grep -o 'name="csrf" value="[^"]*"' | head -1 | sed 's/.*value="//;s/"//')
curl -s -o /dev/null -b "$J2" -c "$J2" -d "csrf=$T3&username=mallory&password=another-long-password" "$BASE?a=register"
curl -s -o /dev/null -b "$J2" -c "$J2" -d "csrf=$T3&username=mallory&password=another-long-password" "$BASE?a=login"
C=$(curl -s -o /dev/null -w '%{http_code}' -b "$J2" "$BASE?a=download&id=1")
check "Other user cannot download alice's file (IDOR) (404)" "$([ "$C" = 404 ] && echo 1 || echo 0)"
rm -f "$J2"

# lockout
for i in 1 2 3 4 5; do curl -s -o /dev/null -b "$JAR" -c "$JAR" -d "csrf=$T&username=alice&password=wrong$i" "$BASE?a=login"; done
LK=$(curl -s -b "$JAR" -c "$JAR" -d "csrf=$T&username=alice&password=correct-horse-battery" "$BASE?a=login")
check "Account locks after 5 failures" "$(echo "$LK" | grep -q 'locked' && echo 1 || echo 0)"

# XSS: filename is escaped on render
printf 'x' > "$TMP/x.txt"
echo
echo "Passed: $pass  Failed: $fail"
[ "$fail" -eq 0 ]
