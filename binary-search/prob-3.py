#  prob-3
# Return index of last occurrence of an element in sorted array


def last_occurance(arr,target):
    low=0
    high=len(arr)-1
    ans=-1

    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            ans=mid
            low=mid+1
        elif arr[mid]>target: 
            high=mid-1
        else:
            low=mid+1
    return ans
print(last_occurance([1,2,2,3,5,6,4,],2))            
               