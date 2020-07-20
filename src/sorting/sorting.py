# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    #set up the indices you wanna mess with
    index_a = 0
    index_b = 0
    #loop through the array with all the filler crap in it
    for i in range(len(merged_arr)):
        #if the current index in b is out of range then insert from list a
        if index_b > len(arrB) - 1:
            merged_arr[i] = arrA[index_a]
            index_a += 1
        #and vice versa
        elif index_a > len(arrA) - 1:
            merged_arr[i] = arrB[index_b]
            index_b += 1
        # if the current thing in a is smaller than the current thing in b then insert from list a
        elif arrA[index_a] < arrB[index_b]:
            merged_arr[i] = arrA[index_a]
            index_a += 1
        #vice versa
        elif arrB[index_b] < arrA[index_a]:
            merged_arr[i] = arrB[index_b]
            index_b += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        left_arr_sorted = merge_sort(arr[:mid])
        right_arr_sorted = merge_sort(arr[mid:])
        sorted_arr = merge(left_arr_sorted, right_arr_sorted)
        return sorted_arr













# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

