# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i, j, k = 0, 0, 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i+=1
        else:
            merged_arr[k] = arrB[j]
            j+=1
        k+=1
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i+=1
        k+=1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j+=1
        k+=1

    # return merged_arr
# test_array1 = [1,3,4,5]
# test_array2 = [2,6,7,8,9]
# print(merge(test_array1, test_array2))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
#     # Your code here
    if len(arr) >1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(left, right)
        # i, j, k = 0, 0, 0

        # while i< len(left) and j < len(right):
        #     if left[i] < right[j]:
        #         arr[k] = left[i]
        #         i+= 1
        #     else:
        #         arr[k] = right[j]
        #         j+= 1
        #     k+=1
        # while i < len(left):
        #     arr[k] = left[i]
        #     i+= 1
        #     k+= 1
        # while j < len(right):
        #     arr[k] = right[j]
        #     j+= 1
        #     k+= 1

    return arr

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


# helper function to partition the input array
# def partition(arr):
#     #pick a pivot
#     pivot = arr[0]
#     left = []
#     right = []

#     # partition the elements around the pivot
#     for x in arr[1:]:
#         if x <= pivot:
#             left.append(x)
#         else:
#             right.append(x)

#     # we have elements partitioned in the left, pivot, and right arrays
#     return left, pivot, right

# def quicksort(arr):
#     # base case
#     # if len(arr) is <= 1
#     if len(arr) <= 1:
#         return arr
    
#     #otherwise, we need to call our partition function to break the input array into smaller chunks
#     left, pivot, right = partition(arr)

#     #stick the pivot in a list
#     pivot = [pivot]

#     #run quicksort on the left and right chunks
#     # to break them down further
#     qleft = quicksort(left)
#     qright = quicksort(right)

#     # concatenate all the pieces together
#     return quicksort(left) + [pivot] + quicksort(right)
