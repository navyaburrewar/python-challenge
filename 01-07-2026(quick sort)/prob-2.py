# Question 2: Partition Only

# Perform one partition on

# [8,4,7,9,3,10,5]

# Pivot = last element.

# Return

# Final array after partition
# Pivot index

def sorted_arry(arr):
    n=len(arr)
    if n<=1:
        return arr
    pivot=arr[-1]
    left=[x for x in arr if x<pivot]
    right=[x for x in arr if x>pivot]
    pivot_index=len(left)
    result=left+[pivot]+right
   
    return result,pivot_index
print(sorted_arry([8,4,7,9,3,10,5]))