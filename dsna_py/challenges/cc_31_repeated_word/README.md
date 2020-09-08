# Hashing and Hash Tables - Repeated Word
Find the first repeated word in a book.

## Specifications
- Read all of the following instructions carefully. Name things exactly as described.
- Do all your work in a public repository (matching the example provided by your instructor) called __`data-structures-and-algorithms`__, with a well-formatted, detailed __top-level README.md__
- Create a branch in your repository called __`repeated-word`__
- On your branch, create a folder named __`repeated_word`__ which contains a file called __`repeated_word.py`__
- Include any language-specific configuration files required for this challenge to become an individual component, module, library, etc.
	- __*NOTE: You can find an example of this configuration for your course in your class lecture repository.*__

## Feature Tasks
* Write a function that accepts a lengthy string parameter.
* Without utilizing any of the built-in library methods available to python, return the first word to occur more than once in that provided string.

## Structure and Testing
Utilize the *Single-responsibility principle*: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write at least three test assertions for each method that you define.

Ensure your tests are passing before you submit your solution.

## Example

__*Input*__
__`"Once upon a time, there was a brave princess who..."`__ <br>
__*Output*__	__`"a"`__ <br>

__*Input*__
__`"It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."`__ <br>
__*Output*__  __`"it"`__ <br>

__*Input*__
__`"It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."`__ <br>
__*Output*__	__`"summer"`__ <br>

---

## Approach & Efficiency
<!-- __Big O space complexity__ for this approach is __`O(n)`__ <br>
__Big O time complexity__ for this approach is __`O(n)`__ <br>
__Big O time complexity for insertion/deletion__ is __`O(1)`__ <br> -->

## API
<!-- Descriptions of each method publicly available to my NN are detailed above (q.v.). -->

My code is [here](./repeated_word.py)

---

## Code Challenge 31 whiteboards:
<!-- ![CC-31 repeated word - 1](./RELATIVE_PATH) -->

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
