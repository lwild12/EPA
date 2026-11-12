# Assurance strategy (template)

**Pass only. Time-box: 35 minutes.** Fill each part in short sentences. The text in brackets is a suggestion. Replace it with your own words.

**What the v4 pass criterion asks:** "Develop an assurance strategy for a defined system, selecting appropriate assurance approaches." The knowledge criterion also asks you to explain "trusted" versus "trustworthy", the main approaches, one extrinsic system, third-party testing and two intrinsic ways.

## 1. The system and what needs assuring (3 min)

- System: CareLink's clinician devices, the sync API, and the cloud care management system (SaaS).
- Needs assuring: ____ (patient records; clinician devices; the sync API).

## 2. Security objectives (3 min)

1. ____ (Patient data stays confidential.)
2. ____ (Only authorised devices and tokens connect.)
3. ____ (Infostealer activity is detected and contained quickly.)

## 3. Acceptance criteria (5 min)

Each must be measurable.

| ID | Criterion | How it is measured | Evidence |
| --- | --- | --- | --- |
| A1 | After [N] invalid tokens, further attempts are throttled or locked | Repeat the 200-token test | Test log |
| A2 | All clinician devices use full-disk encryption | Device inventory check | MDM report |
| A3 | EDR alerts on process injection | Run a safe test sample in a lab | Alert record |

Add one of your own: ____.

## 4. Trusted versus trustworthy (2 min)

- **Trusted** means we rely on it.
- **Trustworthy** means it deserves that reliance.
- Assurance is the evidence that closes the gap between the two: ____ (in your words).

## 5. The four approaches (7 min)

| Approach | What it is | Example for CareLink | When in the lifecycle |
| --- | --- | --- | --- |
| Design and implementation | Building security in and testing it | ____ (threat-led design; security tests on the sync API) | Design, build |
| Intrinsic | Assurance from inside the organisation | ____ (1) vulnerability scans and configuration reviews; ____ (2) code review before each release | Build, operate |
| Extrinsic | Independent assurance from outside | ____ (independent penetration test) | Before go-live, yearly |
| Operational policy and process | Ongoing rules and procedures | ____ (change control, incident response, supplier reviews) | Operate |

**Extrinsic example, benefits and limits (write both):**

- Benefits: independence; fresh eyes; credibility with the risk owner.
- Limits: point-in-time; limited scope; cost; needs fixing afterwards.

**Third-party testing:** gives the risk owner independent evidence that controls work, and finds problems the internal team may miss because they know the system too well. ____ (in your words).

## 6. Test plan (7 min)

Five rows or more.

| Test | Scope | Technique | Expected result | Owner | Evidence | Priority |
| --- | --- | --- | --- | --- | --- | --- |
| API token throttling | Sync API | Security-focused functional test | Throttled or locked after [N] invalid tokens | ____ | Test log, figure | High |
| Device configuration check | Clinician laptops and mobiles | Configuration testing | Encryption on; EDR running; lockout set | ____ | MDM report | High |
| Vulnerability scan | Sync API and test VM | Vulnerability assessment | No high-severity findings left open | ____ | Scan report | Medium |
| Phishing simulation | Clinicians | Simulated campaign | Few clicks; reports to security | ____ | Campaign report | Medium |
| Supplier assurance review | SaaS provider | Document review; independent test summary | Evidence of recent independent testing | ____ | Supplier evidence | Medium |

## 7. Prioritisation rule (1 min)

Test first what is most critical (patient records, clinician devices), most likely to be attacked (phishing, infostealers) and has the most severe known weakness (missing throttling). ____ (in your words).

## 8. Findings workflow and change (2 min)

Record, then rate, then fix, then retest. Each finding gets an ID, severity, owner, due date and retest result.

**Retest when:** a new release ships, the supplier changes, the threat picture changes (new intelligence), or a finding is fixed.

## Check before you stop

- ☐ Objectives, acceptance criteria and a test plan of 5 rows or more
- ☐ All four approaches named, with 2 intrinsic examples and 1 extrinsic example with benefits and limits
- ☐ "Trusted" versus "trustworthy" explained
- ☐ Third-party testing explained
- ☐ Findings workflow and retest triggers written
- ☐ Stop. It is pass only.
