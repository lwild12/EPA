import json
from datetime import datetime, timedelta, timezone

import pytest

from sync_validator import ValidationError, validate

NOW = datetime(2026, 11, 20, 12, 0, tzinfo=timezone.utc)


def good(**changes):
    body = {
        "client_id": "dev42-0001",
        "staff_id": "staff_123",
        "patient_ref": "P-90210",
        "note_text": "Visited at 10:00. Patient comfortable.\nNext visit Friday.",
        "created_at": "2026-11-20T11:30:00Z",
    }
    body.update(changes)
    return json.dumps(body).encode()


def rejects(raw, field=None):
    with pytest.raises(ValidationError) as err:
        validate(raw, now=NOW)
    if field:
        assert str(err.value) == field


# ---------- NORMAL ----------
def test_normal_good_note():
    assert validate(good(), now=NOW)["client_id"] == "dev42-0001"


def test_normal_multiline_note_with_tab():
    assert validate(good(note_text="line1\n\tline2"), now=NOW)


# ---------- BOUNDARY ----------
def test_boundary_id_64_ok():
    assert validate(good(client_id="a" * 64), now=NOW)


def test_boundary_id_65_rejected():
    rejects(good(client_id="a" * 65), "client_id")


def test_boundary_note_20000_ok():
    assert validate(good(note_text="x" * 20000), now=NOW)


def test_boundary_note_20001_rejected():
    rejects(good(note_text="x" * 20001), "note_text")


def test_boundary_date_just_inside_30_days():
    when = (NOW - timedelta(days=29, hours=23)).isoformat()
    assert validate(good(created_at=when), now=NOW)


def test_boundary_date_older_than_30_days_rejected():
    when = (NOW - timedelta(days=31)).isoformat()
    rejects(good(created_at=when), "created_at")


def test_boundary_date_4_minutes_future_ok():
    when = (NOW + timedelta(minutes=4)).isoformat()
    assert validate(good(created_at=when), now=NOW)


def test_boundary_date_10_minutes_future_rejected():
    when = (NOW + timedelta(minutes=10)).isoformat()
    rejects(good(created_at=when), "created_at")


# ---------- ERROR ----------
def test_error_empty_body():
    rejects(b"", "invalid_json")


def test_error_not_json():
    rejects(b"hello", "invalid_json")


def test_error_json_list_not_object():
    rejects(b"[1,2,3]", "not_an_object")


def test_error_missing_field():
    body = json.loads(good())
    del body["staff_id"]
    rejects(json.dumps(body).encode(), "missing_field")


def test_error_number_instead_of_string():
    rejects(good(client_id=12345), "client_id")


def test_error_blank_note():
    rejects(good(note_text="   "), "note_text")


def test_error_bad_date_text():
    rejects(good(created_at="not a date"), "created_at")


def test_error_date_is_number():
    rejects(good(created_at=20261120), "created_at")


def test_error_body_is_text_not_bytes():
    rejects("a string, not bytes", "body")


# ---------- SECURITY ----------
def test_security_sql_injection_in_patient_ref():
    rejects(good(patient_ref="x' OR '1'='1"), "patient_ref")


def test_security_path_traversal_in_client_id():
    rejects(good(client_id="../../etc/passwd"), "client_id")


def test_security_trailing_newline_in_id():
    rejects(good(client_id="abc\n"), "client_id")


def test_security_null_byte_in_note():
    rejects(good(note_text="hello\x00world"), "note_text")


def test_security_huge_body():
    rejects(b"{" + b" " * 10_000_000 + b"}", "body_too_large")


def test_security_duplicate_keys():
    raw = (b'{"client_id":"a","client_id":"b","staff_id":"s","patient_ref":"p",'
           b'"note_text":"n","created_at":"2026-11-20T11:30:00Z"}')
    rejects(raw, "duplicate_key")


def test_security_extra_admin_field():
    body = json.loads(good())
    body["is_admin"] = True
    rejects(json.dumps(body).encode(), "unknown_field")


def test_security_invalid_utf8():
    rejects(b"\xff\xfe\x00bad", "invalid_json")


def test_security_error_never_echoes_input():
    with pytest.raises(ValidationError) as err:
        validate(good(patient_ref="SECRET'; DROP TABLE notes;--"), now=NOW)
    assert "SECRET" not in str(err.value)
