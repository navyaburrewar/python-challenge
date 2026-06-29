
# [8, 3, 1, 7, 0, 10, 2]

# using the last element as the pivot.

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quick_sort(left)+middle+quick_sort(right)
arr=[8, 3, 1, 7, 0, 10, 2]
print("sorted arrray", quick_sort(arr))