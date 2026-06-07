#  Find floor of an element in sorted array

# arr=[1,2,3,4,5,7,8]
# target=6

def floor(arr,target):
    low=0
    high=len(arr)-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if target>=arr[mid]:
            ans=mid
            low=mid+1
        else:
            high=mid-1

    return ans
print(floor([1,2,3,4,5,6],5))            
print(floor([1,2,3,5,6],4)) 
print(floor([1,2,3,4,5,6],8))       

## ans in index not value