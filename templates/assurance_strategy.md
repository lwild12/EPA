# Assurance strategy template

**Goal:** give stakeholders justified confidence that controls exist, are designed well, and work in practice.

## 1. Assurance layers (three lines)
| Line | Who | Activities |
|---|---|---|
| 1st | System owners / operations | Control operation, self-checks, monitoring, patching |
| 2nd | Security / risk / compliance | Policy, risk assessment, control testing, KPIs |
| 3rd | Internal audit / external assessors | Independent audit, penetration test, certification (ISO 27001, Cyber Essentials Plus) |

## 2. Assurance activities and cadence
| Activity | Scope | Method | Frequency | Output | Owner |
|---|---|---|---|---|---|
| Vulnerability scanning | All hosts/apps | Nessus/OpenVAS authenticated scans | Weekly (critical assets) / monthly | Findings with CVSS and SLA | SecOps |
| Penetration test | External + web app | Scoped, independent tester (CHECK/CREST) | Annually + after major change | Report, retest evidence | Security lead |
| Configuration review | Network and servers | CIS benchmarks, `linux_audit.sh`, Cisco config audit | Quarterly | Deviation list | Network/SysOps |
| Secure code review | In-house code | Peer review + SAST/DAST in CI | Every change / release | Findings, gates | Dev lead |
| Backup restore test | Critical systems | Restore to isolated env, verify integrity | Quarterly | Test record | IT |
| Incident exercise | IR plan | Tabletop with scenario | Twice yearly | Lessons, actions | IR manager |
| Access review | Privileged and all users | Manager attestation | Quarterly / 6-monthly | Removals logged | IAM |
| Supplier review | Critical suppliers | Questionnaire + certificates + SOC 2/ISO evidence | Annually | Risk rating | Procurement |
| Internal ISMS audit | ISMS scope | ISO 19011-style audit | Annually | Audit report, corrective actions | Internal audit |

## 3. Evidence rules
Independent where possible, repeatable (documented method), time-stamped, retained for <period>, linked to a control ID and risk ID.

## 4. Metrics and thresholds
| Metric | Target | Red if |
|---|---|---|
| Critical vulns older than 14 days | 0 | > 0 |
| Systems failing config baseline | < 5% | > 10% |
| Restore test success | 100% | any fail |
| Privileged accounts without MFA | 0 | > 0 |
| Overdue audit actions | < 10% | > 25% |

## 5. Reporting
Monthly dashboard to security lead, quarterly to executive, annual assurance statement. Escalate red metrics immediately with an owner and date.

## 6. Limits of assurance (say this; markers like honesty)
Testing is a sample at a point in time; scans miss logic flaws; pen tests are scope-limited; attestations rely on honesty. Therefore combine methods and re-test after change.

## 7. Standards
ISO/IEC 27001 clause 9, NIST SP 800-53A / 800-115, NCSC CAF, OWASP ASVS and WSTG, CIS Benchmarks, CREST.
