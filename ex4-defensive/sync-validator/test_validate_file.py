import os

from validate_file import main

HERE = os.path.dirname(os.path.abspath(__file__))
SAMPLES = os.path.join(HERE, "samples")


def run(path):
    return main(["validate_file.py", path])


def test_good_sample_is_accepted(capsys):
    assert run(os.path.join(SAMPLES, "good.json")) == 0
    assert capsys.readouterr().out.strip() == "OK"


def test_injection_sample_is_rejected(capsys):
    assert run(os.path.join(SAMPLES, "bad_injection.json")) == 1
    assert capsys.readouterr().out.strip() == "REJECTED: patient_ref"


def test_missing_file(capsys):
    assert run(os.path.join(SAMPLES, "nope.json")) == 2


def test_folder_instead_of_file(capsys):
    assert run(SAMPLES) == 2


def test_oversized_file_is_rejected_not_loaded(tmp_path, capsys):
    big = tmp_path / "big.json"
    big.write_bytes(b" " * 5_000_000)
    assert run(str(big)) == 1
    assert capsys.readouterr().out.strip() == "REJECTED: body_too_large"


def test_wrong_number_of_arguments(capsys):
    assert main(["validate_file.py"]) == 2
