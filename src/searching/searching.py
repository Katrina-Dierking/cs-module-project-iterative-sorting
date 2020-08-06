def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) -1
    while low <= high:
        middle = low + (high -1 )//2
        if target == arr[middle]:
            return middle
        elif target > arr[middle]:
            low = middle + 1
        else:
            high = middle -1
    return -1  # not found
