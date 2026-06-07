#  Find ceil of an element in sorted array

# arr=[1,2,3,4,5,7,8]
# target=6

def ceil(arr,target):
    low=0
    high=len(arr)-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if target<=arr[mid]:
            ans=mid
            high=mid-1
        else:
            
            low=mid+1

    return ans
print(ceil([1,2,3,4,5,6],5))            
print(ceil([1,2,3,5,6],4)) 
print(ceil([1,2,3,4,5,6],8))       

## ans in index not value