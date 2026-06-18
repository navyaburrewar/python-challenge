# 5. Check if Array is Already Sorted

# Before sorting, determine whether the array is already sorted.

# Input:

# [1, 2, 3, 4, 5]

def funct(arr):
    if all(arr[i]<=arr[i+1] for i in range(len(arr)-1)):
        return "already sorted"
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

    return arr
print(funct([1, 2, 3, 4, 5]))        
        