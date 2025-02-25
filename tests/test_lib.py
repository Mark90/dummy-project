from src.lib import get_largest_number

import pytest

def shuffle_deterministic(list_):
    from random import Random
    ctx = Random(1)
    ctx.shuffle(list_)

@pytest.mark.benchmark
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

@pytest.mark.benchmark
def test_largest_number_3():
    # given
    numbers = list(range(100_000)) + list(range(100_000))
    shuffle_deterministic(numbers)

    # when
    largest = get_largest_number(numbers)

    # then
    assert largest == 99_999

@pytest.fixture
def setup_large():
    # given
    numbers = list(range(100_000)) + list(range(100_000))
    shuffle_deterministic(numbers)
    return numbers

@pytest.mark.benchmark
def test_largest_number_3_with_fixture(setup_large):
    """Same as test_largest_number_3 but with setup in fixture to check whether codspeed excludes fixture from measurements.

    And it seems like it does, which is very handy!
    """
    # given
    numbers = setup_large


    # when
    largest = get_largest_number(numbers)

    # then
    assert largest == 99_999


def test_largest_number_3_with_decorator(benchmark):
    """Same as test_largest_number_3 but using benchmark decorator to explicitly measure the code we're interested in."""
    # given
    numbers = list(range(100_000)) + list(range(100_000))
    shuffle_deterministic(numbers)

    @benchmark  # Note that this decorator automatically calls the function, after which `to_bench` refers to the output
    def to_bench():
        return get_largest_number(numbers)

    # when
    largest = to_bench

    # then
    assert largest == 99_999
