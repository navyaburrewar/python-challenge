# 3. Count Total Swaps

# Modify Bubble Sort to count how many swaps happen.

# Example:

# Input: [4, 3, 2, 1]
# Output: 6 swaps

def bubble_sort(arr):
    count=0
    for i in range(len(arr)):
        
        for j in range(0,len(arr)-i-1):   ## here -1 will removes the soted last element index
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                count+=1   
    return arr,count
arr,count=bubble_sort([4, 3, 2, 1]) 

print("sorted Array:",arr) 
print("total_swap",count)
