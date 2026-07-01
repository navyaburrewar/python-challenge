def sorted_arr(arr):
    pivot=arr[-1]
    left=[x for x in arr if x<pivot]
    right=[x for x in arr if x>pivot]
    pivot_index=len(left)
    result=left+[pivot]+right

    return result,pivot_index
print(sorted_arr([8, 4, 7, 9, 3, 1, 5]))