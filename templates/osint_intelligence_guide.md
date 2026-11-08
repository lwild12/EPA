# Intelligence analysis and OSINT quick reference

## 1. Intelligence cycle
Direction (what question?) -> Collection -> Processing -> Analysis -> Dissemination -> Feedback.
Write the **intelligence requirement** first: "Is IP 203.0.113.50 linked to known malicious activity, and should we block it?"

## 2. Source and information grading (Admiralty / NATO 4x4 or 6x6)
| Source reliability | Meaning | | Information credibility | Meaning |
|---|---|---|---|---|
| A | Completely reliable | | 1 | Confirmed by other sources |
| B | Usually reliable | | 2 | Probably true |
| C | Fairly reliable | | 3 | Possibly true |
| D | Not usually reliable | | 4 | Doubtful |
| E | Unreliable | | 5 | Improbable |
| F | Cannot be judged | | 6 | Cannot be judged |
Grade the source AND the item separately (e.g. "B2": usually reliable source, probably true).

## 3. Confidence language (UK PHIA probability yardstick, use consistently)
Remote chance (<5%), highly unlikely (10-20%), unlikely (25-35%), realistic possibility (40-50%), likely/probable (55-75%), highly likely (80-90%), almost certain (>95%).
Add a confidence level (low / moderate / high) for the *assessment*, separate from the probability.

## 4. Analytic techniques
- **ACH** (Analysis of Competing Hypotheses): list hypotheses, list evidence, mark consistent/inconsistent, focus on what DISPROVES.
- **Diamond Model:** adversary - capability - infrastructure - victim.
- **Cyber kill chain / MITRE ATT&CK:** place observed behaviour in stages and techniques.
- **Pyramid of Pain:** hashes (trivial for attacker to change) < IPs < domains < tools < TTPs (hardest). Prefer detections on TTPs.
- **Bias checks:** confirmation, anchoring, mirror-imaging, availability. Use a devil's advocate or red-team question.

## 5. OSINT sources (passive, legal, ethical)
| Need | Sources |
|---|---|
| IP / domain | WHOIS/RDAP, passive DNS (e.g. SecurityTrails), crt.sh certificate transparency, Shodan/Censys, URLhaus |
| File hash / URL | VirusTotal, MalwareBazaar, Hybrid Analysis, any.run public reports |
| Vulnerabilities | NVD, CISA KEV, vendor advisories, EPSS |
| Threat reporting | NCSC, CISA, vendor blogs, MITRE ATT&CK groups |
| People / orgs | Company registries (Companies House), professional sites; follow data-protection and ethics rules |
| Archives | Wayback Machine |

## 6. Legal and ethical rules
Only collect what is lawful and proportionate; do not access systems or accounts you are not authorised for; do not use deception that breaches terms or law; handle personal data under UK GDPR / DPA 2018 (data minimisation, purpose limitation); record sources for auditability; apply TLP markings (CLEAR, GREEN, AMBER, AMBER+STRICT, RED) when sharing.

## 7. Documenting findings (indicator record)
| Indicator | Type | First seen | Source (grade) | Context | Confidence | Action |
|---|---|---|---|---|---|---|
| 203.0.113.50 | IP | <date> | <source> (B2) | Received 900 KB upload from 10.0.0.25 | Moderate | Block, investigate host |

## 8. Product format (BLUF)
**Bottom line up front** (1-2 sentences) -> key judgements with probability and confidence -> evidence -> gaps -> recommendations.
