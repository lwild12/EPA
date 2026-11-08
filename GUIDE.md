# EPA day guide

This is a plan, not an answer. Your brief overrules everything here. I have not seen the brief, so write-up content has to come from the tasks it sets.

## Tonight (20 minutes)
1. Send the "still open" email: are own devices, installs and USB allowed, and can you set up before 09:30?
2. Test your Blackboard, VirusShare, GitHub and Cisco logins on your phone.
3. Put this repo link and the zip somewhere you can reach offline.
4. Sleep. A rested six hours beats extra revision.

## First 20 minutes at the machine
1. Read the whole brief once without touching anything.
2. Highlight every verb (design, justify, evaluate, test). Each verb is a marker's checkbox.
3. Write your own checklist of required outputs per exercise.
4. Start a timer. Take breaks at the times your notes say, and send the break emails.
5. Set up the tools (below), then start.

## Setup (10 minutes, only if installs are allowed)
1. `git clone https://github.com/lwild12/EPA` (or unzip the USB copy).
2. `pip install -r requirements.txt`
3. Confirm one command from each folder runs. If something fails, skip it and use the manual route; do not debug the kit during the exam.

## Running each exercise
Time-box each part. If a task stalls for 20 minutes, note it and move on.

- **Ex1 Design:** plan addresses first (`vlsm_calc.py`), then devices, then ACLs, then evidence. Screenshots as you go, not at the end.
- **Ex2 Malware:** sample hash first, static triage, sandbox, then compare the two. Lab VM only.
- **Ex3 Monitoring:** pcap to SQLite, run queries, run the analysis, link each finding to a risk row.
- **Ex4 Code:** run the failing case first, find the cause with the debugger, fix, show it passes.

Each folder has a README with the exact commands.

## Writing it up (the part that decides your grade)
Your target is Merit. That means every criterion passed and each grade item shown at Merit level. For every decision write five short parts:
1. What you chose.
2. The threat or requirement it answers.
3. Your evidence (numbered figure).
4. One alternative and why you rejected it.
5. What risk is left.

Use the scaffold in `templates/justification_and_grading.md` and paste your brief's exact criterion wording above each answer. Short, evidenced paragraphs beat long general ones.

## Rules to remember
- Submit to Blackboard. The end-of-day upload is final, so upload a good draft by mid-afternoon and improve it.
- Pre-written scripts from a public repo are allowed, but the Distinction-level scripting criterion likely needs your own work. Edit the tools visibly and say what you changed. Cite the repo anyway; it costs one line.
- No malware samples in the repo and none on host machines.
- Mention a limitation honestly. Markers read "this does not cover X" as understanding.

## Last 30 minutes each day
1. Re-read the brief's output list against your files.
2. Check every figure is numbered and mentioned in the text.
3. Check hashes, commands and sources are recorded.
4. Upload. Confirm the upload shows as submitted.

## If something goes wrong
- **Tool will not install:** describe what you would do and show the closest evidence you can produce. Say it plainly.
- **No pcap given:** capture VM-to-VM traffic; practise once if you can.
- **Short on time:** finish every Pass criterion first, then add Merit evidence where cheapest.
- **Panic:** stop, drink water, re-read the verb list.

## Honest limits of this kit
Snort rules and the MIPS programs were not tested in real Snort or MARS/SPIM. Valgrind needs Linux. The templates are starting points; marks come from your reasoning on the brief's scenario.

## Worked example paragraphs (practice data only: replace with your own evidence)
These show the five-part shape. Do not paste them; your marker needs your scenario and your figures.

**Ex1 design:** "I segmented students onto VLAN 20 and applied an inbound ACL (Figure 4) that permits only HTTPS and DNS to named servers and logs everything else to the server VLAN. This addresses the brief's requirement that students must not reach staff systems, and limits lateral movement if a student device is compromised. `show access-lists` (Figure 5) shows the deny rule matching during a test ping. I considered a firewall appliance but rejected it because the brief gives no budget for one and a router ACL meets the requirement. The residual risk is that an ACL is stateless for return traffic, so I would add zone-based filtering in a larger network."

**Ex2 malware:** "Static triage (Figure 7) showed a high-entropy `.data` section, few imports and a writable and executable section, which suggests packing. The imports of `VirtualAllocEx` and `WriteProcessMemory` map to process injection (T1055), but imports show capability, not use. The sandbox run (Figure 9) confirmed a remote thread in `explorer.exe`, so I rate the injection finding as confirmed. I wrote a YARA rule on the two API names and a section name; it matched the sample and not a clean binary (Figure 10). It could be evaded by dynamic API resolution, so I would pair it with behaviour-based detection."

**Ex3 monitoring:** "A SYN-count query (Figure 12) showed one source sending SYNs to 400 distinct ports on one host in under a minute, which is a port scan. A second query showed the same source making 61 connections to port 22, consistent with brute force. Z-score analysis flagged the source as 3.4 standard deviations above the mean for port diversity. I scored the risk 16 (likelihood 4, impact 4) and recommend rate limiting and key-only SSH. The busiest internal host also appears as an outlier because it is the server; I excluded it as expected behaviour, which shows why a baseline is needed."

**Ex4 code:** "The vulnerable `read_file` accepted `../secret.txt` and returned a file outside the public directory (test output, Figure 14). I fixed it by resolving the real path and rejecting any path not inside the base directory. The test now raises a permission error and the normal file still loads (Figure 15). An allow-list of filenames would be stricter, but the application needs dynamic names, so I chose path resolution. Symlinks inside the base directory could still point outside; `realpath` handles that, and I would also run the service with a read-only mount."

## Final check before you submit
1. Did you answer every verb you highlighted?
2. Does each claim have a figure number?
3. Did you say where something is adapted from a public repo?
4. Is anything you could not run clearly stated as not run?
