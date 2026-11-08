"""Each test shows the exploit working on the vulnerable version and failing on the fixed one."""
import os
import pickle
import sqlite3

import pytest

import vuln_examples as v


def test_path_traversal(tmp_path):
    base = tmp_path / "public"
    base.mkdir()
    (base / "ok.txt").write_text("fine")
    (tmp_path / "secret.txt").write_text("TOP SECRET")
    assert v.read_file_vulnerable(str(base), "../secret.txt") == "TOP SECRET"
    with pytest.raises(PermissionError):
        v.read_file_fixed(str(base), "../secret.txt")
    assert v.read_file_fixed(str(base), "ok.txt") == "fine"


def test_sql_injection():
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT)")
    con.executemany("INSERT INTO users (username) VALUES (?)", [("alice",), ("bob",)])
    payload = "x' OR '1'='1"
    assert len(v.find_user_vulnerable(con, payload)) == 2
    assert v.find_user_fixed(con, payload) == []
    assert v.find_user_fixed(con, "alice")[0][1] == "alice"


def test_command_injection():
    assert "INJECTED" in v.ping_label_vulnerable("x; echo INJECTED").splitlines()
    with pytest.raises(ValueError):
        v.ping_label_fixed("x; echo INJECTED")
    assert v.ping_label_fixed("example.com").strip() == "checking example.com"


def test_timing_compare_functionally_correct():
    # Timing leaks are statistical; here we only prove both give right answers and the fix is constant-time API.
    assert v.check_token_vulnerable("abc", "abc") and not v.check_token_vulnerable("abd", "abc")
    assert v.check_token_fixed("abc", "abc") and not v.check_token_fixed("abd", "abc")
    import inspect
    assert "compare_digest" in inspect.getsource(v.check_token_fixed)


def test_toctou(tmp_path):
    victim = tmp_path / "victim.txt"
    victim.write_text("original")
    link = tmp_path / "report.txt"
    os.symlink(victim, link)            # attacker plants a symlink
    # vulnerable: os.path.exists follows the link (victim exists) so it refuses here; show the dangling variant
    dangling = tmp_path / "dangling.txt"
    target = tmp_path / "newvictim.txt"
    os.symlink(target, dangling)        # points to a file that does not exist yet
    v.write_report_vulnerable(str(dangling), "pwned")
    assert target.exists() and target.read_text() == "pwned"   # wrote through the symlink
    dangling2 = tmp_path / "dangling2.txt"
    target2 = tmp_path / "newvictim2.txt"
    os.symlink(target2, dangling2)
    with pytest.raises(OSError):
        v.write_report_fixed(str(dangling2), "pwned")
    assert not target2.exists()
    v.write_report_fixed(str(tmp_path / "fresh.txt"), "ok")
    assert (tmp_path / "fresh.txt").read_text() == "ok"
    assert oct((tmp_path / "fresh.txt").stat().st_mode & 0o777) == "0o600"


def test_password_hashing():
    a, b = v.hash_password_vulnerable("hunter2"), v.hash_password_vulnerable("hunter2")
    assert a == b and len(a) == 32                       # unsalted, fast: same hash for same password
    s1, s2 = v.hash_password_fixed("hunter2"), v.hash_password_fixed("hunter2")
    assert s1 != s2                                      # salted
    assert v.verify_password_fixed("hunter2", s1) and not v.verify_password_fixed("wrong", s1)


def test_deserialisation(tmp_path):
    marker = tmp_path / "pwned"

    class Evil:
        def __reduce__(self):
            return (open, (str(marker), "w"))            # harmless stand-in for code execution

    blob = pickle.dumps(Evil())
    v.load_profile_vulnerable(blob)
    assert marker.exists()                               # attacker-controlled callable ran
    marker.unlink()
    with pytest.raises(Exception):
        v.load_profile_fixed(blob)
    assert not marker.exists()
    assert v.load_profile_fixed(b'{"name": "a", "age": 3}') == {"name": "a", "age": 3}


def test_predictable_token():
    assert v.make_token_vulnerable(1234) == v.make_token_vulnerable(1234)   # attacker who guesses the seed gets the token
    assert v.make_token_fixed() != v.make_token_fixed()
    assert len(v.make_token_fixed()) == 32


def test_xss():
    p = "<script>alert(1)</script>"
    assert "<script>" in v.render_comment_vulnerable(p)
    out = v.render_comment_fixed(p)
    assert "<script>" not in out and "&lt;script&gt;" in out
