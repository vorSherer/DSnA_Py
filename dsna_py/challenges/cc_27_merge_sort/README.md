# Merge Sort
This project demonstrates the documentation and implementation of a merge sort.

## Challenge 27
Review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

Once you are done with your article, code a working, tested implementation of Merge Sort based on the pseudocode provided.

---

## Pseudocode
```
ALGORITHM Mergesort(arr)
  DECLARE n <-- arr.length

  if n > 1
    DECLARE mid <-- n/2
    DECLARE left <-- arr[0...mid]
    DECLARE right <-- arr[mid...n]
    // sort the left side
    Mergesort(left)
    // sort the right side
    Mergesort(right)
    // merge the sorted left and right sides together
    Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
  DECLARE i <-- 0
  DECLARE j <-- 0
  DECLARE k <-- 0

  while i < left.length && j < right.length
    if left[i] <= right[j]
      arr[k] <-- left[i]
      i <-- i + 1
    else
      arr[k] <-- right[j]
      j <-- j + 1

    k <-- k + 1

  if i = left.length
    set remaining entries in arr to remaining values in right
  else
    set remaining entries in arr to remaining values in left
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
*************************************************************************
__Big O space complexity__ for this approach is __`O(1)`__ <br>
__Big O time complexity__ for this approach is __`O(n^2)`__ <br>
__Big O time complexity for comparison__ is __`O(1)`__ <br>
*************************************************************************


My code is [here](./merge_sort.py)

## Code Challenge 27 blog / whiteboards:
[CC-27 merge sort blog.md file](./assets/merge_sort_blog.md)

---

## Task Checklist: <br>
- [ ] Top-level README “Table of Contents” is updated <br>
- [ ] Feature tasks for this challenge are completed <br>
- [ ] Unit tests written and passing <br>
    - [ ] “Happy Path” - Expected outcome <br>
    - [ ] Expected failure <br>
    - [ ] Edge Case (if applicable/obvious) <br>
- [ ] README for this challenge is complete <br>
    - [ ] Summary, Description, Approach & Efficiency, Solution <br>
    - [ ] Link to code <br>
    - [ ] Link to blog.md in lieu of whiteboards <br>

###### PR for new directory: NN
