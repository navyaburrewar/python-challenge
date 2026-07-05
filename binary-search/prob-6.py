# Implement upper bound (first index > target)

arr=[1,2,3,4,5,6]

target=2
#upper bound means that target sholud upper

def upper_bound(arr,target):
    low=0
    high=len(arr)-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if target<arr[mid]:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

print(upper_bound([1,2,3,4,6,7,5]))        