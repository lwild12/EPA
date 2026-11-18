"""Company alert triage (Ex4, Script B): the algorithm.

Problem : alert fatigue. Hundreds of repeated alerts hide the real incidents.
Input   : list of alerts, each a dict:
            source (str), type (str), asset (str), severity (int 1-5), time (epoch seconds)
Output  : {"incidents": [...top N, highest score first...], "rejected": number of bad alerts}
Grouping: same (source, type, asset) within WINDOW seconds of the group's first alert = one incident.
Score   : severity x asset criticality x log(count + 1)
Safety  : bad alerts are counted and skipped; open groups are capped so a flood
          of unique alerts cannot use unlimited memory.
"""
import heapq
import math

WINDOW = 600            # 10 minutes
MAX_OPEN_GROUPS = 50_000
TOP_N = 100
CRITICALITY = {"patient-db": 5, "sync-api": 4, "laptop": 2}   # unknown assets = 1
MAX_TEXT = 128


def _valid(a):
    try:
        return (
            all(isinstance(a[k], str) and 0 < len(a[k]) <= MAX_TEXT for k in ("source", "type", "asset"))
            and isinstance(a["severity"], int) and not isinstance(a["severity"], bool)
            and 1 <= a["severity"] <= 5
            and isinstance(a["time"], (int, float)) and not isinstance(a["time"], bool)
            and math.isfinite(a["time"])
        )
    except (KeyError, TypeError):
        return False


def _score(group):
    crit = CRITICALITY.get(group["asset"], 1)
    return group["severity"] * crit * math.log(group["count"] + 1)


def triage(alerts, window=WINDOW, max_open=MAX_OPEN_GROUPS, top_n=TOP_N):
    rejected = 0
    good = []
    for a in alerts:
        if _valid(a):
            good.append(a)
        else:
            rejected += 1
    good.sort(key=lambda a: a["time"])          # O(n log n): this is the slowest step

    open_groups = {}                            # key -> group (dicts keep insertion order)
    best = []                                   # min-heap holding the top_n incidents
    counter = 0                                 # tie-breaker so heap never compares dicts

    def close(group):
        nonlocal counter
        counter += 1
        item = (_score(group), counter, group)
        if len(best) < top_n:
            heapq.heappush(best, item)
        else:
            heapq.heappushpop(best, item)

    for a in good:
        key = (a["source"], a["type"], a["asset"])
        group = open_groups.get(key)
        if group and a["time"] - group["first_seen"] > window:
            close(open_groups.pop(key))         # old group is finished
            group = None
        if group is None:
            if len(open_groups) >= max_open:    # flood defence: close the oldest group
                oldest = next(iter(open_groups))
                close(open_groups.pop(oldest))
            open_groups[key] = {"source": a["source"], "type": a["type"], "asset": a["asset"],
                                "severity": a["severity"], "first_seen": a["time"], "count": 1}
        else:
            group["count"] += 1
            group["severity"] = max(group["severity"], a["severity"])

    for group in open_groups.values():
        close(group)

    ranked = sorted(best, key=lambda t: t[0], reverse=True)
    incidents = [dict(g, score=round(s, 3)) for s, _, g in ranked]
    return {"incidents": incidents, "rejected": rejected}
