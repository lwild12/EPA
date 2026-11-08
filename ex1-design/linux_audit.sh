#!/usr/bin/env bash
# Quick Linux hardening audit (read-only). Prints PASS/WARN lines you can paste into evidence.
# Usage: sudo bash linux_audit.sh
# Makes NO changes to the system.

pass() { printf '[PASS] %s\n' "$1"; }
warn() { printf '[WARN] %s\n' "$1"; }

echo "== Linux hardening audit: $(hostname) $(date -Is) =="

# --- SSH ---
sshd_cfg=/etc/ssh/sshd_config
if [ -r "$sshd_cfg" ]; then
  grep -Eiq '^\s*PermitRootLogin\s+(no|prohibit-password)' "$sshd_cfg" && pass "SSH root login restricted" || warn "SSH PermitRootLogin not set to no"
  grep -Eiq '^\s*PasswordAuthentication\s+no' "$sshd_cfg" && pass "SSH password auth disabled (keys only)" || warn "SSH password auth enabled"
  grep -Eiq '^\s*Protocol\s+1' "$sshd_cfg" && warn "SSH protocol 1 enabled" || pass "SSH protocol 1 not enabled"
  grep -Eiq '^\s*MaxAuthTries\s+[1-4]\b' "$sshd_cfg" && pass "SSH MaxAuthTries <= 4" || warn "SSH MaxAuthTries not limited"
else
  warn "Cannot read $sshd_cfg (is sshd installed? run as root)"
fi

# --- Firewall ---
if command -v ufw >/dev/null 2>&1 && ufw status 2>/dev/null | grep -q "Status: active"; then
  pass "ufw active"
elif command -v nft >/dev/null 2>&1 && nft list ruleset 2>/dev/null | grep -q chain; then
  pass "nftables ruleset present"
elif command -v iptables >/dev/null 2>&1 && [ "$(iptables -S 2>/dev/null | wc -l)" -gt 3 ]; then
  pass "iptables rules present"
else
  warn "No active firewall detected"
fi

# --- Listening services ---
echo "-- Listening sockets (review each; disable what is not needed) --"
if command -v ss >/dev/null 2>&1; then ss -tulpn 2>/dev/null | sed -n '1,40p'; fi

# --- Accounts ---
awk -F: '($2=="" ){print "[WARN] empty password for user: "$1}' /etc/shadow 2>/dev/null
awk -F: '($3==0 && $1!="root"){print "[WARN] extra UID 0 account: "$1}' /etc/passwd
pass "Account checks done (no output above means no empty passwords / extra UID 0)"

# --- File permissions ---
for f in /etc/passwd:644 /etc/shadow:640 /etc/gshadow:640 /etc/group:644; do
  file=${f%%:*}; want=${f##*:}
  [ -e "$file" ] || continue
  have=$(stat -c %a "$file")
  if [ "$have" -le "$want" ]; then pass "$file perms $have"; else warn "$file perms $have (want <= $want)"; fi
done
wwdirs=$(find / -xdev -type d -perm -0002 ! -perm -1000 2>/dev/null | head -5)
[ -z "$wwdirs" ] && pass "No world-writable dirs without sticky bit (first 5 checked)" || { warn "World-writable dirs without sticky bit:"; echo "$wwdirs"; }

# --- Kernel / sysctl ---
chk() { v=$(sysctl -n "$1" 2>/dev/null); [ "$v" = "$2" ] && pass "$1 = $2" || warn "$1 = ${v:-unset} (want $2)"; }
chk net.ipv4.ip_forward 0
chk net.ipv4.conf.all.accept_redirects 0
chk net.ipv4.conf.all.send_redirects 0
chk net.ipv4.tcp_syncookies 1
chk kernel.randomize_va_space 2

# --- Updates / logging ---
if command -v apt >/dev/null 2>&1; then
  n=$(apt list --upgradable 2>/dev/null | grep -vc Listing)
  [ "$n" -eq 0 ] && pass "No pending apt updates" || warn "$n packages upgradable"
fi
systemctl is-active --quiet auditd 2>/dev/null && pass "auditd running" || warn "auditd not running"
systemctl is-active --quiet rsyslog 2>/dev/null || systemctl is-active --quiet systemd-journald 2>/dev/null && pass "logging service running"

echo "== done =="
