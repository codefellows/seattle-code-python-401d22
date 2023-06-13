import pytest
from factorial import factorial


# 1
def test_factorial_one():
    actual = factorial(1)
    expected = 1
    assert actual == expected


# 2 * 1
def test_factorial_two():
    actual = factorial(2)
    expected = 2
    assert actual == expected


# 3 * 2 * 1
def test_factorial_three():
    actual = factorial(3)
    expected = 6
    assert actual == expected


# 4 * 3 * 2 * 1
def test_factorial_four():
    actual = factorial(4)
    expected = 24
    assert actual == expected
