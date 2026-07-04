# 3. Kth Smallest (Quick Select)

# Input

# Array:
# [7,10,4,3,20,15]
# k=3
# Expected Output
# 7

def quick_sort(arr):
    
    n=len(arr)
    if n<=1:
        return arr
    pivot=arr[0]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]

    return quick_sort(left)+middle+quick_sort(right)
arr=[6,7,2,8,9,1]
new_array=quick_sort(arr)
print(new_array)
k=int(input())
for i in range(len(new_array)):
    if i==k:
        print(new_array[k-1]) 







