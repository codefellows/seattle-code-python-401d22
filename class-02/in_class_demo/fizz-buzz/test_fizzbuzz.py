import pytest
from fizzbuzz import fizz_buzz


def test_one():
    actual = fizz_buzz(1)
    expected = 1
    assert actual == expected


def test_one_alt():
    assert fizz_buzz(1) == 1


def test_two():
    actual = fizz_buzz(2)
    expected = 2
    assert actual == expected


def test_three():
    actual = fizz_buzz(3)
    expected = "Fizz"
    assert actual == expected


def test_four():
    actual = fizz_buzz(4)
    expected = 4
    assert actual == expected


def test_five():
    actual = fizz_buzz(5)
    expected = "Buzz"
    assert actual == expected


def test_fifteen():
    actual = fizz_buzz(15)
    expected = "FizzBuzz"
    assert actual == expected


def test_large_num_good():
    actual = fizz_buzz(1500000000)
    expected = "FizzBuzz"
    assert actual == expected


def test_large_num_bad():
    actual = fizz_buzz(1500000001)
    expected = 1500000001
    assert actual == expected
