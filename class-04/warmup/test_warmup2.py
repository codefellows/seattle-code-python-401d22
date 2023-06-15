import pytest
from warmup2 import add_values

def test_add_values_one_two_pass():
    actual = add_values(1, 2)
    expected = 3
    assert actual == expected

def test_add_values_one_two_fail():
    actual = add_values(1, 2)
    expected = 6
    assert actual != expected
