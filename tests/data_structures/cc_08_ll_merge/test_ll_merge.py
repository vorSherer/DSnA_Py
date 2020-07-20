import pytest

from dsna_py.data_structures.cc_05_linked_list.linked_list import (
    Node,
    LinkedList,
)
from dsna_py.challenges.cc_08_ll_merge.ll_merge import merge_lists


def test_Node_exists():
    assert Node


def test_LinkedList_exists():
    assert LinkedList


# @pytest.mark.skip
def test_ll_merge_exists():
    assert merge_lists

@pytest.fixture
def salad_1():
    ll1 = LinkedList()
    ll1.insert("raspberry vinaigrette")
    ll1.insert("chopped nuts")
    ll1.insert("dried cranberries")
    ll1.insert("broccoli")
    ll1.insert("kale")
    ll1.insert("romaine")

    return ll1


@pytest.fixture
def salad_2():
    ll2 = LinkedList()
    ll2.insert("cucumber")
    ll2.insert("red bell pepper")
    ll2.insert("spinach")
    return ll2


def test_merge_two_lists_pass(salad_1, salad_2):
    ll1 = salad_1
    ll2 = salad_2
    assert str(merge_lists(ll1, ll2)) == "{ romaine } -> { spinach } -> { kale } -> { red bell pepper } -> { broccoli } -> { cucumber } -> { dried cranberries } -> { chopped nuts } -> { raspberry vinaigrette } -> None"

def test_merge_two_lists_fail(salad_1, salad_2):
    ll1 = salad_1
    ll2 = salad_2
    assert str(merge_lists(ll1, ll2)) != "{ romaine } -> { spinach } -> { kale } -> { red bell peppers } -> { broccoli } -> { cucumber } -> { dried cranberries } -> { chopped nuts } -> { raspberry vinaigrette } -> None"


def test_merge_one_list_and_one_empty(salad_1):
    ll1 = salad_1
    ll2 = LinkedList()
    assert str(merge_lists(ll1, ll2)) == "{ romaine } -> { kale } -> { broccoli } -> { dried cranberries } -> { chopped nuts } -> { raspberry vinaigrette } -> None"

