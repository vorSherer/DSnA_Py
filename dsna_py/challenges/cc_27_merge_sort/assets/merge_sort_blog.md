# Challenge 27: Merge Sort
This project demonstrates the documentation and implementation of a merge sort.
Working from the pseudocode below, I will trace the algorithm by stepping through the process with each of the provided sample lists, showing the step-by-step output after each iteration through the algorithm.

## PSEUDOCODE:
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


---

# Example 1
## TRACE:
Sample List: 	[ 8, 4, 23, 42, 16, 15]

---

#### PASS 1:
```        INITIAL:                             RESULT:
  j  i                        i = 1
[ 8, 4, 23, 42, 16, 15]       j = 0     [ 4, 8, 23, 42, 16, 15]
  0  1   2   3   4   5     temp = 4       0  1   2   3   4   5
                         arr[j] = 8
```
In the first pass, we evaluate whether the number at list index 1 (stored in temp) is smaller than the value at index j (i.e., i-1, index 0). Since it is, the index 0 value is moved to index 1. As we are at the beginning of the list and there are no more values to the left to evaluate, the temp value is stored at index 0, completing the While loop and the first pass through the For loop.


#### PASS 2:

---

## Efficency
TBD
<!-- - __Time: O(n^2)__
	- The basic operation of this algorithm is comparison; worst case, this will happen __n * (n-1)__ number of times, thus the algorithm is simplified to __`n`__ squared.
- __Space: O(1)__
	- No additional space is being created: This array is being sorted in place, resulting in an __`O(1)`__ complexity. -->

