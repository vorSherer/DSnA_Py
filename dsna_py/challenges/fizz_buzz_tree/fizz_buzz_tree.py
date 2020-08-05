from collections import deque

class TreeNode:
    def __init__(self, value, child=None):
        self.value = value
        if child == None:
            self.child = []
        else:
            self.child = child
    
    
def fizz_buzz_tree(tree):
    new_tree = None
    arg_node = tree

    def fizz_buzz_node_maker(fb_node):
        if fb_node.value % 15 == 0:
            new_node = TreeNode("FizzBuzz")
        elif fb_node.value % 5 == 0:
            new_node = TreeNode("Buzz")
        elif fb_node.value % 3 == 0:
            new_node = TreeNode("Fizz")
        else:
            new_node = TreeNode(str(fb_node.value))
        
        return new_node

    def walk(curr_node, new_tree_node):
        nonlocal new_tree

        # Break immediately if node is empty
        if not curr_node:
            return
        
        # Raise exception if node vlue is not an integer
        if not type(curr_node.value) is int:
            raise TypeError('Node value is not an integer.')
                
        # Deal with the root
        fb_tree_node = fizz_buzz_node_maker(curr_node)
        if new_tree is None:
            new_tree = fb_tree_node
        else:
            new_tree_node.child.append(fb_tree_node)

        # walk ttrough child nodes
        for child in curr_node.child:
            walk(child, fb_tree_node)


    walk(arg_node, new_tree)

    return new_tree






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

    fb_tree = fizz_buzz_tree(root)
    print(fb_tree)
