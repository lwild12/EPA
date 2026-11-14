> Text only. Screenshots are in `Ex2_Notes.docx`.

Agent Tesla – Infostealer

PE32 Executable .net assembly for MS windows

SHA256 699ec052ecc898bdbdafea0027c4ab44c3d01ae011c17745dd2b7fbddaa077f3

Infostealers like Agent Tesla target saved credentials, like the sign in details cached on the staff devices. These can present risk to <company> as this can provide an attacker with direct credentials that are known good for the <company> infrastructure

Infostealers are often delivered by mechanisms such as phishing emails, which rely on human interaction and susceptibility.



Very few imports, likely a packed sample. This limits the static view of the file.

sample checked in any.run and CAPEv2 sandbox





Static analysis and dynamic analysis match for the strings, but all other analysis is incomplete for the static analysis due to the packed nature of the sample.

How it gets in: Phishing email, malicious download

How it runs: It performs recon against the OS, user details and looks for credentials stored in tools like SFTP clients, browsers, email clients. Persistence is achieved by setting the registry key

HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run\xws to add xws.exe to the startup programmes.

It sends information gathered to a server that is controlled by the attacker(s).

It hides by utlising encrypted payloads, and by attempting to remove traces of file downloads etc.

Prevention:

Block IOCs for network traffic at the IP address and DNS level

EDR

Short lived tokens and MFA to limit the usability of stolen credentials. Use of conditional access/sign in risk if using Entra ID.

Small cache to restrict the data that is held on devices that infostealers could access

Isolate devices where suspicion of compromise. Revoke tokens and credentials associated with the user remote wipe.

Where a delivery vector has been identified, issue awareness messaging to staff, and block/moderate where appropriate


---

## Guidance: what to add next (one step at a time)

Tick each box as you go. Challenge points are my reading: check them against your sandbox output.

### 1. Static evidence: packed or not?
- [ ] Few imports is not proof of packing. A .NET assembly normally imports almost nothing (only mscoree.dll).
- [ ] Add stronger evidence: section entropy, or Detect It Easy output. Screenshot it.
- [ ] If you can, open the file in ILSpy or dnSpy. Readable code is better static evidence than "incomplete".

### 2. Persistence: check the exact keys
- [ ] As I understand it, StartupApproved\Run only records enabled or disabled. The entry that launches the program is normally in the Run key itself.
- [ ] Open the CAPE or Any.run registry output. Write down every key that was written.
- [ ] Note where xws.exe was copied to (the folder path).

### 3. Split the five mechanisms (the brief names them)
- [ ] Access: phishing or download. Say which one the sandbox showed.
- [ ] Execute: what launches, and from which process. Add the process tree figure.
- [ ] Persist: the key(s) from step 2.
- [ ] Communicate: protocol, destination domain or IP, port. Take these from the CAPE network tab. These are your IOCs.
- [ ] Evade: say what you saw (not just "encrypted payloads"), and how you got past it. This is the Merit item 9 point.
- [ ] Write "not seen" for anything the sandbox did not show.

### 4. Map to ATT&CK (candidates: confirm each against what you saw)
- [ ] Phishing: T1566
- [ ] Credentials from password stores: T1555
- [ ] Registry run keys: T1547.001
- [ ] Exfiltration over C2 channel: T1041
- [ ] Obfuscated files or information: T1027

### 5. Detection, not just prevention (the brief says detected, contained or mitigated)
- [ ] Detect: alert on a new startup registry entry.
- [ ] Detect: alert on workstations making outbound connections to unusual ports or mail servers.
- [ ] Detect: write one YARA rule from ex2-malware/rules/generic_triage.yar and test it.
- [ ] Contain: isolate the device, revoke tokens and credentials (already in your notes).
- [ ] Mitigate: short-lived tokens, MFA, conditional access, small cache (already in your notes). Link each to a <company> control from Ex1.

### 6. Compare static and dynamic
- [ ] Write two lines: where they agree (strings) and what each one missed.
- [ ] Say plainly that the packed sample limited static analysis.

### 7. Make the figures traceable
- [ ] Replace each [] placeholder with a numbered figure (Fig 1, Fig 2...).
- [ ] Log each in ex2-checklists/00_evidence_log.md with the tool and time.
- [ ] Mention every figure number in the text.

## How to check (tool steps)

Tab and menu names may differ slightly in your tool versions. Use them as a guide.

### 1. Communicate (CAPEv2)
- [ ] Open the CAPE report, go to the **Network** tab.
- [ ] Note DNS lookups, then TCP connections (destination IP and port).
- [ ] Look for ports 25, 465, 587 (SMTP), 21 (FTP), 80 or 443 (HTTP), or a Telegram API domain. These are the usual AgentTesla exfil routes, as far as I know.
- [ ] Check the **Payloads** or **Config** section. CAPE often extracts the AgentTesla config.
- [ ] Screenshot it and log it as a figure.
- [ ] If the config shows attacker credentials, black them out in your screenshot. Record the server or domain as an IOC. Do not log in to it.

### 2. Persistence (registry)
- [ ] CAPE: **Behavior Analysis**, find the registry keys written.
- [ ] Any.run: click the `xws.exe` process and check its registry events.
- [ ] Write down each full key path.
- [ ] Check whether `...\CurrentVersion\Run` is present, or only `StartupApproved\Run`.
- [ ] Note the folder path `xws.exe` was copied to.

### 3. Packed or not
- [ ] Open the sample in **Detect It Easy** (DIE), in your VM only.
- [ ] Note what it detects (compiler, .NET, any packer or obfuscator).
- [ ] Click **Entropy** and screenshot the graph. High entropy across a section suggests packed or encrypted.
- [ ] Open it in **ILSpy**. Readable class and method names suggest light obfuscation. Garbled names or a tiny loader are evidence of obfuscation or a packed payload.

### 4. Evasion (Merit item 9)
- [ ] CAPE: open **Signatures**.
- [ ] Note any about anti-VM, anti-debug, sleeping, or deleting files.
- [ ] For each, write what it means and how the sandbox still saw the behaviour.
- [ ] If none, write "not seen" and say why.

### 5. ATT&CK
- [ ] Any.run has a MITRE ATT&CK tab. CAPE lists techniques in its signatures.
- [ ] Keep only techniques you actually saw. Delete the rest of the candidates.

### 6. Detection rule
- [ ] Run `python3 ex2-malware/triage.py SAMPLE --yara ex2-malware/rules`.
- [ ] Copy a rule from `generic_triage.yar` and change it to match a string you found.
- [ ] Test that it matches your sample and does not match a clean file.
