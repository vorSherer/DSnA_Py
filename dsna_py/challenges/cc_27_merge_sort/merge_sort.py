def merge_sort(arr):
    n = len(arr)

    if n > 1:
        mid = int(n/2)
        left = arr[:mid]
        print("Left= ", left)
        right = arr[mid:]
        print("Right= ", right)
        merge_sort(left)
        print("Sorted left= ", left)
        merge_sort(right)
        print("Sorted right= ", right)
        merge(left, right, arr)
    return arr


def merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        print("Left len= ", len(left))
        print("Right len= ", len(right))
        # print("K going in= ", k)
        if left[i] <= right[j]:
            arr[k] = left[i]
            print(f"Left.appended arr[k]= {arr[k]}, i= {i}.")
            i += 1
        else:
            arr[k] = right[j]
            print(f"Right.appended arr[k]= {arr[k]}, j= {j}.")
            j += 1
        k += 1
        # print("K coming out= ", k)

    # try:
    #     if i == len(left):
    #         arr[k].append(right[j]
    #     else:
    #         arr[k].append(left[i]
    # except:
    #     print("OK, THAT didn't work!")

    return arr





if __name__ == "__main__":
    lst1 = [8,4,23,42,16,15]
    print(merge_sort(lst1))
