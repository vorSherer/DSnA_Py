# FizzBuzzTree
Conduct “FizzBuzz” on a k-ary tree while traversing through it to create a new tree.

Set the values of each of the new nodes depending on the corresponding node value in the source tree.

## Challenge 18
- Write a function called __`FizzBuzzTree`__ which takes a __k-ary tree__ as an argument.
- Without utilizing any of the built-in methods available to your language, determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:
	- If the value is divisible by 3, replace the value with __*"Fizz"*__
	- If the value is divisible by 5, replace the value with __*"Buzz"*__
	- If the value is divisible by 3 and 5, replace the value with __*"FizzBuzz"*__.
	- If the value is not divisible by 3 or 5, simply turn the number into a __String__. <br>
- Return a __*new*__ tree.

- Write unit tests.

## Approach & Efficiency
__Big O space complexity__ for this approach is __`O(n)`__ <br>
__Big O time complexity__ for this approach is __`O(n**2)`__ <br>

## API
<!-- Descriptions of each method publicly available to my k-ary tree are detailed above (q.v.). -->

My code is [here](./fizz_buzz_tree.py)

## Code Challenge 18 whiteboards:
<!-- ![CC-18 FizzBuzzTree - 1](./RELATIVE_PATH) -->
<!-- ![CC-18 FizzBuzzTree - 2](./RELATIVE_PATH) -->
<!-- ![CC-18 FizzBuzzTree - 3](./RELATIVE_PATH) -->


## Attributions
- root directory __.gitignore__ content courtesy of https://www.toptal.com/developers/gitignore/api/python

- __ics.uci.edu__ helped with [envisioning a k-ary tree](https://www.ics.uci.edu/~brgallar/week6_3.html)

- __Geeks for Geeks__ helped with starter code for
	- [Iterative Preorder Traversal of an N-ary Tree](https://www.geeksforgeeks.org/iterative-preorder-traversal-of-a-n-ary-tree/), <br>
	- [constructing the full k-ary tree from its preorder traversal](https://www.geeksforgeeks.org/construct-full-k-ary-tree-preorder-traversal/), <br>




## Task Checklist: <br>
- [X] Top-level README “Table of Contents” is updated <br>
- [ ] Feature tasks for this challenge are completed <br>
- [ ] Unit tests written and passing <br>
    - [ ] “Happy Path” - Expected outcome <br>
    - [ ] Expected failure <br>
    - [ ] Edge Case (if applicable/obvious) <br>
- [ ] README for this challenge is complete <br>
    - [ ] Summary, Description, Approach & Efficiency, Solution <br>
    - [X] Link to code <br>
    - [ ] Pictures of whiteboards <br> -->

###### PR for new directory: https://github.com/vorSherer/DSnA_Py/pull/21
