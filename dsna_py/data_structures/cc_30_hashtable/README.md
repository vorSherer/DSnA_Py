# Hashtables
This exercise explores the implementation of hashing and hash tables in python.

## Challenge
### Features
Implement a Hashtable with the following methods:

1. __`add`__: takes in both the __key__ and __value__. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
1. __`get`__: takes in the __key__ and returns the __value__ from the table.
1. __`contains`__: takes in the __key__ and returns a boolean, indicating if the key exists in the table already.
1. __`hash`__: takes in an arbitrary __key__ and returns an index in the collection. <br>

### Structure and Testing <br>
Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition. <br>

Write tests to prove the following functionality: <br>

1. Adding a key/value to your hashtable results in the value being in the data structure
1. Retrieving based on a key returns the value stored
1. Successfully returns null for a key that does not exist in the hashtable
1. Successfully handle a collision within the hashtable
1. Successfully retrieve a value from a bucket within the hashtable that has a collision
1. Successfully hash a key to an in-range value

## Approach & Efficiency
__Big O space complexity__ for this approach is __`O(n)`__ <br>
__Big O time complexity__ for this approach can be __`O(n)`__ but is typically closer to O(1) <br>
__Big O time complexity for lookup__ is __`O(1)`__ <br>

## API
This method has access to the full functionality of __Linked Lists__ for collision resolution.

My code is [here](./hashtable.py)

---

## Code Challenge N whiteboards:
<!-- ![CC-30 hashtable - 1](./RELATIVE_PATH) -->

---

## Task Checklist: <br>
- [X] Top-level README “Table of Contents” is updated <br>
- [X] Feature tasks for this challenge are completed <br>
- [ ] Unit tests written and passing <br>
    - [ ] “Happy Path” - Expected outcome <br>
    - [ ] Expected failure <br>
    - [ ] Edge Case (if applicable/obvious) <br>
- [ ] README for this challenge is complete <br>
    - [ ] Summary, Description, Approach & Efficiency, Solution <br>
    - [X] Link to code <br>
    - [ ] Pictures of whiteboards <br>

---

###### PR for new directory: PR
