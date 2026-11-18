import time
from alert_triage import triage

for n in (1_000, 10_000, 100_000):
    alerts = [{"source": "ids", "type": "t%d" % (i % 50), "asset": "laptop",
               "severity": 3, "time": i} for i in range(n)]
    start = time.perf_counter()
    triage(alerts)
    print(f"{n:>8} alerts: {time.perf_counter() - start:.3f} seconds")
