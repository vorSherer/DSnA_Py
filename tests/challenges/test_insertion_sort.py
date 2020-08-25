import pytest

from dsna_py.challenges.cc_26_insertion_sort.insertion_sort import insertion_sort


# @pytest.mark.skip
def test_insertion_sort_exists():
    assert insertion_sort


def test_insertion_sort_pass():
    expected = [4,8,15,16,23,42]
    actual = insertion_sort([ 8, 4, 23, 42, 16, 15])
    assert actual == expected


def test_insertion_sort_fail():
    expected = [4,8,15,16,23,42]
    actual = insertion_sort([ 8, 4, 23, 43, 16, 15])
    assert actual != expected


