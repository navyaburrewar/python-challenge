# 8. Sort in Descending Order

# Input

# [2,5,1,8]

# Expected Output

# [8,5,2,1]


# 7. Count Comparisons

def partition(arr,low,high):
    
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        
        if arr[j]>pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
            
        
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quick_sort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)

        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

arr=[3,6,1,8,1,0]
quick_sort(arr,0,len(arr)-1)
print(arr)   
