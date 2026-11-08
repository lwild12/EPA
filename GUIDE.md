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
