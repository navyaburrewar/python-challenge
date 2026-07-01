# Question 6

# Modify Quick Sort so that it sorts
# Descending Order.

# Example
# Input
# 4 8 2 7 1

# Output
# 8 7 4 2 1




def quick_sort(arr):
    n=len(arr)
    if n<=1:
        return arr

    pivot=arr[-1]

    left=[ x for x in arr if x>pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x<pivot]

    return quick_sort(left)+middle+quick_sort(right)
print(quick_sort([4, 8, 2, 7, 1]))

