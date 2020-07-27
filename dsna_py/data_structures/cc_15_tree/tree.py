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

        def walk(node):
            if not node:
                return
            
            # Deal with the root
            values.append(node.value)
            # Check for a left-child node
            walk(node.left_child)
            # Check for a right-child node
            walk(node.right_child)
        walk(self.root)

        return values

    def in_order(self, left_child=None, right_child=None):
        pass

    def post_order(self, left_child=None, right_child=None):
        pass


class BinarySearchTree(BinaryTree):
    """
    Instantiate an empty binary search tree as a subclass of BinaryTree, with 'add' and 'contains' methods.
    """
    def add(self,value):
        pass

        # def walk(node, node_to_add):

        #     if not node:
        #         return
            
        #     if node_to_add.value < node.value:
        #         if not node.left_child:
        #             node.left_child = node_to_add
        #         else:
        #             walk(node.left_child, node_to_add)
        #     else:
        #         if not node.right_child:
        #             node.right_child = node_to_add
        #         else:
        #             walk(node.right_child, node_to_add)

        # new_node = TreeNode(value)

        # if not self.root_node:
        #     self.root_node = new_node
        #     return

        # walk(self.root_node, new_node)
        


    def contains(self,value):
        pass




if __name__ == "__main__":
    pass

