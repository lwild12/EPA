import re
import sqlite3
import sys

db = sys.argv[1] if len(sys.argv) > 1 else "own_traffic.db"
log = sys.argv[2] if len(sys.argv) > 2 else "vsftpd.log"

# Example line:  Tue Nov 17 11:20:03 2026 [pid 4209] [msfadmin] FAIL LOGIN: Client "192.168.56.101"
pat = re.compile(r'^(\w{3} \w{3}\s+\d+ [\d:]+ \d{4}) \[pid \d+\] (?:\[([^\]]*)\] )?FAIL LOGIN: Client "(?:::ffff:)?([0-9a-fA-F.:]+)"')

con = sqlite3.connect(db)
con.execute("DROP TABLE IF EXISTS auth_events")
con.execute("CREATE TABLE auth_events (logtime TEXT, service TEXT, username TEXT, src TEXT)")
rows = []
for line in open(log, errors="ignore"):
    m = pat.match(line)
    if m:
        rows.append((m.group(1), "vsftpd", m.group(2) or "", m.group(3)))
con.executemany("INSERT INTO auth_events VALUES (?,?,?,?)", rows)
con.commit()
print(len(rows), "failed FTP logins loaded into auth_events")
print(con.execute("SELECT src, COUNT(*) FROM auth_events GROUP BY src ORDER BY 2 DESC").fetchall())
