# Information Security Policy: mobile visit notes

| | |
| --- | --- |
| Organisation | `<COMPANY>` |
| Version | 1.0 (draft) |
| Owner | Chief Information Security Officer |
| Approved by | Board of Directors (date to add) |
| Review | Every two years, and after any major incident or change in law |

## 1. Purpose and scope

1.1 This policy protects the personal data of the people `<COMPANY>` supports, mainly visit notes that staff write offline, cache on laptops and phones, and sync later through the care system API. It also protects business information.
1.2 It applies to all staff and contractors, and to every device, network and system used to handle this data, including personal devices used for work.
1.3 Visit notes are health and care information about vulnerable people. They are treated as the most sensitive data we hold.

## 2. Roles

2.1 The Board approves this policy.
2.2 The Chief Information Security Officer (CISO) is responsible for putting it into effect.
2.3 The Data Protection Officer (DPO) advises on data protection and decides on reports to the regulator.
2.4 Everyone must follow this policy and report problems. Breaches of it may lead to disciplinary action.

## 3. Mobile devices and remote wipe

3.1 Only devices approved by IT, and enrolled in mobile device management (MDM), may hold visit notes.
3.2 Devices must use full-disk encryption, a PIN or password, and an automatic screen lock.
3.3 Rooted or jailbroken devices are not permitted.
3.4 A device holds only the notes needed for the day's visits. Cached notes are cleared once the server confirms the sync.
3.5 A device that has not synced for [7] days wipes its cache automatically. IT may also wipe a device remotely when it has signal.
3.6 Notes may be written offline. They sync only when the device holds a valid token (section 5).
3.7 Notes must not be stored in unapproved apps, personal cloud storage or removable media. Approved removable media must be encrypted.
3.8 Working away from the office needs a private setting where screens cannot be seen.

## 4. Access control and authentication

4.1 Access is by role and follows least privilege. Access is reviewed every [6] months and removed when a person leaves or changes role.
4.2 Passwords must be at least 12 characters, unique, and not on a list of known breached passwords. Long phrases are encouraged. Composition rules are not forced.
4.3 Accounts lock after five failed sign-ins. Resets go through a trusted process.
4.4 Multi-factor authentication (MFA) is required for remote access, cloud services and all administrator accounts.
4.5 Network devices are managed only from the administration VLAN, using SSH version 2 and individual accounts.
4.6 Administrator actions and sign-ins are logged, and logs are kept for at least 12 months and protected from change.
4.7 Staff are told that systems are monitored. Monitoring is proportionate and limited to security purposes, and a data protection impact assessment (DPIA) records the reasons.

## 5. Cryptography and key management

5.1 Data in transit is protected: sync traffic uses TLS 1.2 or later, and the API refuses requests that do not use HTTPS.
5.2 Data at rest on devices is protected by disk encryption (section 3.2).
5.3 API tokens are random, scoped to the least privilege needed, expire after [30] days, and are stored only as hashes.
5.4 Tokens are revoked immediately when a device is lost, a person leaves, or misuse is suspected. A revoked token must fail the next request.
5.5 Private keys are kept off shared storage, with access limited to named administrators. They are never stored in source code or the web folder.
5.6 Each key has an owner and a recorded lifecycle: generation, storage, access, rotation, revocation and protection. Keys are rotated on a schedule and at once after any suspected compromise.
5.7 Recovery keys for device encryption are held in the management system, not on the device.
5.8 Certificates in production come from a trusted authority. Lab certificates are self-signed and are never used in production.

## 6. Incident and breach reporting

6.1 Staff must report any lost or stolen device, suspected breach, weakness or near miss to the IT Security team within 24 hours of finding it. This is an internal rule.
6.2 The CISO and DPO assess each incident for the risk to people.
6.3 Where a breach is likely to risk people's rights and freedoms, `<COMPANY>` reports it to the Information Commissioner's Office (ICO) where feasible within 72 hours of becoming aware (UK GDPR Article 33). Information may be sent in stages.
6.4 Where the risk to people is high, they are told without undue delay.
6.5 Every incident is recorded: what happened, the data involved, the actions taken, and the lessons learned. Major incidents get a post-incident review.
6.6 The incident plan is tested at least once a year.

## 7. Legal and regulatory basis

- UK GDPR and the Data Protection Act 2018, in particular Article 5 (principles), Article 32 (security of processing) and Article 33 (breach notification).
- Caldicott principles for confidential health and care information.
- Data Security and Protection Toolkit (DSPT), where `<COMPANY>` has access to NHS patient data and systems.
- Computer Misuse Act 1990, for unauthorised access.

## 8. Rule, control and evidence

| Rule | Control | Evidence |
| --- | --- | --- |
| 3.2 Encryption and lock | BitLocker, screen lock | Topic 3 "after" file |
| 3.4, 3.5 Small cache, auto-wipe | Cache rules, MDM wipe | Design note, architecture diagram |
| 4.1 Least privilege | Scope check in `sync.php` | Test 5 (403) |
| 4.5 Management only from admin VLAN | ACLs, SSH v2 | Part A test table |
| 5.1 HTTPS only | TLS, `REQUIRE_HTTPS` | HTTP 403 test, Wireshark captures |
| 5.3 Hashed, expiring tokens | SHA-256 hash, `expires_at` | `api_tokens` table screenshot |
| 5.4 Revocation | `revoked` flag | Revocation test (401) |
| 5.6 Key lifecycle | Lifecycle table | Task 5 table |
| 6.1 to 6.5 Reporting | Incident process | Written procedure (not yet tested) |

## 9. Known gaps

- The lab uses a self-signed certificate with no passphrase on the key.
- Wi-Fi uses a shared pre-shared key. Production should use WPA2-Enterprise.
- MDM, remote wipe and the incident process are described but not built in the lab.
- Square-bracket values are proposals. Change them to match `<COMPANY>`'s own risk appetite.
