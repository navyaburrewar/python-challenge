# 2. Descending Order Bubble Sort

# Sort the array in descending order using Bubble Sort.

# Example:

# Input: [3, 1, 5, 2]
# Output: [5, 3, 2, 1]



def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):   ## here -1 will removes the soted last element index
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr
print(bubble_sort([3, 1, 5, 2]))            