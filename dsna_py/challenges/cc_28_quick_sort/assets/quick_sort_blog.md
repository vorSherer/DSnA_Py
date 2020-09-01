# Challenge 28: Quick Sort
This project demonstrates the documentation and implementation of a quick sort.
Working from the pseudocode below, I will trace the algorithm by stepping through the process with each of the provided sample lists, showing the step-by-step output after each iteration through the algorithm.

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

---

# Example 1
## TRACE:
Sample List: 	[ 8, 4, 23, 42, 16, 15]

---

#### Partition Whole List:
```        SETUP:
  l              r   p    pivot = 15
[ 8, 4, 23, 42, 16, (15)]  left =  8
  0  1   2   3   4   5    right = 16
```
To begin partitioning, set the left pointer to the first index of the list and the right pointer to the last.  Then the value of the right pointer is assigned to the 'pivot' variable and right pointer is re-assigned one place to the left (i.e., len(list)-1).
---
```   Left Pointer:
         l       r   p    pivot = 15
[ 8, 4, 23, 42, 16, (15)]  left = 23
  0  1   2   3   4   5    right = 16
```
The value at the left pointer is recursively compared to the pivot value; while the left value is less than or equal to the pivot, left pointer is moved one index to the right. Once the left value is greater than or equal to the pivot value, the left pointer stops.
---
```  Right Pointer:
        lr           p    pivot = 15
[ 8, 4, 23, 42, 16, (15)]  left = 23
  0  1   2   3   4   5    right = 23
```
Once the left pointer stops, the right pointer is activated, again recursively comparing the right value to be greater than or equal to the pivot value. In this example, there are no values less than the Pivot value, so the right pointer eventually meets the left and stops. Had the right pointer stopped at value is less than or equal to the pivot value, the left and right values would have been swapped.
---
```  Pivot Swap:
         p          lr    pivot = 15
[ 8, 4, 15, 42, 16, 23]    left = 23    
  0  1   2   3   4   5    right = 23
```
Once the left and right pointers meet, the pointers no longer are moved.  At this point the pivot value and that at the left pointer are swapped.
---
``` Partition Left:
  lr  p                   pivot =  4
[ 8, (4), 15, 42, 16, 23]  left =  8
  0  1   2   3   4   5    right =  8
```
Now the sublist to the left of the pivot value gets partitioned; the right-most value in the sublist becomes the new pivot and left and right pointers are set as before. The left sublist would be partitioned as before. In this example, however, both pointers are initially set to the same position, ending pointer movement. 
---
```  Pivot Swap:
  p lr                    pivot =  4
[ 4, 8, 15, 42, 16, 23]    left =  8
  0  1   2   3   4   5    right =  8
```
As before, the pivot value is swapped with that of the left pointer. moved.  At this point the pivot value and that at the left pointer are swapped. This process would be repeated until all values to the left of the original pivot have been evaluated as a pivot.
---
``` Partition Right:
             l   r   p    pivot = 23
[ 4, 8, 15, 42, 16, (23)]  left = 42
  0  1   2   3   4   5    right = 16
```
Now the sublist to the right of the original pivot value gets partitioned; the right-most value becomes the new pivot and left and right pointers are set as before. The left pointer value is compared to the pivot value; in this example, it is greater, so the left pointer stops. The right pointer value is compared next; since it is less than the pivot value, the right pointer stops.
---
```  Value Swap:
             l   r   p    pivot = 23    
[ 4, 8, 15, 16, 42, (23)]  left = 42    
  0  1   2   3   4   5    right = 16    
```
Since both pointers have stopped, their values are swapped.
---
```   Left Pointer:     
                lr   p    pivot = 23
[ 4, 8, 15, 16, 42, (23)]  left = 42
  0  1   2   3   4   5    right = 16
```
The left pointer value (16) is now less than the pivot value, so it moves right. Since both pointers now point to the same position, they both stop.

```  Pivot Swap:
                 p  lr    pivot =  4
[ 4, 8, 15, 16, 23, 42]    left =  8
  0  1   2   3   4   5    right =  8
```
Since both pointers have stopped and the value at the left pointer is less than the pivot value, the left pointer value and the pivot value are swapped. This process also continues until all values to the right of the original pivot have also been evaluated as pivots. The list is now sorted in place.
---

## Efficency
- __Time: O(n * log n)__
	- The basic operation of this algorithm is partitioning via comparisons and swaps; worst case, this will happen __n^2 / 2__ number of times, thus the algorithm is simplified to __`n^2`__.
- __Space: O(1)__
	- No additional space is being created: This array is being sorted in place, resulting in an __`O(1)`__ complexity.

### Sample Arrays
For your own understanding, consider also stepping through these inputs:

- Reverse-sorted: __`[20,18,12,8,5,-2]`__
    [20,18,12,8,5,(-2)]
    [-2,18,12,8,5,(20)]
    [-2,18,12,8,5,(20)]
    [20,18,12,8,5,(-2)]
    [20,18,12,8,5,(-2)]
    [20,18,12,8,5,(-2)]
    [20,18,12,8,5,(-2)]

- Few uniques: __`[5,12,7,5,5,7]`__
- Nearly-sorted: __`[2,3,5,7,13,11]`__

---


