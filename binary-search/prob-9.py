# # Search in rotated sorted array (no duplicates)
# arr=[3,4,5,1,2]
# target=5

def rotated(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        if arr[low]<=arr[mid]:
            if arr[low]<=target<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<target<=arr[high]:
                low=mid+1
            else:
                high=mid-1
print(rotated([3,4,5,1,2],3))   
print(rotated([3,4,5,1,2],2)) 
print(rotated([3,4,5,1,2],5))          

                            
            

            
            

               


