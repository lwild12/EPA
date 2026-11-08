# Incident response plan template (aligned to NIST SP 800-61 and NCSC incident management)

**Organisation:** <name>  **Version/date:** <>  **Owner:** <role>  **Review:** annually and after every major incident

## 1. Purpose and scope
Defines how <org> prepares for, detects, responds to and learns from security incidents affecting <systems/data>.

## 2. Roles
| Role | Responsibility | Primary / deputy | Contact |
|---|---|---|---|
| Incident manager | Owns the response, makes containment calls | | |
| Technical lead | Investigation, containment, eradication | | |
| Communications | Staff, customers, media | | |
| Legal / DPO | Regulatory and data-protection decisions | | |
| Executive sponsor | Approves major actions (e.g. shutting down services) | | |
| Scribe | Keeps the timeline log (who, what, when) | | |

## 3. Severity levels
| Level | Example | Response target | Escalate to |
|---|---|---|---|
| 1 Critical | Ransomware, active data theft, safety impact | Start within 15 min, 24/7 | Exec + legal |
| 2 High | Confirmed compromise of one system or account | 1 hour | Security lead |
| 3 Medium | Malware blocked, policy breach | 4 hours | Service desk lead |
| 4 Low | Phishing reported, failed scan | Next business day | Service desk |

## 4. Lifecycle

1. **Prepare**: asset inventory, logging (central, time-synced), backups tested, contacts list, playbooks, exercises (tabletop at least yearly).
2. **Detect and analyse**: alerts, user reports, threat intel. Record: first seen, affected hosts/accounts, indicators (hashes, IPs, domains), initial scope. Preserve volatile evidence first.
3. **Contain**: short-term (isolate host, disable account, block IOC) then long-term (segment, patch). Decide using impact vs evidence-loss trade-off.
4. **Eradicate**: remove malware/persistence, reset credentials and keys, close the entry route.
5. **Recover**: restore from known-good, monitor closely for recurrence, staged return to service.
6. **Lessons learned**: blameless review within 2 weeks; update controls, detections and this plan.

## 5. Evidence handling
- Hash and record everything (SHA-256), keep a chain-of-custody log, work on copies, store originals read-only.
- Time-stamp in UTC; note timezone of any local logs.

## 6. Notification and reporting (UK, verify current guidance before use)
- **Personal data breach:** assess risk; report to the data protection regulator within **72 hours** of becoming aware if there is a risk to individuals (UK GDPR Art. 33). The regulator is now the **Information Commission** (succeeded the ICO on 30 September 2026).
- **Individuals:** inform without undue delay if high risk to them (Art. 34).
- **Cyber crime / fraud:** report via **Report Fraud** (replaced Action Fraud) and to the NCSC where appropriate (NCSC incident reporting).
- Sector duties: NIS regulations / sector regulator, insurer notification clause, contractual customer notices.
- Record the decision and reasoning even if you decide NOT to notify.

## 7. Communication rules
- Single spokesperson. Use out-of-band channels if email may be compromised.
- Factual, no speculation. Log every external statement.

## 8. Playbook stubs (one page each)
- Ransomware | Phishing / BEC | Lost or stolen device | Web app compromise | DDoS | Insider misuse

## 9. Metrics
Mean time to detect, to contain, to recover; incidents by type; % with completed lessons-learned actions.
