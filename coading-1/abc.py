#================Find an element in a sorted array==========================#

# arr=[1,2,3,4,5,6,7,8]
# target=8


def target_1(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1

arr=[1,2,3,4,5,6,7,8]
target=7
print(target_1(arr,target))