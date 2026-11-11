# Ex2 Thursday: keep-on-track sheet

Full detail is in the Thursday guide. This sheet only keeps you on time.
**Start time: ________**   **Finish by: ________**

**Rules**

1. 15 minutes over a box? Stop. Move on. Come back at the end.
2. Screenshot straight after each step. Log it on the evidence sheet.
3. Lab VMs only. Revert to `clean` after each test.
4. Never cut: evidence for every highlighted topic, the hashes, notes for tomorrow.
5. Stuck? Water, say "the next step is ____", write your assumption, move on.

**Highlighted (mandatory) topics in my brief:**
☐ Malware   ☐ Threats and attacks   ☐ Assurance   ☐ Legal and ethics   ☐ Autopsy   ☐ Justification

## Schedule (6 hours)

| # | Block | Mins | T+ | Clock | Done |
| --- | --- | --- | --- | --- | --- |
| 1 | Start of day | 30 | 0:30 | ____ | ☐ |
| 2 | A. Malware | 115 | 2:25 | ____ | ☐ |
|   | **Break** | 10 | 2:35 | ____ | ☐ |
| 3 | B1. Intel | 25 | 3:00 | ____ | ☐ |
| 4 | B2. Threat model | 30 | 3:30 | ____ | ☐ |
| 5 | B3. Scans | 40 | 4:10 | ____ | ☐ |
|   | **Break** | 10 | 4:20 | ____ | ☐ |
| 6 | B4. Attacks | 40 | 5:00 | ____ | ☐ |
| 7 | Tidy, log, upload | 50 | 5:50 | ____ | ☐ |
| 8 | Buffer or extras | 10 | 6:00 | ____ | ☐ |

## Quick ticks

**1 Start (30)** ☐ folders ☐ brief read, verbs highlighted ☐ rules of engagement written ☐ VM snapshots `clean` ☐ app running, `test_sync.sh` 10 PASS ☐ Nessus activating ☐ sample downloaded in VM ☐ M57-Jean hashed

**2 Malware (115)** ☐ A1 safe setup + SHA-256 ☐ A2 triage + strings ☐ A3 sandbox run + screenshots ☐ A4 static vs dynamic ☐ A5 verdict + YARA + CareLink actions ☐ VM reverted

**3 to 5 Threats (95)** ☐ B1 method, sources, 3 threats ☐ B2 diagram + STRIDE ☐ B3 nmap ☐ Nikto ☐ dirb ☐ Burp ☐ Nessus export

**6 Attacks (40)** ☐ SQLMap ☐ 200 wrong tokens ☐ abuse table ☐ one fix retested ☐ DB cleaned

**7 Wrap (50)** ☐ evidence log complete ☐ hashes noted ☐ sample removed from upload ☐ upload done and confirmed ☐ Autopsy opens ☐ Friday sticky note

**Extras (only if ahead)** ☐ obfuscation / evasion ☐ own script edit ☐ process threats ☐ their mitigations

<div class="pb"></div>

# Sheet A: malware capture

**Sample**

::: {.tall}

| Item | Value |
| --- | --- |
| SHA-256 | |
| MD5 / SHA-1 | |
| Source and date | |
| VirusTotal family / detections | |
| File type and size | |
| Compile time (may be faked) | |
| Packed? Entropy | |
| Tool used for dynamic run | |

:::

**Sections and entropy**

::: {.tall}

| Section | Size | Entropy | Note |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |

:::

**ATT&CK techniques**

::: {.tall}

| ID | Technique | Tactic | Confirmed or suspected | Fig |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

:::

**IOCs**

::: {.tall}

| Type (IP, domain, URL, file, key, mutex) | Value | Seen in (static / dynamic) |
| --- | --- | --- |
| | | |
| | | |
| | | |
| | | |
| | | |

:::

<div class="pb"></div>

**Static vs dynamic**

::: {.taller}

| Behaviour | Static | Dynamic | Agree? |
| --- | --- | --- | --- |
| Starts processes / injects | | | |
| Persistence | | | |
| Network / C2 | | | |
| Files / data touched | | | |
| Evasion | | | |

:::

**Verdict (one line):** ________________________________________________

**Five headings** (how it gets in / runs / persists / talks out / hides):

::: {.taller}

| Heading | What I found | Fig |
| --- | --- | --- |
| Gets in | | |
| Runs | | |
| Persists | | |
| Talks out | | |
| Hides | | |

:::

**YARA:** hit on sample ☐   no hit on clean file ☐   What I changed: ____________________

**CareLink actions**

::: {.taller}

| Action | Detect, contain or mitigate | Links to my Ex1 control |
| --- | --- | --- |
| | | |
| | | |
| | | |
| | | |

:::

<div class="pb"></div>

# Sheet B: threats and attacks results

**Three threats (B1)**

::: {.taller}

| # | Threat | Asset | Source (rated A/B/C) | Ex1 control |
| --- | --- | --- | --- | --- |
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

:::

**Top 3 risks from STRIDE (B2)**

::: {.taller}

| Threat | Likelihood 1-5 | Impact 1-5 | Score | After controls |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |

:::

**Scans (B3). Target IP: ____________**

::: {.taller}

| Tool | Top finding | Real or false positive? | Action | Fig |
| --- | --- | --- | --- | --- |
| nmap | | | | |
| Nikto | | | | |
| dirb | | | | |
| Burp | | | | |
| Nessus | | | | |

:::

<div class="pb"></div>

**Attacks (B4)**

::: {.taller}

| Attack | Worked? | Impact if it had | Why it held / fix | Fig |
| --- | --- | --- | --- | --- |
| SQLMap | | | | |
| 200 wrong tokens | | | | |
| Read-only token writes | | | | |
| Revoked token | | | | |
| Expired token | | | | |
| Same note twice | | | | |
| 3 MB note | | | | |
| Malformed JSON | | | | |
| GET not POST | | | | |
| Token over plain HTTP | | | | |

:::

**Fix I applied and retested:** ____________________   Before: ____   After: ____

**IDOR / bad upload:** not applicable because ____________________

**Extras (item 12): process threats and mitigations**

::: {.taller}

| Process threat | Mitigation |
| --- | --- |
| Helpdesk reset | |
| Supplier access | |
| Leavers | |

:::

<div class="pb"></div>

# Sheet C: evidence log

**Hashes (record before opening anything)**

::: {.tall}

| Item | SHA-256 | Source | Date |
| --- | --- | --- | --- |
| Malware sample | | | |
| M57-Jean image | | | |

:::

::: {.tall}

| Fig | What it shows | File name | Used in |
| --- | --- | --- | --- |
| 01 | | | |
| 02 | | | |
| 03 | | | |
| 04 | | | |
| 05 | | | |
| 06 | | | |
| 07 | | | |
| 08 | | | |
| 09 | | | |
| 10 | | | |
| 11 | | | |
| 12 | | | |
| 13 | | | |
| 14 | | | |
| 15 | | | |
| 16 | | | |
| 17 | | | |
| 18 | | | |
| 19 | | | |
| 20 | | | |

:::
