# 1. Basic Selection Sort

# Write a Python program to sort the given list in ascending order using Selection Sort.
# arr = [64, 25, 12, 22, 11]

# Expected Output:
# [11, 12, 22, 25, 64]


def selection_sort(arr):
    for i in range(len(arr)):
        min_ind=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_ind]:
                min_ind=j
        arr[i],arr[min_ind]=arr[min_ind],arr[i]

    return arr
print(selection_sort([64, 25, 12, 22, 11]))            
