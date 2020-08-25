# Challenge 26: Insertion Sort
This project demonstrates the documentation and implementation of an insertion sort.
Working from the pseudocode below, I will trace the algorithm by stepping through the process with each of the provided sample lists, showing the step-by-step output after each iteration through the algorithm.

## PSEUDOCODE:
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
```        INITIAL:                                      RESULT:
     j   i                i =  2    temp  arr[j]
[ 4, 8, 23, 42, 16, 15]   j =  1     23 !<  8      [ 4, 8, 23, 42, 16, 15]
  0  1   2   3   4   5                               0  1   2   3   4   5
```
In the second pass, we evaluate whether the number at list index 2 (stored in temp) is smaller than the value at index j (i.e., i-1, index 1). Since it is not, the While loop is hereafter skipped and the temp value is re-stored at index 2, completing the second pass through the For loop.


#### PASS 3:
```        INITIAL:                                      RESULT:
         j   i            i =  3    temp  arr[j]
[ 4, 8, 23, 42, 16, 15]   j =  2     42 !< 23      [ 4, 8, 23, 42, 16, 15]
  0  1   2   3   4   5                               0  1   2   3   4   5
```
In the third pass, we evaluate whether the number at list index 3 (stored in temp) is smaller than the value at index j (i.e., i-1, index 2). Since it is not, the While loop is hereafter skipped and the temp value is re-stored at index 3, completing the third pass through the For loop.

#### PASS 4:
```        INITIAL:                    temp  arr[j]      RESULT:
             j   i        i =  4     16  < 42   
[ 4, 8, 23, 42, 16, 15]   j =  3     16  < 23      [ 4, 8, 16, 23, 42, 15]
  0  1   2   3   4   5               16 !<  8        0  1   2   3   4   5
```
In the fourth pass, we evaluate whether the number at list index 4 (stored in temp) is smaller than the value at index j (i.e., i-1, index 3). Since it is, the index 3 value is moved to index 4 and j is decremented. The value in temp is then evaluated against the value at the new j (i.e., index 2) and is also found to be lower. The index 2 value is moved to index 3, j is again decremented and temp is evaluated against the value at the new j (i.e., index 1). Since the value in temp is not less than the value at index 1, the While loop is hereafter skipped and the temp value is re-stored at index 2.


#### PASS 5:
```        INITIAL:                    temp  arr[j]      RESULT:
                 j   i    i =  5     15  < 42   
[ 4, 8, 16, 23, 42, 15]   j =  4     15  < 23      [ 4, 8, 15, 16, 23, 42]
  0  1   2   3   4   5               15  < 16        0  1   2   3   4   5
                                     15 !<  8
```
In the fifth pass, we evaluate whether the number at list index 5 (stored in temp) is smaller than the value at index j (i.e., i-1, index 4). Since it is, the index 4 value is moved to index 5 and j is decremented. The value in temp is then evaluated against the value at the new j (i.e., index 3) and is again found to be lower. The index 3 value is moved to index 4, j is again decremented and temp is evaluated against the value at the new j (i.e., index 2). The value in temp is again found to be lower. The index 2 value is moved to index 3, j is again decremented and temp is evaluated against the value at the new j (i.e., index 1). Since the value in temp is not less than the value at index 1, the While loop is hereafter skipped and the temp value is re-stored at index 2. Since we have reached the end of the list, the For loop is also complete, leaving the list sorted.


## Efficency
- __Time: O(n^2)__
	- The basic operation of this algorithm is comparison; worst case, this will happen __n * (n-1)__ number of times, thus the algorithm is simplified to __`n`__ squared.
- __Space: O(1)__
	- No additional space is being created: This array is being sorted in place, resulting in an __`O(1)`__ complexity.

---
