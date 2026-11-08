# Risk register and risk-assessment method

## Method (say this in one paragraph in your write-up)

1. **Identify assets** (data, systems, services, people) and their value (C, I, A each 1-5).
2. **Identify threats** (who/what) and **vulnerabilities** (weakness). Use STRIDE or ATT&CK to prompt ideas (see `stride_threat_model.md`).
3. **Likelihood** 1-5 (1 rare ... 5 almost certain) using evidence: logs, scan results, threat intel.
4. **Impact** 1-5 (1 negligible ... 5 severe) across confidentiality, integrity, availability, legal/regulatory, safety.
5. **Inherent risk** = Likelihood x Impact (1-25). Bands: 1-4 Low, 5-9 Medium, 10-16 High, 17-25 Critical.
6. **Treat**: Mitigate / Transfer / Avoid / Accept. Name the control and owner.
7. **Residual risk** = re-score after controls. Record who accepted it and review date.
8. **Monitor**: review on change, incident, or at least quarterly.

Aligns with ISO/IEC 27005, NIST SP 800-30 and the NCSC risk-management guidance (check current wording before citing).

## Scoring grid

| Likelihood \ Impact | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 5 | 5 | 10 | 15 | 20 | 25 |
| 4 | 4 | 8 | 12 | 16 | 20 |
| 3 | 3 | 6 | 9 | 12 | 15 |
| 2 | 2 | 4 | 6 | 8 | 10 |
| 1 | 1 | 2 | 3 | 4 | 5 |

## Register template

| ID | Asset | Threat | Vulnerability | L | I | Inherent | Treatment | Control (standard ref) | Owner | Residual L | Residual I | Residual | Review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | Web upload app | Malicious file upload | No type/content validation | 4 | 4 | 16 High | Mitigate | Allow-list + MIME check + store outside web root (OWASP ASVS V12) | Dev lead | 1 | 4 | 4 Low | Quarterly |
| R2 | Student VLAN | Lateral movement to servers | Flat network | 4 | 5 | 20 Critical | Mitigate | VLAN + ACL segmentation (CIS Control 12) | Network | 2 | 5 | 10 High | Quarterly |
| R3 | Admin accounts | Credential theft | Password-only login | 3 | 5 | 15 High | Mitigate | MFA (NCSC guidance) | IT | 1 | 5 | 5 Medium | Quarterly |
| R4 | Backups | Ransomware encrypts backups | Backups reachable from domain | 3 | 5 | 15 High | Mitigate | Immutable/offline copy, 3-2-1 (NCSC) | IT | 1 | 5 | 5 Medium | Quarterly |
| R5 | Remote access | Brute force on SSH/RDP | Exposed management ports | 4 | 4 | 16 High | Mitigate | VPN-only, rate-limit, MFA | Network | 1 | 4 | 4 Low | Quarterly |

(The rows above are examples. Replace them with risks from YOUR brief and YOUR evidence.)

## Writing tips

- One risk = one threat + one weakness + one consequence. Do not bundle.
- Show the arithmetic once (L x I) so the marker sees the method, not just the number.
- Always include at least one **accepted** risk with a reason; it shows you are not pretending to remove all risk.
- Link each high risk to the control you built/tested in the exercise (evidence figure number).
