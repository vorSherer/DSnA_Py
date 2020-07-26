import pytest

from dsna_py.data_structures.cc_15_tree.tree import (
    TreeNode,
    BinaryTree,
    BinarySearchTree,
    )


# Test connections to Module
def test_TreeNode_exists():
    assert TreeNode

def test_bin_tree_exists():
    assert BinaryTree

def test_bin_srch_tree_exists():
    assert BinarySearchTree


# Test TreeNode
def test_TreeNode_instantiation():
    binary_node = TreeNode(7)
    expected = 7
    actual = binary_node.value
    assert actual == expected


# @pytest.mark.skip
def test_Node_left_value(simple_tree):
    binary_node = TreeNode(7)
    expected = None
    actual = binary_node.left_child
    assert actual == expected


# @pytest.mark.skip
def test_Node_right_value(simple_tree):
    binary_node = TreeNode(7)
    expected = None
    actual = binary_node.right_child
    assert actual == expected


@pytest.fixture
def simple_tree():
    #build a binary tree of three nodes
    bt = BinaryTree()
    root_node = TreeNode(7)
    left_child = TreeNode(3)
    right_child = TreeNode(1)


@pytest.mark.skip
def test_binary_tree_instantiates(simple_tree):
    tree = simple_tree()

