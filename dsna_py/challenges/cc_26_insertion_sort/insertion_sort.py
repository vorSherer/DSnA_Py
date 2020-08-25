def insertion_sort(list_):
    for i in range(1, len(list_)):

        j = i-1
        temp_value = list_[i]

        while j >= 0 and list_[j] > temp_value:
            list_[j + 1] = list_[j]
            j -= 1
        
        list_[j + 1] = temp_value

    return list_





if __name__ == "__main__":
    lst1 = [ 8, 4, 23, 42, 16, 15]
    print(insertion_sort(lst1))
