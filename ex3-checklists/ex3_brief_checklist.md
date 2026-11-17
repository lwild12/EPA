# Ex3 brief checklist (mapped to the v11 brief)

Use this to check you have attempted **every yellow topic**. The guide section for each is in brackets. Tick a box only when the evidence exists and has a figure number.

## The 8 mandatory topics

### 1. Apply statistical techniques to large data sets. Identify vulnerabilities in big data architectures and deployment. [Guide A]

- ☐ Large **heterogeneous** data sets identified (CIC-IDS2017 slice, own pcap, login log) and sources named
- ☐ Database designed and set up (tables, keys, a join across sources)
- ☐ Security questions that statistics can answer written down
- ☐ Statistical techniques chosen and baseline of normal activity set (z-score, IQR, KMeans)
- ☐ Anomalies or patterns investigated, with evidence
- ☐ Architecture of collection, storage and processing described
- ☐ Weaknesses at ingestion, interfaces, access control, storage, processing, APIs, deployment
- ☐ Effect on confidentiality, integrity, availability or reliability of data and monitoring

### 2. Undertake ethical system reconnaissance and intelligence analysis. [Guide B]

- ☐ Scope and objectives defined, and what is legitimately in scope
- ☐ Intelligence gathered from authorised or public sources only
- ☐ Contradictory sources analysed, provenance considered, a likely picture hypothesised
- ☐ Target profiled and potential weaknesses identified legally
- ☐ Information organised and correlated into an attack surface view
- ☐ Technologies, services, dependencies and third parties listed
- ☐ Potential attack paths and areas for further investigation
- ☐ Confirmed vs assumed vs needs-validation separated
- ☐ Authorised, proportionate and compliant (stated)

### 3. Undertake risk modelling, analysis and trades. [Guide D]

- ☐ Assets, threats, vulnerabilities and impacts identified
- ☐ Risk model showing relationships (threat, vulnerability, asset, likelihood, consequence)
- ☐ One consistent scoring approach, assumptions and limitations stated
- ☐ Treatment options for significant risks (technical, procedural, monitoring, design)
- ☐ Trade-offs (security, cost, usability, performance, availability)
- ☐ Alternatives compared and decisions justified with evidence
- ☐ Residual risks and further actions
- ☐ Cyber risk related to business and operational risk, with costs and value-for-money judgement (Pass)
- ☐ Asset values, risk appetite and tolerance, treatment types (mitigate, transfer, accept, avoid)
- ☐ A system modelling method applied (STRIDE, CVSS, SABSA, DBSy or NIST 800-154) (Pass)
- ☐ Architectural model (UML-style) integrated with the enterprise model (Pass)
- ☐ **MERIT:** two methods used, and compared and contrasted for their effect on the risk analysis
- ☐ **DISTINCTION:** investment options identified from the comparison and modelling

### 4. Undertake risk assessment to an external standard. [Guide E]

- ☐ Recognised standard chosen and why
- ☐ Scope, assets, assumptions, dependencies and criteria set before assessing
- ☐ Threats, vulnerabilities, likelihood and impact assessed in the standard's way
- ☐ Records clear enough for another person to repeat
- ☐ Risks mapped to controls or treatment, gaps identified
- ☐ Residual risk, limitations, assumptions and further work documented
- ☐ Evidence that the standard was followed

### 5. Apply a management system and develop an information security management plan. [Guide F]

- ☐ Organisational context, assets, stakeholders, responsibilities, objectives
- ☐ Management approach: roles, policies, processes, reporting
- ☐ Key risks turned into measurable objectives or actions
- ☐ Plan covers risk treatment, access management, monitoring, incident management, training, continual improvement
- ☐ How controls are implemented, measured, reviewed and improved
- ☐ Measures or indicators for the objectives
- ☐ Feedback from changes in organisation, technology, threats and regulation

### 6. Security monitoring, analysis and intrusion detection. Recognise anomalies and behaviours. [Guide C]

- ☐ Events and data sources to monitor
- ☐ Normal behaviour and suspicious characteristics
- ☐ Monitoring and detection designed or configured (Snort, queries)
- ☐ Rules, alerts or detection logic for threats and behaviours
- ☐ Unusual events analysed, incidents separated from benign activity
- ☐ Multiple sources correlated and compared with known threat and vulnerability data
- ☐ Anomalies inspected at packet, protocol and log level; impact characterised
- ☐ Alerts prioritised, recorded, escalated and used to improve detection

### 7. Manage intrusion response, including with third parties. [Guide G]

- ☐ Approach: identification, triage, containment, eradication, recovery, post-incident review
- ☐ Roles, responsibilities, escalation, decision authority
- ☐ Severity and priority criteria, and when to ask for specialist help
- ☐ Role of third parties (cloud, managed security, suppliers, external teams)
- ☐ Secure sharing of information and evidence
- ☐ Communication, reporting and notification obligations
- ☐ Response exercise conducted or designed, improvements identified
- ☐ Local response to a non-major incident follows a defined procedure
- ☐ Escalation message to an external team written; evidence preservation covered

### 8. Written justification (1,000 plus or minus 100 words). [Guide H, `ex3_justification.md`]

- ☐ Word count between 900 and 1,100
- ☐ Covers every topic above
- ☐ Every figure number appears in the text
- ☐ Honest about pre-written tools and what was not run

## The 7 knowledge areas the brief says your work must evidence

| Knowledge area | Where it shows |
| --- | --- |
| Information management, big data, statistics, databases, data quality | A3 to A6 (SQL, baseline, missing and infinite values) |
| Structured and ethical intelligence analysis | B |
| Management of cyber risk, tools and techniques | D, E |
| Quantitative and qualitative risk theory, role of risk stakeholders | D (ALE row, scales), F (roles) |
| Security management systems, governance, international standards | E, F (ISO/IEC 27005, 27001) |
| Diagnosing cause from observables, SIEM | C4 (correlation table) |
| Incident response, escalation, investigation, third parties | G |

## Grade criteria from your v4 table (Annex 1, Ex3 rows)

**Only risk modelling has Merit and Distinction. Every other Ex3 row is "Not applicable" for Merit and Distinction.** So Pass on everything, plus Merit and Distinction in D.

| Item | Pass | Merit | Distinction | Done where |
| --- | --- | --- | --- | --- |
| TC3 Statistics, big data | Statistics on large heterogeneous data sets; vulnerabilities in big data architectures; design and set up a database | n/a | n/a | A |
| TC14 Recon and intelligence | Analyse contradictory sources, consider provenance, profile a target legally, critical thinking | n/a | n/a | B |
| TC15 Risk modelling and trades | Cyber risk related to other risk classes; costs and trade-off business case; one modelling method; architectural model integrated with enterprise model | **Two methods compared and contrasted** (SABSA, DBSy, CVSS, STRIDE, NIST 800-154) | **Investment options** identified from the comparison | D |
| TC16 Risk assessment to a standard | Assessment against a recognised standard with a recognised methodology; remediation advice | n/a | n/a | E |
| TC17 Management system and plan | Follow policies and SLAs; ISMS plan for a defined business area per ISO 27001 or similar | n/a | n/a | F |
| TC22 Monitoring and detection | Recognise anomalies in packets, protocols, logs, alerts; correlate sources; compare to threat data; characterise impact | n/a | n/a | C |
| TC23 Intrusion response | Manage local response to non-major incidents by procedure; communicate with internal and external teams | n/a | n/a | G |
| Knowledge 3, 14, 15, 16, 17, 22, 23 | Understand the topics in the brief's knowledge list | KU15 Merit: employ one method to inform risk analysis | KU15 Distinction: options for investment | A to G |
