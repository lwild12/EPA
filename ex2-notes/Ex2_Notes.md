Agent Tesla – Infostealer

PE32 Executable .net assembly for MS windows

SHA256 699ec052ecc898bdbdafea0027c4ab44c3d01ae011c17745dd2b7fbddaa077f3

Infostealers like Agent Tesla target saved credentials, like the sign in details cached on the staff devices. These can present risk to CareLink as this can provide an attacker with direct credentials that are known good for the CareLink infrastructure

Infostealers are often delivered by mechanisms such as phishing emails, which rely on human interaction and susceptibility.

<img src="media/image1.png" style="width:6.26806in;height:8.75556in" /><img src="media/image2.png" style="width:1.46895in;height:0.38547in" />

Very few imports, likely a packed sample. This limits the static view of the file.

sample checked in any.run and CAPEv2 sandbox

<img src="media/image3.png" style="width:5.8654in;height:3.4484in" /><img src="media/image4.png" style="width:6.26806in;height:3.01875in" /><img src="media/image5.png" style="width:6.26806in;height:3.17361in" /><img src="media/image6.png" style="width:6.26806in;height:1.78958in" /><img src="media/image7.png" style="width:6.26806in;height:6.08125in" />

<img src="media/image8.png" style="width:6.26806in;height:2.08819in" /><img src="media/image9.png" style="width:6.26806in;height:4.66389in" />

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
