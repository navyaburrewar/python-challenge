# Count the number of swaps performed.


def quick_sort(arr):
    n=len(arr)
    l=0
    r=n-1
    mid=(l+r)//2
    if n<=1:
        return arr
    pivot=arr[mid]
    count=0
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    
    
    return quick_sort(left)+middle+quick_sort(right)
    
    
    
print(quick_sort([3,1,4,2,7,1],))


