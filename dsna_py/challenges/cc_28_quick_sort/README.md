# Quick Sort
This project demonstrates the documentation and implementation of a quick sort.

## Challenge 28
## Feature summary:

Review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

Once you are done with your article, code a working, tested implementation of Quick Sort based on the pseudocode provided.


---

## Pseudocode
```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value 
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right. 
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
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
<!-- __Big O space complexity__ for this approach is __`O(1)`__ <br>
__Big O time complexity__ for this approach is __`O(n^2)`__ <br>
__Big O time complexity for comparison__ is __`O(1)`__ <br> -->


My code is [here](./quick_sort.py)

## Code Challenge 28 blog / whiteboards:
[CC-28 quick sort blog.md file](./assets/quick_sort_blog.md)

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
