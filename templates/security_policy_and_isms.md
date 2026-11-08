# Information security policy and ISMS templates (ISO/IEC 27001 / NCSC aligned)

## A. Information security policy (one page; board/exec approved)

**Policy owner:** <role>  **Approved by:** <name/role>  **Date:** <>  **Next review:** <+12 months>

1. **Purpose.** Protect the confidentiality, integrity and availability of <org> information and systems, and meet legal, regulatory and contractual duties.
2. **Scope.** All staff, contractors, systems, networks, cloud services and information assets owned or processed by <org>.
3. **Principles.** Risk-based; least privilege; defence in depth; secure by default; accountability; continual improvement.
4. **Commitments.**
   - Maintain an asset register and a risk register, reviewed at least quarterly.
   - Control access using unique IDs, MFA for remote and privileged access, and timely leaver removal.
   - Keep systems patched (critical within 14 days, others within 30), backed up (tested), and logged.
   - Provide security awareness training at induction and annually; run phishing exercises.
   - Report incidents immediately; follow the incident response plan.
   - Assess suppliers before onboarding and review annually.
5. **Roles.** Executive owns risk acceptance; Security lead runs the ISMS; line managers enforce; all staff comply and report.
6. **Compliance.** Breaches may lead to disciplinary action. Exceptions need a documented, time-limited risk acceptance.
7. **Supporting documents.** Acceptable use, access control, cryptography/key management, incident response, business continuity, supplier security, data protection, secure development.

## B. ISMS structure (ISO/IEC 27001 clauses 4-10 in plain English)

| Clause | What it asks | Evidence you can show |
|---|---|---|
| 4 Context | Understand org, interested parties, scope | Scope statement, stakeholder list |
| 5 Leadership | Policy, roles, management commitment | Signed policy, RACI |
| 6 Planning | Risk assessment and treatment, objectives | Risk register, Statement of Applicability (SoA) |
| 7 Support | Resources, competence, awareness, documented info | Training records, document control |
| 8 Operation | Run controls and risk treatment | Procedures, change records, logs |
| 9 Performance | Monitor, internal audit, management review | KPIs, audit report, review minutes |
| 10 Improvement | Fix nonconformities, improve | Corrective action log |

Plan-Do-Check-Act: Plan (4-6), Do (7-8), Check (9), Act (10).

## C. Statement of Applicability (excerpt format)

| Annex A control (2022 numbering) | Applicable? | Why / why not | Implemented? | Evidence |
|---|---|---|---|---|
| 5.15 Access control | Yes | Protects systems from unauthorised use | Yes | Access policy, review records |
| 5.24 Incident management planning | Yes | Legal reporting duties | Yes | IR plan, exercise log |
| 8.5 Secure authentication | Yes | Remote admin exposure | Partial | MFA on VPN; gap on legacy app (R3) |
| 8.13 Information backup | Yes | Ransomware risk | Yes | Restore test report |
| 8.24 Use of cryptography | Yes | Data at rest/in transit | Yes | Key management plan |
| 8.28 Secure coding | Yes | In-house web apps | Yes | Code review, SAST output |
| 7.4 Physical security monitoring | No (cloud-only) | No premises with systems | N/A | Hosting provider certification |

## D. KPIs for management review
Patch compliance %, MFA coverage %, mean time to detect/contain, phishing click rate, backup restore success, open high risks, audit findings closed on time.

## E. Standards cross-reference (cite where you use them)
ISO/IEC 27001:2022 and 27002:2022; NIST CSF 2.0; NCSC 10 Steps and CAF; Cyber Essentials; CIS Controls v8.
