# D. Legal, ethics and evidence (time-box: 1.5 hours)

**Brief topic 4:** Organise testing and investigation work in accordance with legal and ethical requirements.

**Done when:** you have rules of engagement (scope and authorisation), legal duties named, evidence handling described, safe testing procedures and an auditable record.

Brief prompts this file covers: scope, authorisation and boundaries; legal, regulatory, organisational and contractual requirements; handling of sensitive information, credentials, malware and evidence; safe testing procedures (rules of engagement, test environments, access controls, backup/recovery, escalation); an auditable record of activities, evidence, decisions and findings.

## Step 1. Rules of engagement (do this FIRST, tonight)
Fill in and keep as a half page:

| Item | Your answer |
|---|---|
| Who authorises the testing? | (you, as the learner, for your own lab; say so) |
| What is in scope? | My Ex1 prototype app, my lab VMs, the malware sample in the VM, the M57-Jean image |
| What is out of scope? | Any real CareLink or employer system, any live service, any other person's system |
| Where is it done? | Isolated lab VM / local machine, no real personal data |
| What is allowed? | Scans, injection tests, brute force against my own app only |
| Backup / recovery | VM snapshots before each test; revert after |
| Stop and escalate | Stop if anything touches a system outside scope; tell my coach |
| Record keeping | Evidence log with times; hashes of samples and images |

## Step 2. Legal (30 min)
Use `templates/uk_legal_reference.md`. Name the duty each control or activity supports.
- [ ] Computer Misuse Act 1990: why you only test what you own or are authorised to test.
- [ ] UK GDPR and DPA 2018: security (Art. 32), breach notification (Art. 33, where feasible within 72 hours).
- [ ] Regulator: the **Information Commission** (succeeded the ICO on 30 Sep 2026). Mention the change once.
- [ ] Caldicott principles and the DSPT for health and care data.
- [ ] Do not lean on NIS 2018 unless you can justify it: the gov.uk health guide I found does not list social or community care providers as in scope.

## Step 3. Evidence (20 min)
- [ ] ACPO / NPCC digital evidence principles: do not change the original.
- [ ] Hash first, work on a copy, log who/what/when (chain of custody).
- [ ] How malware, credentials and personal data are stored during the work (VM only, no real data).

## Step 4. Ethics (10 min)
- [ ] Cite one recognised professional body's code (BCS or CIISec) and the ethical duties of a cyber security professional.
- [ ] Say how law applies to **intelligence collection and analysis**: data protection, human rights and privacy.
- [ ] Say how law applies to testing third parties (ethical hacking, pen testing): authorisation first.

## Step 5. Auditable record (15 min)
The brief wants work you can show was **authorised, proportionate and professionally conducted**.
- [ ] Evidence log (`00_evidence_log.md`) has a time for every action.
- [ ] Decisions recorded with a one-line reason (for example why you chose this sample).
- [ ] Findings recorded, with what you did about each.

## Optional extras (not in the v11 Ex2 brief)
- **Incident response plan:** the v11 brief puts this in **Ex3**, not Ex2. The older v4 pack listed it in Ex2. Only do it here if your live brief asks. Start from `templates/incident_response_plan.md`.
- **Autopsy / M57-Jean:** good supporting evidence for chain of custody. See `ex2-autopsy/README.md`. Do it after all five topics are done.
