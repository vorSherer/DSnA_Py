class TreeNode:
    """
    Instantiate a node containing any value and pointers to any left and right child nodes.
    """
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree:
    """
    Instantiate an empty binary tree data structure, with traversal methods.
    """
    def __init__(self):
        self.root_node = None

    def pre_order(self, left_child=None, right_child=None):
        """
        Implement a call stack to facilitate a root-left-right traversal methodology and return a list of the values found.
        """
        values = []

        def walk(curr_node):
            # Break immediately if node is empty
            if not curr_node:
                return
            
            # Deal with the root
            values.append(curr_node.value)
            # Check for a left-child node
            walk(curr_node.left_child)
            # Check for a right-child node
            walk(curr_node.right_child)

        walk(self.root_node)

        return values

    def in_order(self, left_child=None, right_child=None):
        """
        Implement a call stack to facilitate a left-root-right traversal methodology and return a list of the values found.
        """
        values = []

        def walk(curr_node):
            if not curr_node:
                return
            
            # Check for a left-child node
            walk(curr_node.left_child)
            # Deal with the root
            values.append(curr_node.value)
            # Check for a right-child node
            walk(curr_node.right_child)

        walk(self.root_node)

        return values


    def post_order(self, left_child=None, right_child=None):
        """
        Implement a call stack to facilitate a left-right-root traversal methodology and return a list of the values found.
        """
        values = []

        def walk(curr_node):
            if not curr_node:
                return
            
            # Check for a left-child node
            walk(curr_node.left_child)
            # Check for a right-child node
            walk(curr_node.right_child)
            # Deal with the root
            values.append(curr_node.value)

        walk(self.root_node)

        return values





class BinarySearchTree(BinaryTree):
    """
    Instantiate an empty binary search tree as a subclass of BinaryTree, with 'add' and 'contains' methods.
    """
    def add(self, value):
        """
        Instantiate a node which takes in any value and traverse the Binary Search Tree to add the node in the correct location.
        """
        def walk(curr_node, node_to_add):

            if not curr_node:
                return
            
            if node_to_add.value < curr_node.value:
                if not curr_node.left_child:
                    curr_node.left_child = node_to_add
                else:
                    walk(curr_node.left_child, node_to_add)
            else:
                if not curr_node.right_child:
                    curr_node.right_child = node_to_add
                else:
                    walk(curr_node.right_child, node_to_add)

        new_node = TreeNode(value)

        if not self.root_node:
            self.root_node = new_node
            return

        walk(self.root_node, new_node)
        
    def contains(self, value):
        """
        Traverse a Binary Search Tree comparing a given value to the value of each node and return a boolean indicating whether or not the value is in the tree at least once.
        """
        def walk(curr_node, value):
            if not curr_node:
                return False

            # If value found, return True
            if value == curr_node.value:
                return True
            # If value < root, search left
            elif value < curr_node.value:
                return walk(curr_node.left_child, value)
            # If value > root, search right
            elif value > curr_node.value:
                return walk(curr_node.right_child, value)
            # If value not found, return False
            return False

        return walk(self.root_node, value)
 


if __name__ == "__main__":
    pass
    # bst = BinarySearchTree()
    # bst.add(4)
    # bst.add(7)
    # bst.add(5)
    # bst.add(9)
    # bst.add(2)
    # bst.add(30)
    # bst.add(-1)
    # print(bst.pre_order)
