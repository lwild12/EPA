# Evidence log, figure captions and page budget

**Screenshots: maximum 5 pages of A4.** Crop tightly. Every figure needs a number, a caption and a mention in the text.

## Figure list

The "Original file" column lets you trace each figure back to the screenshot taken on Thursday. Captions are suggestions: check each one against the image and change it.

| Fig | Original file | Suggested caption | Used in |
| --- | --- | --- | --- |
| 1 | `Screenshot 2026-11-12 110036` | Static triage report: one import, entropy 6.96, "low suspicion" verdict | Malware |
| 2 | `Screenshot 2026-11-12 112123` | CAPE static analysis: "encrypted or compressed data" warning; VT, MWDB and Bazaar tags on the hash | Malware, Intel |
| 3 | `Screenshot 2026-11-12 111046` | Process tree: the sample starts a child copy of itself | Malware |
| 4 | `Screenshot 2026-11-12 111118` | YARA hits on process dumps (`agent_tesla`, `AgentTeslaV2`) | Malware |
| 5 | `Screenshot 2026-11-12 111130` | Modified files: `Temp\xws\xws.exe` | Malware |
| 6 | `Screenshot 2026-11-12 111146` | Modified registry keys: `Run\xws` and the `mscfile` command | Malware |
| 7 | `Screenshot 2026-11-12 115726` | MITRE ATT&CK mapping from the sandbox | Malware |
| 8 | `Screenshot 2026-11-12 111216` | DNS requests, including `checkip.dyndns.org` | Intel, Malware |
| 9a | `Screenshot 2026-11-12 150954` | One request with an invalid token: 401 "authentication required" | Threats (lab) |
| 9b | `Screenshot 2026-11-12 151003` | 200 invalid-token requests: all 401, no lockout | Threats (lab) |

**Not used:** `150545` (the loop printed `200 000`, a failed connection), `110201` (small file-name crop), `111208` (30-row host list; its data is used in Table 1 instead).

## Page budget (5 pages of A4)

Suggested layout:

1. Figs 1, 2
2. Figs 3, 4
3. Figs 5, 6, 7
4. Fig 8
5. Figs 9a, 9b

**If you are over 5 pages, cut in this order:**

1. Crop Fig 7 harder (keep the persistence, evasion and C2 columns)
2. Stack 9a and 9b together
3. Merge Figs 5 and 6
4. Drop Fig 8

## Evidence log (activity record)

The brief asks for "an auditable record of activities, evidence, decisions and findings". Keep it short. Add a line after each block.

| Time | Action | Evidence (Fig or file) | Decision or finding |
| --- | --- | --- | --- |
| 09:30 | Started Friday work | none | none |
| | | | |
| | | | |
| | | | |

Write the time as you finish each block (e.g. "10:30 Intel table complete, 7 rows enriched").
