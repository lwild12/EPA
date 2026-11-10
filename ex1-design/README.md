# Ex1: Design (network, hardening, web app)

Do these in order. Each step is small.

1. **Read the brief.** Note user counts per LAN and any security requirements.
2. **Plan addresses.** Run:
   `python3 vlsm_calc.py 192.168.0.0/22 "Staff=120" "Guest=60" "Servers=30" "WAN=2" --growth 0.2 --markdown`
   Paste the table into your write-up. Use the brief's numbers, not these.
3. **Build in Packet Tracer.** First get links and routing working with `packet_tracer_setup.md` (router-to-router link, ISP/cell tower, default route, troubleshooting). Then harden using `cisco_hardening.md`: base hardening, then VLANs, ACLs, port security.
4. **Collect evidence.** Run the `show` commands at the bottom of `cisco_hardening.md`. Screenshot each.
5. **Linux server (if asked).** `sudo bash linux_audit.sh` (read-only). Fix each WARN, re-run, keep both outputs.
6. **Web app (if asked).** In `php-upload/`: `php -S 127.0.0.1:8080 app.php`. Test with `bash test_app.sh`. Needs PHP 8 and the `fileinfo` extension.
7. **Write it up.** For each control: decision, threat it stops, evidence, alternative, residual risk (see `../templates/justification_and_grading.md`).

If PHP is not installed and you cannot install it, describe the app's controls from `app.php` comments and say which you did not run.
