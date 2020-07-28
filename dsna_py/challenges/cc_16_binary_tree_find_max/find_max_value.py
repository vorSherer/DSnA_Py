from dsna_py.data_structures.cc_15_tree.tree import (
    # TreeNode,
    BinaryTree,
)

def find_maximum_value(tree):
    max_val = -1
    def walk(curr_node):
        nonlocal max_val
        if not curr_node:
            return
        if curr_node.value > max_val:
            max_val = curr_node.value
        # Traverse left
        walk(curr_node.left_child)
        # Traverse right
        walk(curr_node.right_child)

        return max_val

    return walk(tree.root_node)


