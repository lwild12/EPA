"""Runs each .asm program through mips_mini and checks the output. Run: python3 -m pytest -q test_mips.py
NOTE: this is a minimal simulator written for testing. Always re-check once in MARS/SPIM on the day."""
import os

import pytest

from mips_mini import MIPS

HERE = os.path.dirname(os.path.abspath(__file__))


def run(name):
    return MIPS(open(os.path.join(HERE, name)).read()).run()


def test_sum_array():
    assert run("sum_array.asm") == "Sum = 150\n"


def test_factorial():
    assert run("factorial.asm") == "6! = 720\n"


def test_bubble_sort():
    assert run("bubble_sort.asm") == "1 2 3 5 8 9\n"


def test_safe_copy_truncates_and_does_not_overflow():
    out = run("safe_copy.asm")
    assert out == "copied: AAAAAAA\ntruncated: 1\nguard: OK\n"


@pytest.mark.parametrize("name", [f for f in os.listdir(HERE) if f.endswith(".asm")])
def test_every_program_terminates(name):
    assert isinstance(run(name), str)
