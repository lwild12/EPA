"""Nine vulnerable/fixed pairs for Exercise 4 (defensive programming).

Each pair: <name>_vulnerable() and <name>_fixed(). Read the docstring (CWE, attack, fix), then run
test_vuln_examples.py to SEE the exploit succeed against the vulnerable version and fail against the fix.
Everything is local and harmless (temp dirs, in-memory SQLite, `echo`).
"""
import base64
import hashlib
import hmac
import html
import json
import os
import pickle
import secrets
import shlex
import sqlite3
import subprocess
import tempfile
import time

# ---------------------------------------------------------------------------
# 1. Path traversal (CWE-22)
# Attack: filename "../secret.txt" escapes the intended folder.
# Fix: resolve the real path and check it is inside the base directory.
# ---------------------------------------------------------------------------
def read_file_vulnerable(base_dir: str, name: str) -> str:
    with open(os.path.join(base_dir, name)) as f:
        return f.read()


def read_file_fixed(base_dir: str, name: str) -> str:
    base = os.path.realpath(base_dir)
    target = os.path.realpath(os.path.join(base, name))
    if os.path.commonpath([base, target]) != base:
        raise PermissionError("path escapes base directory")
    with open(target) as f:
        return f.read()


# ---------------------------------------------------------------------------
# 2. SQL injection (CWE-89)
# Attack: username "x' OR '1'='1" returns every row.
# Fix: parameterised queries (data never becomes SQL).
# ---------------------------------------------------------------------------
def find_user_vulnerable(con: sqlite3.Connection, username: str):
    return con.execute(f"SELECT id, username FROM users WHERE username = '{username}'").fetchall()


def find_user_fixed(con: sqlite3.Connection, username: str):
    return con.execute("SELECT id, username FROM users WHERE username = ?", (username,)).fetchall()


# ---------------------------------------------------------------------------
# 3. OS command injection (CWE-78)
# Attack: host "x; echo INJECTED" runs a second command via the shell.
# Fix: no shell, pass an argument list, and validate the input.
# ---------------------------------------------------------------------------
def ping_label_vulnerable(host: str) -> str:
    # stands in for `ping`: harmless echo so the demo is safe
    return subprocess.run(f"echo checking {host}", shell=True, capture_output=True, text=True).stdout


def ping_label_fixed(host: str) -> str:
    import re
    if not re.fullmatch(r"[A-Za-z0-9.\-]{1,253}", host):
        raise ValueError("invalid host")
    return subprocess.run(["echo", "checking", host], shell=False, capture_output=True, text=True).stdout


# ---------------------------------------------------------------------------
# 4. Timing side channel in comparison (CWE-208)
# Attack: == returns at the first differing byte, leaking how many leading bytes are right.
# Fix: hmac.compare_digest (constant time).
# ---------------------------------------------------------------------------
def check_token_vulnerable(supplied: str, expected: str) -> bool:
    return supplied == expected


def check_token_fixed(supplied: str, expected: str) -> bool:
    return hmac.compare_digest(supplied.encode(), expected.encode())


# ---------------------------------------------------------------------------
# 5. Race condition / TOCTOU (CWE-367)
# Attack: file can be swapped (e.g. for a symlink) between the check and the use.
# Fix: open once with O_NOFOLLOW / O_EXCL and work on the descriptor.
# ---------------------------------------------------------------------------
def write_report_vulnerable(path: str, text: str) -> None:
    if not os.path.exists(path):         # check ...
        # <-- attacker window: create path as a symlink to a victim file here
        with open(path, "w") as f:       # ... then use (follows symlinks!)
            f.write(text)


def write_report_fixed(path: str, text: str) -> None:
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0), 0o600)
    with os.fdopen(fd, "w") as f:        # atomic create-or-fail, no symlink following
        f.write(text)


# ---------------------------------------------------------------------------
# 6. Weak password storage (CWE-916 / CWE-328)
# Attack: unsalted fast hash is cracked by rainbow tables / GPUs.
# Fix: per-user random salt + slow KDF (scrypt here; argon2/bcrypt also fine).
# ---------------------------------------------------------------------------
def hash_password_vulnerable(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


def hash_password_fixed(password: str, salt: bytes | None = None) -> str:
    salt = salt or secrets.token_bytes(16)
    dk = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)
    return f"scrypt${base64.b64encode(salt).decode()}${base64.b64encode(dk).decode()}"


def verify_password_fixed(password: str, stored: str) -> bool:
    _, salt_b64, dk_b64 = stored.split("$")
    again = hash_password_fixed(password, base64.b64decode(salt_b64))
    return hmac.compare_digest(again.split("$")[2], dk_b64)


# ---------------------------------------------------------------------------
# 7. Unsafe deserialisation (CWE-502)
# Attack: pickle.loads on untrusted bytes can execute code (via __reduce__).
# Fix: use a data-only format (JSON) and validate the shape.
# ---------------------------------------------------------------------------
def load_profile_vulnerable(blob: bytes):
    return pickle.loads(blob)


def load_profile_fixed(blob: bytes) -> dict:
    data = json.loads(blob.decode())
    if not isinstance(data, dict) or set(data) - {"name", "age"}:
        raise ValueError("unexpected profile shape")
    return data


# ---------------------------------------------------------------------------
# 8. Predictable tokens (CWE-338)
# Attack: `random` is a seedable PRNG; tokens can be predicted.
# Fix: `secrets` uses the OS CSPRNG.
# ---------------------------------------------------------------------------
def make_token_vulnerable(seed: int | None = None) -> str:
    import random
    r = random.Random(seed if seed is not None else int(time.time()))
    return "".join(r.choice("abcdef0123456789") for _ in range(32))


def make_token_fixed() -> str:
    return secrets.token_hex(16)


# ---------------------------------------------------------------------------
# 9. Cross-site scripting / output encoding (CWE-79)
# Attack: comment "<script>alert(1)</script>" is rendered as live markup.
# Fix: encode for the HTML context (templating engines do this by default).
# ---------------------------------------------------------------------------
def render_comment_vulnerable(comment: str) -> str:
    return f"<p>{comment}</p>"


def render_comment_fixed(comment: str) -> str:
    return f"<p>{html.escape(comment, quote=True)}</p>"


PAIRS = {
    "path_traversal": (read_file_vulnerable, read_file_fixed),
    "sql_injection": (find_user_vulnerable, find_user_fixed),
    "command_injection": (ping_label_vulnerable, ping_label_fixed),
    "timing_compare": (check_token_vulnerable, check_token_fixed),
    "toctou_race": (write_report_vulnerable, write_report_fixed),
    "password_hashing": (hash_password_vulnerable, hash_password_fixed),
    "deserialisation": (load_profile_vulnerable, load_profile_fixed),
    "predictable_token": (make_token_vulnerable, make_token_fixed),
    "xss_encoding": (render_comment_vulnerable, render_comment_fixed),
}

if __name__ == "__main__":
    print("Pairs:", ", ".join(PAIRS))
    print("Run: python3 -m pytest -v test_vuln_examples.py")
