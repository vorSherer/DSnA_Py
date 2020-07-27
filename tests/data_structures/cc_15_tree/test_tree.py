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


# Test BinaryTree
@pytest.mark.skip
def test_empty_binary_tree_instantiates():
    et = BinaryTree()
    assert et.root_node == None


@pytest.mark.skip
def test_empty_binary_tree_fails():
    febt = BinaryTree()
    assert febt != 7


@pytest.mark.skip
def test_non_empty_binary_tree_passes():
    pbt = BinaryTree()
    root = TreeNode(3)
    assert pbt.root_node.value == 3


@pytest.mark.skip
def test_non_empty_binary_tree_fails():
    fbt = BinaryTree()
    root = TreeNode(7)
    assert fbt != None


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


# @pytest.mark.skip
def test_binary_tree_instantiates(simple_tree):
    tree = simple_tree
    assert tree.root_node.value == 3
    assert tree.root_node.left_child.value == 1
    assert tree.root_node.right_child.value == 7


@pytest.mark.skip
def test_simple_pre_order_values(simple_tree):
    st = simple_tree
    expected = [3,1,7]
    actual = st.pre_order()
    assert actual == expected


@pytest.mark.skip
def test_simple_in_order_values(simple_tree):
    st = simple_tree
    expected = [1,3,7]
    actual = st.in_order()
    assert actual == expected


@pytest.mark.skip
def test_simple_post_order_values(simple_tree):
    st = simple_tree
    expected = [1,7,3]
    actual = st.pre_order()
    assert actual == expected


# @pytest.fixture
@pytest.mark.skip
def balanced_tree():
    #build a binary tree of seven nodes in three levels
    bt = BinaryTree()
    curr_root = TreeNode(7)
    root_left = TreeNode(3)
    root_left_left = TreeNode(1)
    root_left_right = TreeNode(5)
    root_right = TreeNode(11)
    root_right_left = TreeNode(9)
    root_right_right = TreeNode(13)
    # curr_root.left_child = root_left
    # curr_root.right_child = root_right
    # bt.root_node = curr_root
    return bt


@pytest.mark.skip
def test_balanced_tree_instantiates(balanced_tree):
    tree = balanced_tree
    assert tree.root_node.value == 7
    assert tree.root_node.left_child.value == 3
    assert tree.root_node.left_child.left_child.value == 1
    assert tree.root_node.left_child.right_child.value == 5
    assert tree.root_node.right_child.value == 11
    assert tree.root_node.right_child.left_child.value == 9
    assert tree.root_node.right_child.right_child.value == 13


@pytest.mark.skip
def test_balanced_tree_traverses_pre_order(balanced_tree):
    tree = balanced_tree
    assert tree.pre_order() == [7,3,1,5,11,9,13]


@pytest.mark.skip
def test_balanced_tree_traverses_in_order(balanced_tree):
    tree = balanced_tree
    assert tree.in_order() == [1,3,5,7,9,11,13]


@pytest.mark.skip
def test_balanced_tree_traverses_post_order(balanced_tree):
    tree = balanced_tree
    assert tree.post_order == [1,5,3,9,13,11,7]


# @pytest.fixture
@pytest.mark.skip
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
    # curr_root.left_child = root_left
    # curr_root.right_child = root_right
    # ut.root_node = curr_root
    return ut


@pytest.mark.skip
def test_unbalanced_tree_instantiates(unbalanced_tree):
    utree = unbalanced_tree
    assert utree.root_node.value == 7
    assert utree.root_node.left_child.value == 3
    assert utree.root_node.left_child.left_child.value == 1
    assert utree.root_node.left_child.right_child.value == 5
    assert utree.root_node.right_child.value == 11
    assert utree.root_node.right_child.left_child.value == 9
    assert utree.root_node.right_child.right_child.value == 13


# Test BinarySearchTree
@pytest.mark.skip
def test_empty_bst_instantiates():
    ebst = BinarySearchTree()
    assert ebst.root_node == None


@pytest.mark.skip
def test_empty_bst_fails():
    febst = BinarySearchTree()
    assert febst != 7


@pytest.mark.skip
def test_non_empty_bst_passes():
    pbst = BinarySearchTree()
    root = TreeNode(3)
    assert pbst.root_node.value == 3


@pytest.mark.skip
def test_non_empty_bst_fails():
    fbst = BinarySearchTree()
    root = TreeNode(7)
    assert fbst != None


@pytest.mark.skip
def test_bst_instantiates(balanced_tree):
    bst = BinarySearchTree()
    assert tree.root_node.value == 7
    assert tree.root_node.left_child.value == 3
    assert tree.root_node.left_child.left_child.value == 1
    assert tree.root_node.left_child.right_child.value == 5
    assert tree.root_node.right_child.value == 11
    assert tree.root_node.right_child.left_child.value == 9
    assert tree.root_node.right_child.right_child.value == 13


@pytest.mark.skip
def test_balanced_bst_traverses_pre_order(balanced_tree):
    bstree = balanced_tree
    assert bstree.pre_order() == [7,3,1,5,11,9,13]


@pytest.mark.skip
def test_balanced_bst_traverses_in_order(balanced_tree):
    bstree = balanced_tree
    assert bstree.in_order() == [1,3,5,7,9,11,13]


@pytest.mark.skip
def test_balanced_bst_traverses_post_order(balanced_tree):
    bstree = balanced_tree
    assert bstree.post_order == [1,5,3,9,13,11,7]


@pytest.mark.skip
def test_unbalanced_bst_instantiates(unbalanced_tree):
    ubstree = unbalanced_tree
    assert ubstree.root_node.value == 6
    assert ubstree.root_node.left_child.value == 4
    assert ubstree.root_node.left_child.left_child.value == 2
    assert ubstree.root_node.right_child.value == 16
    assert ubstree.root_node.right_child.left_child.value == 10
    assert ubstree.root_node.right_child.right_child.value == 26
    assert ubstree.root_node.right_child.right_child.right_child.value == 42

@pytest.mark.skip
def test_unbalanced_bst_traverses_pre_order(unbalanced_tree):
    ubstree = unbalanced_tree
    assert ubstree.pre_order() == [6,4,2,16,10,26,42]


@pytest.mark.skip
def test_unbalanced_bst_traverses_in_order(unbalanced_tree):
    ubstree = unbalanced_tree
    assert ubstree.in_order() == [2,4,6,10,16,26,42]


@pytest.mark.skip
def test_unbalanced_bst_traverses_post_order(unbalanced_tree):
    ubstree = unbalanced_tree
    assert ubstree.post_order == [2,4,10,42,26,16,6]


@pytest.mark.skip
def test_bst_add_left_passes(unbalanced_tree):
    ubstree = unbalanced_tree
    ubstree.add(5)
    assert ubstree.in_order() == [2,4,5,6,10,16,26,42]
    

@pytest.mark.skip
def test_bst_add_fails(unbalanced_tree):
    ubstree = unbalanced_tree
    ubstree.add(12)
    assert ubstree.in_order() == [2,4,6,10,16,26,42]


@pytest.mark.skip
def test_bst_add_right_passes(unbalanced_tree):
    ubstree = unbalanced_tree
    ubstree.add(12)
    assert ubstree.in_order() == [2,4,6,10,12,16,26,42]


@pytest.mark.skip
def test_bst_contains_passes(unbalanced_tree):
    ubstree = unbalanced_tree
    assert ubstree.contains(42) == True

@pytest.mark.skip
def test_bst_contains_fails(unbalanced_tree):
    ubstree = unbalanced_tree
    assert ubstree.contains(13) == True
