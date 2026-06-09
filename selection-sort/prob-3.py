# 3. Count Number of Swaps

# Modify Selection Sort to count how many swaps are performed.
# arr = [29, 10, 14, 37, 13]
# Your program should print:

# Sorted array
# Total swaps


def selection_sort(arr):
    count=0
    for i in range(len(arr)):
        min_inde=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_inde]:
                min_inde=j
        if min_inde !=i:        
            arr[i],arr[min_inde]=arr[min_inde],arr[i]
            count+=1
    return  arr,count
print(selection_sort([29, 10, 14, 37, 13]))           