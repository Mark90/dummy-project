from src.lib import get_largest_number

import pytest

def shuffle_deterministic(list_):
    from random import Random
    ctx = Random(1)
    ctx.shuffle(list_)


def test_largest_number_error():
    with pytest.raises(ValueError):
        get_largest_number([])

def test_largest_number_1():
    # given
    numbers = list(range(100))
    shuffle_deterministic(numbers)

    # when
    largest = get_largest_number(numbers)

    # then
    assert largest == 99

def test_largest_number_2():
    # given
    numbers = list(range(10_000))
    shuffle_deterministic(numbers)

    # when
    largest = get_largest_number(numbers)

    # then
    assert largest == 9_999

def test_largest_number_3():
    # given
    numbers = list(range(100_000)) + list(range(100_000))
    shuffle_deterministic(numbers)

    # when
    largest = get_largest_number(numbers)

    # then
    assert largest == 99_999
