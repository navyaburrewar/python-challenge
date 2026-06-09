# 4. Count Number of Comparisons

# Write a Selection Sort program that counts total comparisons.

# Hint:

# comparisons += 1


def selection_sort(arr):
    comparisons=0
    for i in range(len(arr)):
        min_inde=i
        for j in range(i+1,len(arr)):
            comparisons+=1
            if arr[j]<arr[min_inde]:
                
                min_inde=j
        arr[i],arr[min_inde]=arr[min_inde],arr[i]

    return  arr,comparisons
print(selection_sort([5, 1, 8, 3, 2]))           