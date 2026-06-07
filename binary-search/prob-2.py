
# ===== 2==============#
# ===============Return index of first occurrence of an element in sorted array (duplicates allowed)==========================

# arr=[1,2,3,4,5,6,6,7]
# target=6 (first ocuurance)


def first_occurance(arr,target):
    low=0
    high=len(arr)-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if target==arr[mid]:
            ans=mid
            high=mid-1
        elif target>arr[mid]:
            low=mid+1
        else:
            high=mid-1

    return ans

print(first_occurance([1,2,3,4,5,6,6,7],6))            
            
    
