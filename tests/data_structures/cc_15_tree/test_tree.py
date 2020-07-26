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
    curr_root = TreeNode(7)
    root_left = TreeNode(3)
    root_right = TreeNode(1)
    curr_root.left_child = root_left
    curr_root.right_child = root_right
    bt.root_node = curr_root
    return bt


# @pytest.mark.skip
def test_binary_tree_instantiates(simple_tree):
    tree = simple_tree
    assert tree.root_node.value == 7
    assert tree.root_node.left_child.value == 3
    assert tree.root_node.right_child.value == 1


@pytest.mark.skip
def test_simple_pre_order_values(simple_tree):
    st = simple_tree
    expected = [7,3,1]
    actual = st.pre_order()
    assert actual == expected



