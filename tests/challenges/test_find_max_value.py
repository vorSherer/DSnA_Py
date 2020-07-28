import pytest

from dsna_py.challenges.cc_16_binary_tree_find_max.find_max_value import find_maximum_value
from dsna_py.data_structures.cc_15_tree.tree import (
    TreeNode,
    BinaryTree,
)


def test_find_max_val_exists():
    assert find_maximum_value


@pytest.mark.skip
def test_empty_tree_instantiates():
    tree = BinaryTree()
    expected = None
    actual = tree.root_node
    assert actual == expected


@pytest.fixture
def simple_tree():
    #build a binary tree of three nodes in two levels
    st = BinaryTree()
    curr_root = TreeNode(3)
    root_left = TreeNode(1)
    root_right = TreeNode(7)
    curr_root.left_child = root_left
    curr_root.right_child = root_right
    st.root_node = curr_root
    return st


@pytest.mark.skip
def test_trial_tree_instantiates(simple_tree):
    poltree = simple_tree
    expected = 3
    actual = poltree.root_node.value
    assert actual == expected


@pytest.mark.skip
def test_max_val_passes(simple_tree):
    ttree = simple_tree
    expected = 7
    actual = find_maximum_value(ttree)
    assert actual == expected

