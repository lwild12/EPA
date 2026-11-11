# D. Legal, ethics and evidence (time-box: 1.5 hours)

**Done when:** you have rules of engagement, legal duties named, evidence handling described, and an IR outline.

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

## Step 5. IR plan (30 min)
The older v4 brief asks for a **comprehensive** plan covering:
- [ ] The role and responsibilities of **each team member**.
- [ ] Procedures for **collecting and analysing data**.
- [ ] Measures that protect **privacy and confidentiality**.
- [ ] Legal and ethical requirements for IR: data protection law, privacy, confidentiality and relevant industry standards.
- [ ] Securing evidence so it could support legal proceedings.

- [ ] Start from `templates/incident_response_plan.md`.
- [ ] Keep to: roles, severity, the 6 lifecycle steps, evidence handling, notification.
- [ ] Add the ransomware / infostealer playbook that matches your sample.
