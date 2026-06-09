# 2. Descending Order Selection Sort

# Sort the list in descending order using Selection Sort.
# arr = [5, 1, 8, 3, 2]

# Expected Output:
# [8, 5, 3, 2, 1]

def selection_sort(arr):
    for i in range(len(arr)):
        max_inde=i
        for j in range(i+1,len(arr)):
            if arr[j]>arr[max_inde]:
                max_inde=j
        arr[i],arr[max_inde]=arr[max_inde],arr[i]

    return  arr
print(selection_sort([5, 1, 8, 3, 2]))           