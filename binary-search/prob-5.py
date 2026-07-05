#  Lower Bound / Upper Bound Pattern

#  5. Implement lower bound (first index ≥ target)

# arr=[1,2,3,4,5,6,7,8]
# target 4

def lowerbound(arr,target):
    low=0
    high=len(arr)-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        
        if arr[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
print(lowerbound([1,2,3,4,5,6,7,8],4))  
print(lowerbound([1,2,3,4,5,5,6,7,8],9)) 
print(lowerbound([1,3,4,5,6,7,8],2)) 




