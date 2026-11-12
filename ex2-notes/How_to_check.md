# Ex2: how to check each point (AgentTesla)

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
