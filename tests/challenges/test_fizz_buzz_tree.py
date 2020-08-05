import pytest

from dsna_py.challenges.fizz_buzz_tree.fizz_buzz_tree import (
    fizz_buzz_tree,
    TreeNode,
)


def test_FBtree_exists():
    assert fizz_buzz_tree


def test_empty_tree_pass():
    empty_tree = fizz_buzz_tree(None)
    expected = None
    actual = empty_tree
    assert actual == expected


def test_string_content_fails():
    with pytest.raises(TypeError):
        string_tree = fizz_buzz_tree(TreeNode('1'))


@pytest.fixture
def kthary_tree():
    root = TreeNode(1) 
    root.child.append(TreeNode(2)) 
    root.child.append(TreeNode(3)) 
    root.child.append(TreeNode(4))
    print(root.child[0])
    root.child[0].child.append(TreeNode(5))  
    root.child[0].child[0].child.append(TreeNode(10))  
    root.child[0].child.append(TreeNode(6))  
    root.child[0].child[1].child.append(TreeNode(11)) 
    root.child[0].child[1].child.append(TreeNode(12)) 
    root.child[0].child[1].child.append(TreeNode(15))  
    root.child[2].child.append(TreeNode(7)) 
    root.child[2].child.append(TreeNode(8)) 
    root.child[2].child.append(TreeNode(9)) 

    return root


def test_tree_instantiates(kthary_tree):
    fb_test = fizz_buzz_tree(kthary_tree)
    expected = "1"
    actual = fb_test.value
    assert actual == expected


def test_tree_instantiated_fail(kthary_tree):
    tree = kthary_tree
    fb_test = fizz_buzz_tree(tree)
    expected = 1
    actual = fb_test.value
    assert actual != expected


def test_fizz_instantiates(kthary_tree):
    tree = kthary_tree
    fb_test = fizz_buzz_tree(tree)
    expected = "Fizz"
    actual = fb_test.child[0].child[1].value
    assert actual == expected


def test_buzz_instantiates(kthary_tree):
    tree = kthary_tree
    fb_test = fizz_buzz_tree(tree)
    expected = "Buzz"
    actual = fb_test.child[0].child[0].child[0].value
    assert actual == expected


def test_fizzbuzz_instantiates(kthary_tree):
    tree = kthary_tree
    fb_test = fizz_buzz_tree(tree)
    expected = "FizzBuzz"
    actual = fb_test.child[0].child[1].child[2].value
    assert actual == expected


def test_string_instantiates(kthary_tree):
    tree = kthary_tree
    fb_test = fizz_buzz_tree(tree)
    expected = "8"
    actual = fb_test.child[2].child[1].value
    assert actual == expected


