# 5. Sort User Input

# Take list elements from user input and sort them using Selection Sort.

# Example:

# Input:

# 5
# 64 25 12 22 11

# Output:
# [11, 12, 22, 25, 64]

def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_inde=i
        for j in range(i+1,n):
            
            if arr[j]<arr[min_inde]:
                
                min_inde=j
        arr[i],arr[min_inde]=arr[min_inde],arr[i]

    return  arr
n=int(input())
arr=list(map(int,input().split()))[:n]
print(selection_sort(arr))           