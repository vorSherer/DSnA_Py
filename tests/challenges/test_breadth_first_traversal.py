import pytest

from dsna_py.challenges.cc_17_binary_tree_breadth_first.breadth_first_traversal import breadth_first
from dsna_py.data_structures.cc_15_tree.tree import (
    TreeNode,
    BinaryTree,
)


def test_breadth_first_exists():
    assert breadth_first


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
def test_simple_breadth_returns(simple_tree):
    st = simple_tree
    expected = [3,1,7]
    actual = breadth_first(st)
    assert actual == expected


@pytest.fixture
def unbalanced_tree():
    #build a binary tree of seven nodes in four levels
    ut = BinaryTree()
    curr_root = TreeNode(6)
    root_left = TreeNode(4)
    root_left_left = TreeNode(2)
    root_right = TreeNode(16)
    root_right_left = TreeNode(10)
    root_right_right = TreeNode(26)
    root_right_right_right = TreeNode(42)

    ut.root_node = curr_root
    curr_root.left_child = root_left
    curr_root.left_child.left_child = root_left_left
    curr_root.right_child = root_right
    curr_root.right_child.left_child = root_right_left
    curr_root.right_child.right_child = root_right_right
    curr_root.right_child.right_child.right_child = root_right_right_right

    return ut


@pytest.mark.skip
def test_unbalanced_breadth_returns(unbalanced_tree):
    ut = unbalanced_tree
    expected = [6,4,16,2,10,26,42]
    actual = breadth_first(ut)
    assert actual == expected


