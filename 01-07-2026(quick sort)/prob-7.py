# Print the array after every partition step.

def quick_sort(arr):
   
   
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    pivot=arr[mid]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]

    print(left+middle+right)
    return quick_sort(left)+middle+quick_sort(right)
print(quick_sort([7,1,4,2,3,1]))

