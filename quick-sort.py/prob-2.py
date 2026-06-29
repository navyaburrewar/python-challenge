# Perform one partition step on the array:
# [8, 3, 1, 7, 0, 10, 2]

# using the last element as the pivot.



def quick_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    pivot=arr[-1]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quick_sort(left)+middle+right
print(quick_sort([8, 3, 1, 7, 0, 10, 2]))
