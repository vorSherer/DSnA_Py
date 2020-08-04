from collections import deque

class TreeNode:
    def __init__(self, value, child=[]):
        self.value = value
        self.child = child
    
    
def kthary_pre_order(root):
        """
        Implement a call stack_ to facilitate a k-ary traversal methodology and return a list of the values found.
        """
        stack_ = deque([])
        # 'pre_order' contains a list of all visited nodes
        pre_order = []
        pre_order.append(root.value)
        stack_.append(root)

        while len(stack_) > 0:
            # 'flag' indicates when all the child nodes have been visited
            flag = 0
            # Case-1; If top of stack_ is a leaf node, pop it off the stack_
            if len((stack_[len(stack_)-1]).child) == 0:
                x = stack_.pop()
            # Case-2; If top of stack_ is a parent with child:
            else:
                parent = stack_[len(stack_)-1]
            
            # When unvisited child is found (l-to-r search), push it onto the stack_ and store it in the pre_order list as 'visited', 
            # Start again from Case-1 to explore this 'visited' child node
            for i in range(0, len(parent.child)):
                if parent.child[i].value not in pre_order:
                    flag = 1
                    stack_.append(parent.child[i])
                    pre_order.append(parent.child[i].value)
                    break
            # If all child nodes of this parent have been visited, then pop the parent from the stack_
            if flag == 0:
                stack_.pop()

            return pre_order

        def walk(curr_node):
            pass
        #     # Break immediately if node is empty
        #     if not curr_node:
        #         return
            
        #     # Deal with the root
        #     values.append(curr_node.value)
        #     # Check for a left-child node
        #     walk(curr_node.left_child)
        #     # Check for a right-child node
        #     walk(curr_node.right_child)

        # walk(self.root_node)

        # return values
        
def fizz_buzz_tree(tree):
    pass
    # orig_tree = tree
    # new_tree = []

    # def build_new_tree(tree.root_node)
    #     curr_node = tree.root_node

    #         if curr_node.value % 15 == 0:
    #             new_node = "FizzBuzz"
    #         elif curr_node.value % 5 == 0:
    #             new_node = "Buzz"
    #         elif curr_node.value % 3 == 0:
    #             new_node = "Fizz"
    #         else:
    #             new_node = str(curr_node.value)
    # return new_tree





if __name__ == "__main__":
    root = TreeNode(1) 
    root.child.append(TreeNode(2)) 
    root.child.append(TreeNode(3)) 
    root.child.append(TreeNode(4))  
    root.child[0].child.append(TreeNode(5))  
    root.child[0].child[0].child.append(TreeNode(10))  
    root.child[0].child.append(TreeNode(6))  
    root.child[0].child[1].child.append(TreeNode(11)) 
    root.child[0].child[1].child.append(TreeNode(12)) 
    root.child[0].child[1].child.append(TreeNode(15))  
    root.child[2].child.append(TreeNode(7)) 
    root.child[2].child.append(TreeNode(8)) 
    root.child[2].child.append(TreeNode(9)) 
        
    print(kthary_pre_order(root))
    # Expected Output: [1, 2, 5, 10, 6, 11, 12, 15, 3, 4, 7, 8, 9]
