# Ex4: Defensive programming

Three parts. Do whichever the brief asks for first.

## python/ (secure code)
1. `pip install pytest`
2. `python3 -m pytest -v test_vuln_examples.py` shows each exploit working, then blocked.
3. Open `vuln_examples.py`. Each pair has the CWE, the attack and the fix in its comment. Reuse these in your write-up.

## c-debug/ (GDB, Valgrind, sanitizers)
1. `make` builds everything (Linux or WSL).
2. Run a bug: `valgrind --leak-check=full ./memory_bugs 2` (bugs 1 to 5), `./memory_bugs_asan 6` after `make asan`.
3. Find the line with GDB: `gdb ./memory_bugs` then `run 2`, `bt`, `print *p`.
4. Fix it, compare with `memory_bugs_fixed.c`, re-run clean.
5. Races: `make tsan && ./race_tsan`, or `valgrind --tool=helgrind ./race`. Fix is the `-DFIXED` mutex build.

Valgrind does not run on Windows. If the machine is Windows without WSL, say so in your write-up and use `-fsanitize=address` with MinGW or the debugger instead.

## mips/ (assembler)
1. Open the `.asm` in MARS or SPIM and run it. Expected output is in each file's header.
2. Read the comments, then change one thing (different array, different size) and predict the output before running.
3. `safe_copy.asm` is the defensive one: bounds check, always terminate, return a truncation flag.

You can also run the programs without MARS: `python3 mips_mini.py sum_array.asm`. It only supports a subset, so confirm in the real tool.
