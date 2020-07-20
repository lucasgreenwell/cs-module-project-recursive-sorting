# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    middle = (start + end) // 2
    if len(arr) < 1:
        return -1
    elif target == arr[middle]:
        return middle
    elif target == arr[start]:
        return start
    elif target == arr[end]:
        return end
    elif target > arr[middle]:
        return binary_search(arr, target, middle + 1, end)
    elif target < arr[middle]:
        return binary_search(arr, target, start, middle - 1)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    if arr[0] < arr[1]:
        low = 0
        high = len(arr) - 1
        while low <= high:
            middle = (high + low) // 2
            if arr[middle] == target:
                return middle
            elif arr[high] == target:
                return high
            elif arr[low] == target:
                return low
            elif target < arr[middle]:
                high = middle - 1
            elif target > arr[middle]:
                low = middle + 1

        return -1
    else:
        low = 0
        high = len(arr) - 1
        while low <= high:
            middle = (high + low) // 2
            if arr[middle] == target:
                return middle
            elif arr[high] == target:
                return high
            elif arr[low] == target:
                return low
            elif target > arr[middle]:
                high = middle - 1
            elif target < arr[middle]:
                low = middle + 1

        return -1