# 6. Find Minimum Element in Each Pass

# During each pass of Selection Sort, print the minimum element found.

# Example Output:

# Pass 1 -> Minimum = 11
# Pass 2 -> Minimum = 12
# Pass 3 -> Minimum = 22



def selection_sort(arr):
    
    for i in range(len(arr)):
        min_inde=i
        
        for j in range(i+1,len(arr)):
            
            if arr[j]<arr[min_inde]:
                
                min_inde=j
        print(f"Pass {i+1} -> Minimum = {arr[min_inde]}")        
        arr[i],arr[min_inde]=arr[min_inde],arr[i]

print(selection_sort([5, 1, 8, 3, 2]))           