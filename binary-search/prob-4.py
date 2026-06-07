# Count occurrences of a target in sorted array

## arr=[1,2,3,4,5,5,5,]
#target 5

def first(arr,target):
    low=0
    high=len(arr)-1
    first_occu=-1
    
    
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            first_occu=mid
            high=mid-1
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return first_occu

def last(arr,target):
    low=0
    high=len(arr)-1
    last_ocuurane=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            last_ocuurane=mid
            low=mid+1
        elif arr[mid]>target :
            high=mid-1
        else:
            low=mid+1
         
    
    return last_ocuurane

def count_occ(arr,target):
    f=first(arr,target)

    if f== -1:
        return 0
    l=last(arr,target)
    return l-f+1
print(count_occ([1,2,3,4,5,5,5,],5))




