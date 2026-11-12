# Lab test write-up (template)

**Time-box: 15 minutes for this write-up.** Use your real results. If something here does not match your files, change it.

This is your evidence for "demonstrate an attack technique in a lab" (Threats, pass) and the mitigation for distinction.

## Test 1: invalid token guessing against the sync API (Figs 9a, 9b)

- **Aim:** check whether the API limits repeated invalid token attempts.
- **Target:** the Ex1 sync application only (in scope in the RoE). Write the target in your log.
- **Method:** I sent 200 requests with different invalid bearer tokens and counted the response codes.
- **Result:** every response was 401 "authentication required". No 429 response, no lockout, no slowdown seen.
- **Finding:** no rate limiting or lockout was seen in 200 attempts. An attacker could keep guessing.
- **Mitigation:** rate limiting and lockout on repeated failures; long random tokens; alerts on bursts of 401 responses.
- **Limit:** 200 attempts is a small sample. I do not claim the API is otherwise secure.
- **Note on the first attempt:** an earlier loop printed `200 000`, which means the connection failed (certificate). It was not used as evidence.

## Test 2: sqlmap against the JSON endpoint (`sqlmap.txt`)

- **Aim:** check for SQL injection in the JSON body.
- **Result:** sqlmap reported that the tested parameter "does not seem to be injectable". It also received `400 (Bad Request)` 752 times.
- **Meaning:** **inconclusive.** The many 400 responses suggest the server rejected the test payloads. That may be good input validation, or the payloads may have broken the request format. It does not prove the code is safe.
- **Next step (assurance):** retest with a request format the API accepts, and review the code.

## Check

- ☐ Target was in scope
- ☐ Counts match your figures (200 requests, all 401; 752 x 400)
- ☐ No word "secure" or "safe" anywhere
- ☐ Mitigation written
- ☐ Figures numbered and mentioned in the text
