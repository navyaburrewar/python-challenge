
# Selection Sort selects the smallest element from the unsorted list 
# and places it at the beginning.
# Time Complexity: O(n²)



#========= 4. Algorithm Steps==============#

"""
Assume the first element is the minimum.
Compare it with all remaining elements.
Find the smallest element in the unsorted part.
Swap the smallest element with the first unsorted position.
Move the boundary of the sorted part by one position.
Repeat for the remaining unsorted elements.
Continue until the entire array becomes sorted.

"""

# ================ basic algorithum =================#
"""
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
            min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr        
"""