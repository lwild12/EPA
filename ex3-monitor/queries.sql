-- Exercise 3 queries. Run:  sqlite3 traffic.db < queries.sql   (or paste into DB Browser for SQLite)
-- For each result, write what it shows and what you would do next.

-- 1. Top talkers by bytes sent
SELECT src, COUNT(*) AS packets, SUM(length) AS bytes
FROM packets GROUP BY src ORDER BY bytes DESC LIMIT 10;

-- 2. Protocol breakdown
SELECT proto, COUNT(*) AS packets, SUM(length) AS bytes,
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM packets), 1) AS pct
FROM packets GROUP BY proto ORDER BY packets DESC;

-- 3. PORT SCAN: sources that sent SYNs to many distinct ports on one host
SELECT src, dst, COUNT(DISTINCT dport) AS distinct_ports, COUNT(*) AS syns
FROM packets WHERE proto = 'TCP' AND flags = 'S'
GROUP BY src, dst HAVING distinct_ports > 50 ORDER BY distinct_ports DESC;

-- 4. Scan success rate: SYN sent vs SYN-ACK answered (low ratio = scanning closed ports)
SELECT src, SUM(syn) AS syns, SUM(synack) AS answered_by_target
FROM (
  SELECT src, dst, 1 AS syn, 0 AS synack FROM packets WHERE flags = 'S'
  UNION ALL
  SELECT dst AS src, src AS dst, 0, 1 FROM packets WHERE flags = 'SA'
) GROUP BY src HAVING syns > 50 ORDER BY syns DESC;

-- 5. BRUTE FORCE: many connections from one source to the same service port
SELECT src, dst, dport, COUNT(*) AS attempts
FROM packets WHERE proto = 'TCP' AND flags = 'S' AND dport IN (21, 22, 23, 3389, 445)
GROUP BY src, dst, dport HAVING attempts > 20 ORDER BY attempts DESC;

-- 6. EXFILTRATION: largest outbound byte totals to non-private destinations
SELECT src, dst, dport, SUM(length) AS bytes, COUNT(*) AS packets
FROM packets
WHERE dst NOT LIKE '10.%' AND dst NOT LIKE '192.168.%' AND dst NOT LIKE '172.16.%'
GROUP BY src, dst, dport ORDER BY bytes DESC LIMIT 10;

-- 7. Rare destinations: hosts contacted by exactly one source (candidate C2/one-off)
SELECT dst, COUNT(DISTINCT src) AS sources, SUM(length) AS bytes
FROM packets GROUP BY dst HAVING sources = 1 ORDER BY bytes DESC LIMIT 10;

-- 8. DNS: most queried names and hosts with the most unique queries (tunnelling / DGA hint)
SELECT dns_query, COUNT(*) AS n FROM packets WHERE dns_query <> '' GROUP BY dns_query ORDER BY n DESC LIMIT 10;
SELECT src, COUNT(DISTINCT dns_query) AS unique_names FROM packets WHERE dns_query <> '' GROUP BY src ORDER BY unique_names DESC LIMIT 5;

-- 9. Timeline: packets per 10-second bucket (spikes mark attacks)
SELECT CAST((ts - (SELECT MIN(ts) FROM packets)) / 10 AS INT) * 10 AS seconds_from_start, COUNT(*) AS packets
FROM packets GROUP BY 1 ORDER BY 1;

-- 10. Resets (closed ports/refused connections) by source
SELECT dst AS responder, src AS client, COUNT(*) AS resets FROM packets WHERE flags LIKE '%R%' GROUP BY dst, src ORDER BY resets DESC LIMIT 10;
