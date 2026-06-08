## prob--10
def findPeakElement(nums):
    low=0
    high=len(nums)-1
    while low <high:
        mid=(low+high)//2
        if nums[mid+1]>nums[mid]:
            low=mid+1
        else:
            high=mid
    return low  
    
print(findPeakElement([1,2,3,4,5,6,5]))    
  
            
            
        
        
