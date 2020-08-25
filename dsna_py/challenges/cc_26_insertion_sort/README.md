# Insertion Sort
This project demonstrates the documentation and implementation of an insertion sort.

## Challenge 26
Review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

Once you are done with your article, code a working, tested implementation of Insertion Sort based on the pseudocode provided.

---

## Pseudocode
```
InsertionSort(int[] arr)

  FOR i = 1 to arr.length

    int j <-- i - 1
    int temp <-- arr[i]

    WHILE j >= 0 AND temp < arr[j]
      arr[j + 1] <-- arr[j]
      j <-- j - 1

    arr[j + 1] <-- temp
```

### Sample Arrays
In your blog article, visually show the output of processing this input array:

__`[8,4,23,42,16,15]`__

For your own understanding, consider also stepping through these inputs:

- Reverse-sorted: __`[20,18,12,8,5,-2]`__
- Few uniques: __`[5,12,7,5,5,7]`__
- Nearly-sorted: __`[2,3,5,7,13,11]`__

---

## Implementation
- Provide a visual step through for each of the sample arrays based on the provided pseudocode.
- Convert the pseudocode into working code in python.
- Present a complete set of working tests.


## Approach & Efficiency
__Big O space complexity__ for this approach is __`O(1)`__ <br>
__Big O time complexity__ for this approach is __`O(n^2)`__ <br>
__Big O time complexity for comparison__ is __`O(1)`__ <br>


My code is [here](./insertion_sort.py)

## Code Challenge 26 blog / whiteboards:
[CC-26 insertion sort blog.md file](./assets/insert_sort_blog.md)

---

## Task Checklist: <br>
- [X] Top-level README “Table of Contents” is updated <br>
- [ ] Feature tasks for this challenge are completed <br>
- [ ] Unit tests written and passing <br>
    - [ ] “Happy Path” - Expected outcome <br>
    - [ ] Expected failure <br>
    - [ ] Edge Case (if applicable/obvious) <br>
- [X] README for this challenge is complete <br>
    - [X] Summary, Description, Approach & Efficiency, Solution <br>
    - [X] Link to code <br>
    - [X] Link to blog.md in lieu of whiteboards <br>

###### PR for new directory: NN
