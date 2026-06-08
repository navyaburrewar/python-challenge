# 1. Basic Bubble Sort

# Write a function to sort an array in ascending order using Bubble Sort.

# Example:

# Input: [5, 1, 4, 2]
# Output: [1, 2, 4, 5]


def ase_ord(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j] ,arr[j+1]=arr[j+1],arr[j]
    return arr
print(ase_ord([5, 1, 4, 2]))            
            




