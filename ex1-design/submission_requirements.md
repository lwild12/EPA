# Ex1: what the sheet requires, and where each part stands

Source: the Exercise 1 section of the practical exercise sheet (version 11.0, 2026 Oct 16).

## What the sheet says you must produce

1. **Attempt every topic highlighted in yellow.** The dashed bullets under each topic are prompts, not a checklist. The highlighting does not survive in the PDF text, so check your coloured copy.
2. **Evidence for each topic.** The sheet asks for evidence in each bullet: designs, configurations, test results (expected against actual), and records of troubleshooting.
3. **A written justification of 1,000 words, plus or minus 100.**
4. **Use the supplementary tables** for pass, merit and distinction. They are *not* in the 9-page sheet, so they are the document that says how each grade is earned. Read them first thing.

**Not stated anywhere in the sheet:** the file format, the folder or system to submit to, or whether the policy and justification are separate files. Ask the assessor.

## The eight topics, evidence needed, and status

| Topic | Evidence the sheet asks for | Status |
| --- | --- | --- |
| 1 Networks | Requirements and trust boundaries, segmented design, configs with ACLs and secure management, test results, troubleshooting and optimisation | Built. Notes hold the VLAN table and test table. Add the requirements table, before and after ACL captures, and 2 or 3 real troubleshooting examples |
| 2 Digital system to a specification | Spec (inputs, outputs, functions, security, constraints), working prototype, failure cases, expected against actual, a debug that fixes a problem without breaking others | Built. Add 413 to the spec's outputs, and record one real fix and the retest |
| 3 OS to a security policy | Configured features (accounts, privileges, authentication, firewall, patching, services, logging), unneeded services reviewed, threat to setting, tested evidence | Table drafted. See the notes below |
| 4 Software and exploits | Input validation, analysis for injection, authentication, information disclosure and error handling, normal and unexpected input tests with security implications | Burp and SQLMap results to record |
| 5 Security technology and keys | Components chosen and configured, what to encrypt, key lifecycle, tests proving the policy | TLS, lifecycle table and revocation test to do |
| 6 Security case | Assets, threats, vulnerabilities, risks, controls, balance against usability and cost, residual risks | To do |
| 7 Architecture | Components, interfaces, trust boundaries, data flows, principles, attacker path, justified decisions, and support for testing, monitoring, maintenance, resilience and future change | To do. Add a short paragraph on that last point |
| 8 Policy and legal | Legal, regulatory, contractual and organisational requirements, policies, controls, how compliance is shown, gaps | `policy.md` drafted. Add one line on contractual duties (the cloud supplier and any NHS contract) |
| Written justification | 1,000 words, plus or minus 100 | Last |

## Points from reviewing the scratch notes

- **Spec outputs:** `sync.php` returns 413 for an oversized body. The spec lists 201, 200, 400, 401, 403 and 405. Add 413, or a marker will see an actual result that is not in the spec.
- **Spec security requirements:** "HTTPS Only" is listed, but `REQUIRE_HTTPS` is off until task 5. Show it off, then on.
- **OS table, firewall row:** it has no "How it is checked". Use `Get-NetFirewallProfile`.
- **OS table, attack paths row:** `Get-Service` does not check SMBv1 or RDP. Use `Get-SmbServerConfiguration` for SMBv1 and the `fDenyTSConnections` registry value for RDP.
- **Network test table:** it proves the denies well. Add one test that the admin VLAN can reach the devices VLAN, and one that another VLAN cannot.
- **Assumptions:** they are good evidence of requirements. Move them into a short "requirements and assumptions" table at the start of the network section.
