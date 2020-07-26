# Binary Tree and BST Implementation
This project demonstrates the instantiation and modification of a __Binary Tree__ and __Binary Search Tree (BST)__ Implementation.

## Challenge 15
- Create a __`Node`__ class that has properties for the value stored in the node, the __left child__ node, and the __right child__ node.
- Create a __`BinaryTree`__ class:
	- Define a method for each of the depth-first traversals called __`preOrder`__, __`inOrder`__, and __`postOrder`__ which returns a list of the values, ordered appropriately.
- __Any exceptions or errors that come from your code should be semantic, capturable errors.__ For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

- Create a __`BinarySearchTree`__ class:
	- Define a method named __`add`__ that accepts a __value__, and *adds a new node with that value in the correct location* in the binary search tree.
	- Define a method named __`contains`__ that accepts a __value__, and __*returns a boolean__ indicating whether or not the value is in the tree* at least once.

#### Write tests to prove the following functionality: <br>
1. Can successfully instantiate an empty tree
1. Can successfully instantiate a tree with a single root node
1. Can successfully add a left child and right child to a single root node
1. Can successfully return a collection from a preorder traversal
1. Can successfully return a collection from an inorder traversal
1. Can successfully return a collection from a postorder traversal

<!-- ## Challenge NN -->
<!-- Feature summary. -->

<!-- ## Challenge NN -->
<!-- Feature summary. -->

## Approach & Efficiency
#### For Binary Trees: 
The __Big O space complexity for a node insertion using breadth first insertion__ will be __`O(w)`__, where __`w`__ is the largest width of the tree. <br>
__Big O time complexity__ for this approach is as follows: <br>
- for __inserting a new node__ is __`O(n)`__ <br>
- for __searching for a specific node__ will also be __`O(n)`__. <br>
A "perfect" binary tree is one where every non-leaf node has exactly two children. The maximum width for a perfect binary tree, is __`2^(h-1)`__, where __`h`__ is the height of the tree. Height can be calculated as __`log n`__, where __`n`__ is the number of nodes.

#### For a Binary Search Tree:
The __Big O time complexity__ of a Binary Search Tree’s __insertion and search__ operations is __`O(h)`__, or __`O(height)`__. <br>
In a balanced (or "perfect") tree, the height of the tree is __`log(n)`__. In an unbalanced tree, the worst case height of the tree is __`n`__.

The __Big O space complexity of a BST search__ would be __`O(1)`__.

## API
Descriptions of each method publicly available to my Binary Trees are detailed above (q.v.).

<!-- My code is [here]() -->

## Code Challenge N whiteboards:
<!-- ![CC-15 binary tree - 1](./RELATIVE_PATH) -->
<!-- ![CC-15 binary tree - 2](./RELATIVE_PATH) -->
<!-- ![CC-15 binary tree - 3](./RELATIVE_PATH) -->

## Code Challenge N whiteboard:
<!-- ![CC-16 binary tree - 1](./RELATIVE_PATH) -->

## Code Challenge N whiteboard:
<!-- ![CC-17 binary tree - 1](./RELATIVE_PATH) -->


## Task Checklist: <br>
<!-- - [ ] Top-level README “Table of Contents” is updated <br>
- [ ] Feature tasks for this challenge are completed <br>
- [ ] Unit tests written and passing <br>
    - [ ] “Happy Path” - Expected outcome <br>
    - [ ] Expected failure <br>
    - [ ] Edge Case (if applicable/obvious) <br>
- [ ] README for this challenge is complete <br>
    - [X] Summary, Description, Approach & Efficiency, Solution <br>
    - [ ] Link to code <br>
    - [ ] Pictures of whiteboards <br> -->

###### PR for new directory: NN
