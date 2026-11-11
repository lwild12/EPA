# Ex1: submission guide

Built from the example EPA pack (version 4, 2023) and the exercise sheet (version 11). The example pack may differ from your live rules, so check every line marked **(check)** against your own paperwork.

## Rules that shape what you hand in

- Submit **all files to ENU Moodle**. The link in the example pack is blank, so get it from your supervisor. **(check)**
- Submission is **final**. No reloading or amending. **(check)**
- Screenshots are limited to **5 pages of A4 in total**. Use a cropping tool, not full-screen shots. **(check)**
- The test is **open book**: notes, books and internet are allowed. **(check)**
- It is an **individual** test. Keep written confirmation of any assistance you were allowed to use. **(check)**
- Test hours are 09:30 to 16:00. Take a 30-minute break and email your supervisor when it starts and ends. **(check)**
- Every exercise must reach the pass standard for the whole test to pass.

## Files to submit (suggested names)

| File | Contents |
| --- | --- |
| `Ex1_justification.docx` | The written justification, 900 to 1,100 words |
| `Ex1_evidence.docx` (or `.pdf`) | Designs, tables and cropped screenshots, within the 5-page screenshot cap |
| `Ex1_network_configs.txt` | Saved running configs (router, switch, others) |
| `Ex1_prototype/` | `sync.php`, `db.php`, `schema.sql`, test script and results |
| `Ex1_os_hardening.txt` | "Before" and "after" command output |
| `Ex1_policy.docx` | The four policies and the rule, control and evidence map |

If the portal wants a single file, merge them and keep the order above. Ask first. **(check)**

## Screenshot budget (5 pages)

Aim for about 8 to 10 small crops per page, labelled with the topic number.

| Page | Topic | Show |
| --- | --- | --- |
| 1 | 1 Network | Topology, VLAN table, test table before and after ACLs |
| 2 | 2 and 4 Prototype | Spec table, test run with PASS/FAIL, Burp or SQLMap result, one fix and retest |
| 3 | 3 OS | Before and after for firewall, encryption, accounts, audit policy |
| 4 | 5 Keys | HTTP capture against HTTPS capture, key lifecycle table, revocation 401 |
| 5 | 6, 7, 8 | Risk table, architecture diagram, rule to evidence map |

Tables you can type into the main document do not need screenshots. Keep screenshots for proof that something ran.

## Grade criteria to cover (from the example pack, check against yours)

| Competency | Pass | Merit | Distinction |
| --- | --- | --- | --- |
| Networks | More than one subnet, with static and dynamic routes. Tests show it meets the design. Typical problems troubleshot | Evidence the optimised network meets the requirements. More than one design option considered | Complex problems troubleshot |
| Digital system | Components working to a defined specification | n/a | n/a |
| OS | Threats, security features, residual weaknesses. OS configured to policy | n/a | n/a |
| Security components | At least 2 types selected and configured | n/a | n/a |
| Security case | A simple system built to a security case, with evidence | Covers two layers | Covers all layers |

Check these points against your build:
- **Dynamic routing:** you have a static default route. If your pack requires dynamic routes, add and test OSPF or RIP between the router and the ISP (or between subnets), or explain why not.
- **Design options:** write one paragraph on an alternative you rejected (for example a routed switch instead of router-on-a-stick).
- **Residual weaknesses:** list those in the OS section.
- **Layers:** show the controls at network, host and application level in the security case.

## Last 30 minutes before you submit

1. Word count of the justification: 900 to 1,100.
2. Every one of the eight topics has some evidence, and none is blank.
3. Each screenshot is cropped and labelled with its topic.
4. Every test table has expected against actual, and the actual results are real.
5. No real passwords, tokens or keys are visible in screenshots or files. Check configs for `enable secret` and API tokens.
6. File names are as the portal expects, and each file opens.
7. Anything you could not finish is named as a gap in the justification, not hidden.
8. Upload, then confirm each file shows on the portal. Remember it is final.

## If you are short of time

1. Never skip: some evidence for all eight topics, and the justification.
2. Cut extra tests in the prototype and extra attacks.
3. Write two policies in full and outline the rest.
4. Shorten the OS "before" capture to firewall, encryption and accounts.
