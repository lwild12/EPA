# Ex1 justification: draft (target 900-1,100 words)

**How to use (read first)**
1. This is a draft built from your Notion plan, NOT from the real brief. I have not seen the brief.
2. Replace every `[BRACKET]` with the brief's real names, numbers and your own figure numbers.
3. Delete any sentence that is not true of what you actually built. Never claim a control you did not build or test.
4. Keep the six headings. Check the word count at 15:40 (only the text between the START and END lines counts).
5. Cut or add in section 3 first; it is the most flexible.

<!-- START DRAFT -->

## 1. Context and requirements

[ORGANISATION] needs a secure network, a hardened server and a web application for [PURPOSE]. The brief requires [REQUIREMENT 1], [REQUIREMENT 2] and [REQUIREMENT 3]. The most sensitive assets are [FINANCE/HR/PATIENT DATA], which must stay confidential, and [SERVICE], which must stay available. I assumed [ASSUMPTION], because the brief does not state it. The main threats I designed against are credential theft, malware spreading between departments, unauthorised access to [FINANCE/HR] data, and loss of [SERVICE] through failure or attack. Success means each requirement is met, tested and supported by evidence (Figures 1 to [N]), and that a non-technical manager can see why each control exists.

## 2. Options considered and why I chose one

For the network I compared two designs. Option A was a flat network with one subnet and a single router. It is simple and cheap, but any compromised device could reach every system, including [FINANCE]. Option B segmented each department onto its own VLAN and subnet, routed with OSPF, with access lists between zones. I chose Option B because the brief's confidentiality requirement needs isolation between departments, and one infected workstation would otherwise reach everything.

For routing I considered static routes only and OSPF. Static routes are predictable but do not adapt to a failed link. I used OSPF for resilience and kept one static route to [DESTINATION], as the brief requires both types. I also considered a dedicated firewall appliance. I rejected it because the brief gives no budget for one and router ACLs meet the requirement; I record the limitation in section 5.

I addressed the network using VLSM, largest subnet first, with about [20]% growth room (Figure 1). This used [X] of [Y] addresses and left space for expansion without renumbering.

## 3. Key design decisions and security rationale

**Network.** [FINANCE] and [HR] are protected by extended ACLs that permit only the services each group needs and log every denied attempt. This reduces lateral movement and gives evidence for monitoring. Management uses SSH version 2 only, with `enable secret`, a login banner and idle timeouts, because Telnet exposes credentials. Port security limits each access port to [2] MAC addresses and unused ports are shut down, which counters rogue devices and MAC flooding. OSPF authentication and `passive-interface` on user networks stop a rogue device injecting routes. Syslog and NTP provide time-aligned logs so incidents can be reconstructed. Each of these controls has a cost in convenience: administrators must use SSH keys or passwords and cannot manage devices from any subnet, which I accepted because management access is the highest-value target on a network.

**Server.** I chose [OS] because [REASON]. I recorded a baseline scan, hardened it, and scanned again to show the change (Figure [N]). Changes: least-privilege accounts with no remote root, a deny-by-default firewall, unused services removed, patches applied, disk encryption on, and password rules following NCSC guidance (length, no forced expiry, MFA where possible).

**Web application.** Passwords use `password_hash`. Prepared statements prevent SQL injection. A new session ID on login limits session fixation, and CSRF tokens protect state-changing requests. Uploads have a size cap, content type checking, random server-side names and storage outside the web root. Every file action checks the owner, which blocks insecure direct object references. A lockout slows brute force. File names are HTML-encoded to stop cross-site scripting.

**Cryptography and keys.** The application uses TLS. Uploaded files are encrypted at rest. The key plan covers creation, storage, sharing, rotation, revocation, backup and destruction, each with a named owner, following NIST SP 800-57.

## 4. Evidence that it works

Connectivity tests between every LAN succeed where permitted (Figure [N]). `show access-lists` shows the Finance deny rule matching a test from [LAN] (Figure [N]). `show ip route` shows OSPF and the static route (Figure [N]). I tested the application with an injection string, a path traversal, a wrong-owner download, a disallowed upload type and a script in a file name; each was rejected (Figure [N]). I also broke [FAULT] on purpose and fixed it by [FIX], which confirmed my understanding of how the design behaves. The server baseline scan found [N] findings and the second scan found [M], with the remaining items explained in Table [N] (for example, services the application needs). I did not test [WHAT YOU DID NOT TEST], so I make no claim about it. Evidence is numbered, labelled with the command or tool used, and shows the result on screen, so a marker can reproduce each test.

## 5. Residual risks and limitations

The ACLs are stateless in places, so a firewall would give stronger inspection. The hub I added for [REASON] allows sniffing on its segment, so sensitive hosts must not share it. The exam environment cannot reproduce [MPLS/INTERNET], so I modelled it with core routers. The application is secured for local testing; before internet exposure it needs a reverse proxy or WAF, a DMZ and monitored TLS configuration. Insider misuse by authorised users is reduced by logging and least privilege but not eliminated. Likelihood and impact scores are my judgement and should be reviewed (risk register, Table [N]). I accepted the remaining low risks, namely [RISK], because the cost of removing them exceeds the harm they could cause, and I recorded who owns that decision. The design also depends on administrators keeping configurations and patches current, so I recommend a documented change process and a quarterly configuration review.

## 6. Assurance and next steps

Controls apply at three layers: enterprise (policy, backups, training), network (segmentation, ACLs, port security) and application (input handling, sessions, encryption). Recovery uses 3-2-1 backups with an RPO of [X] and RTO of [Y]. The policy supports UK GDPR and the Data Protection Act 2018 (security of processing, breach reporting), the Computer Misuse Act 1990 and the NIS Regulations 2018, and [NON-UK LAW, e.g. EU GDPR] for [REASON]. To give the risk owner confidence I recommend an independent penetration test, Cyber Essentials Plus and, longer term, ISO/IEC 27001 certification, with quarterly reviews of the risk register. I would also add [EXTRA CONTROL] because [REASON].

<!-- END DRAFT -->

## Grade-item check (tick before you submit)
- [ ] Item 2: rejected option and why (section 2), fault fixed (section 4)
- [ ] Item 19: controls named at enterprise, network and application layers (section 6 and 3)
- [ ] Item 20: extra controls and the named assurance standard (section 6)
- [ ] Every claim has a figure number and every figure is mentioned
- [ ] Sources named: NCSC, NIST SP 800-57, OWASP, ISO 27001
- [ ] One non-UK jurisdiction included (the brief requires it)
