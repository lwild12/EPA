"""Company sync request validator (Ex4, Script A).

Checks a visit-note sync request BEFORE it reaches the database.
Mirrors the rules in the Ex1 prototype sync.php and adds extra defences.

Input : raw request body (bytes)
Output: a clean dict, or raises ValidationError naming the bad field.
"""
import json
import re
from datetime import datetime, timedelta, timezone

MAX_BODY = 65536                      # 64 KB, same as sync.php
FIELDS = {                            # field name -> max length
    "client_id": 64,
    "staff_id": 64,
    "patient_ref": 64,
    "note_text": 20000,
}
ID_FIELDS = ("client_id", "staff_id", "patient_ref")
ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]+$")
CONTROL_CHARS = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")  # allows \t and \n
MAX_AGE = timedelta(days=30)
CLOCK_DRIFT = timedelta(minutes=5)


class ValidationError(Exception):
    """Carries only a field name, never the user's input (no data leakage)."""


def _is_utf8_safe(text):
    """A lone surrogate (for example the JSON escape \\ud800) cannot be stored as UTF-8."""
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def _no_duplicate_keys(pairs):
    seen = {}
    for key, value in pairs:
        if key in seen:
            raise ValidationError("duplicate_key")
        seen[key] = value
    return seen


def _parse_date(text, now):
    try:
        when = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        raise ValidationError("created_at")
    if when.tzinfo is None:
        when = when.replace(tzinfo=timezone.utc)
    if when > now + CLOCK_DRIFT or when < now - MAX_AGE:
        raise ValidationError("created_at")
    return when


def validate(raw_body, now=None):
    now = now or datetime.now(timezone.utc)

    # 1. size first, before any parsing
    if not isinstance(raw_body, (bytes, bytearray)):
        raise ValidationError("body")
    if len(raw_body) > MAX_BODY:
        raise ValidationError("body_too_large")

    # 2. parse JSON strictly
    try:
        data = json.loads(raw_body.decode("utf-8"), object_pairs_hook=_no_duplicate_keys)
    except (UnicodeDecodeError, ValueError, RecursionError):   # deep nesting raises RecursionError
        raise ValidationError("invalid_json")

    # 3. must be an object with exactly the expected fields
    if not isinstance(data, dict):
        raise ValidationError("not_an_object")
    expected = set(FIELDS) | {"created_at"}
    if set(data) - expected:
        raise ValidationError("unknown_field")
    if expected - set(data):
        raise ValidationError("missing_field")

    # 4. type and length of each field
    for name, max_len in FIELDS.items():
        value = data[name]
        if not isinstance(value, str) or not value.strip() or len(value) > max_len or not _is_utf8_safe(value):
            raise ValidationError(name)

    # 5. patterns
    for name in ID_FIELDS:
        if not ID_PATTERN.fullmatch(data[name]):
            raise ValidationError(name)
    if CONTROL_CHARS.search(data["note_text"]):
        raise ValidationError("note_text")

    # 6. date window
    if not isinstance(data["created_at"], str):
        raise ValidationError("created_at")
    _parse_date(data["created_at"], now)

    return data
