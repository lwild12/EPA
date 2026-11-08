# STRIDE threat model template

## 1. Describe the system (data flow diagram)
List: **external entities** (users, third parties), **processes** (web app, API, DB service), **data stores** (database, file store, logs), **data flows** (arrows, label protocol and data), **trust boundaries** (internet | DMZ | internal | admin).
Sketch it in Packet Tracer / draw.io / ASCII:

```
[User browser] --HTTPS--> [Web app (DMZ)] --SQL/TLS--> [Database (internal)]
                                  |--> [File store]     Admin --SSH via VPN--> [Servers]
```

## 2. STRIDE per element

| Letter | Threat | Violates | Typical mitigation |
|---|---|---|---|
| S | Spoofing identity | Authentication | MFA, certificates, signed tokens, anti-replay |
| T | Tampering | Integrity | TLS, signatures/HMAC, input validation, file integrity monitoring, least-privilege writes |
| R | Repudiation | Non-repudiation | Tamper-evident logs, time sync, audit trail with user IDs |
| I | Information disclosure | Confidentiality | Encryption at rest/in transit, access control, error handling, data minimisation |
| D | Denial of service | Availability | Rate limiting, redundancy, quotas, WAF/CDN, capacity monitoring |
| E | Elevation of privilege | Authorisation | Least privilege, deny by default, patching, sandboxing, object-level checks |

## 3. Threat table (fill one row per threat)

| ID | Element / flow | STRIDE | Threat description | Likelihood | Impact | Mitigation (existing / planned) | Status |
|---|---|---|---|---|---|---|---|
| T1 | Login form | S | Credential stuffing | H | H | Throttling, lockout, MFA | Existing (app.php lockout) |
| T2 | Upload endpoint | T/E | Webshell upload | M | H | Allow-list + MIME + random names + outside web root | Existing |
| T3 | DB link | I | Sniffing SQL traffic | L | H | TLS to DB, segmentation | Planned |
| T4 | Admin path | E | Stolen admin session | M | H | VPN-only, short sessions, MFA | Planned |
| T5 | Log store | R | Attacker clears logs | M | M | Forward logs off-host, append-only | Planned |
| T6 | Public site | D | HTTP flood | M | M | Rate limit, CDN/WAF | Planned |

## 4. Prioritise and link
Score with the risk register method (`risk_register.md`), map each mitigation to a control (ASVS / CIS / ISO 27002) and to a test you ran.

## 5. Validate
For each high threat, state how you would test the mitigation (unit test, scan, manual abuse case) and the result.

## Complementary views
- **ATT&CK** for attacker behaviour on your assets; **kill chain** for stages; **attack trees** for goals (e.g. "steal customer data" -> phish admin OR exploit upload OR SQLi).
