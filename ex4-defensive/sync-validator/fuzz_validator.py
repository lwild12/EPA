"""Dynamic analysis: throw thousands of random and mutated requests at validate().

Two rules are checked on every request:
  1. validate() may only return a dict or raise ValidationError. Any other crash is a defect.
  2. If a request is accepted, the result must really be safe (right keys, safe IDs,
     no control characters, text that can be stored as UTF-8, a date inside the window).
Run:  python fuzz_validator.py          (20,000 requests, same every time)
      python fuzz_validator.py 100000   (more requests)
"""
import json
import random
import re
import sys
from datetime import datetime, timedelta, timezone

from sync_validator import CONTROL_CHARS, FIELDS, ValidationError, validate

NOW = datetime(2026, 11, 20, 12, 0, tzinfo=timezone.utc)
POOL = ["", " ", "abc", "dev-42_x", "../../etc/passwd", "x' OR '1'='1", "abc\n", "a\x00b", "a\ud800b",
        "‮", "ав", "A" * 64, "A" * 65, "note\ttext\nline", "\U0001F600", "{}", "%s%n",
        "2026-11-20T11:30:00Z", "2026-11-20", "9999-12-31T23:59:59Z", "not a date", 12345, 1.5, None,
        True, [], {}, ["x"]]


def random_request(rng):
    body = {"client_id": "dev1", "staff_id": "s1", "patient_ref": "p1", "note_text": "n",
            "created_at": "2026-11-20T11:30:00Z"}
    for key in list(body):
        if rng.random() < 0.5:
            body[key] = rng.choice(POOL)
    if rng.random() < 0.15:
        del body[rng.choice(list(body))]
    if rng.random() < 0.15:
        body[rng.choice(["is_admin", "x", "client_id "])] = rng.choice(POOL)
    raw = json.dumps(body).encode()
    roll = rng.random()
    if roll < 0.10:                                   # deeply nested value
        depth = rng.randint(1000, 30000)
        raw = b'{"client_id":' + b"[" * depth + b"]" * depth + b"}"
    elif roll < 0.25:                                 # flip a few random bytes
        raw = bytearray(raw)
        for _ in range(rng.randint(1, 4)):
            raw[rng.randrange(len(raw))] = rng.randrange(256)
        raw = bytes(raw)
    elif roll < 0.30:                                 # pure random bytes
        raw = bytes(rng.randrange(256) for _ in range(rng.randint(0, 200)))
    return raw


def check_accepted(data):
    assert set(data) == set(FIELDS) | {"created_at"}, "wrong keys"
    for name in ("client_id", "staff_id", "patient_ref"):
        assert re.fullmatch(r"[A-Za-z0-9_-]{1,64}", data[name]), f"unsafe {name}"
    note = data["note_text"]
    assert 0 < len(note.strip()) and len(note) <= 20000, "bad note length"
    assert not CONTROL_CHARS.search(note), "control characters accepted"
    note.encode("utf-8")                              # raises if it cannot be stored
    when = datetime.fromisoformat(data["created_at"].replace("Z", "+00:00"))
    if when.tzinfo is None:
        when = when.replace(tzinfo=timezone.utc)
    assert NOW - timedelta(days=30) <= when <= NOW + timedelta(minutes=5), "date outside window"


def main(count):
    rng = random.Random(1)
    accepted = rejected = 0
    failures = []
    for i in range(count):
        raw = random_request(rng)
        try:
            data = validate(raw, now=NOW)
            check_accepted(data)
            accepted += 1
        except ValidationError:
            rejected += 1
        except Exception as err:                      # a crash or a broken promise
            failures.append((i, type(err).__name__, str(err)[:60]))
    print(f"requests: {count}   accepted: {accepted}   rejected: {rejected}   failures: {len(failures)}")
    seen = set()
    for i, name, msg in failures:
        if (name, msg) not in seen:
            seen.add((name, msg))
            print(f"  FAILURE type={name} detail={msg!r} (first at request {i})")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(int(sys.argv[1]) if len(sys.argv) > 1 else 20000))
