import tracemalloc

from alert_triage import triage


def alert(t=0, source="ids", typ="brute-force", asset="laptop", severity=3):
    return {"source": source, "type": typ, "asset": asset, "severity": severity, "time": t}


# ---------- NORMAL ----------
def test_normal_three_identical_become_one():
    out = triage([alert(0), alert(10), alert(20)])
    assert len(out["incidents"]) == 1
    assert out["incidents"][0]["count"] == 3


def test_normal_ranks_patient_db_above_laptop():
    out = triage([alert(0, asset="laptop"), alert(1, asset="patient-db")])
    assert out["incidents"][0]["asset"] == "patient-db"


def test_normal_unsorted_input_still_works():
    out = triage([alert(20), alert(0), alert(10)])
    assert out["incidents"][0]["count"] == 3


# ---------- BOUNDARY ----------
def test_boundary_empty_list():
    assert triage([]) == {"incidents": [], "rejected": 0}


def test_boundary_single_alert():
    assert triage([alert(5)])["incidents"][0]["count"] == 1


def test_boundary_exactly_at_window_edge_is_same_incident():
    out = triage([alert(0), alert(600)])
    assert len(out["incidents"]) == 1


def test_boundary_one_second_past_window_is_new_incident():
    out = triage([alert(0), alert(601)])
    assert len(out["incidents"]) == 2


def test_boundary_severity_1_and_5_accepted():
    out = triage([alert(0, severity=1), alert(0, typ="x", severity=5)])
    assert out["rejected"] == 0


# ---------- ERROR ----------
def test_error_severity_out_of_range_rejected():
    out = triage([alert(severity=0), alert(severity=9)])
    assert out["rejected"] == 2 and out["incidents"] == []


def test_error_missing_field_rejected():
    bad = alert()
    del bad["asset"]
    assert triage([bad])["rejected"] == 1


def test_error_bad_time_rejected():
    assert triage([alert(t="yesterday"), alert(t=float("nan"))])["rejected"] == 2


def test_error_not_a_dict_rejected():
    assert triage(["hello", None, 42])["rejected"] == 3


# ---------- SECURITY ----------
def test_security_severity_as_string_rejected():
    assert triage([alert(severity="5")])["rejected"] == 1


def test_security_boolean_severity_rejected():
    assert triage([alert(severity=True)])["rejected"] == 1


def test_security_huge_asset_name_rejected():
    assert triage([alert(asset="A" * 1_000_000)])["rejected"] == 1


def test_security_flood_of_unique_alerts_keeps_memory_capped():
    flood = [alert(t=i, asset=f"host-{i}") for i in range(20_000)]
    tracemalloc.start()
    out = triage(flood, max_open=1000, top_n=50)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    assert len(out["incidents"]) == 50          # output stays small
    assert peak < 60_000_000                    # under 60 MB even for a flood
