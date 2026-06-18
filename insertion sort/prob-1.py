# 1. Basic Insertion Sort
# Write a function to sort an array of integers using Insertion Sort.

# Input:
# [5, 2, 4, 6, 1, 3]

# Output:
# [1, 2, 3, 4, 5, 6]


def funct(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print(funct([5, 2, 4, 6, 1, 3]))            