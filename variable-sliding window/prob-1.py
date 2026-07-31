# Given an array of positive integers nums and an integer k, find the length of the longest contiguous subarray whose sum is less than or equal to k.

def logest_subarray_sum(nums,k):
    left=0
    total=0
    max_len=0
    for right in range(len(nums)):
        total+=nums[right]

        while total>k:
            total-=nums[left]
            left+=1

        max_len=max(max_len,right-left+1)

    return max_len        

print(logest_subarray_sum([2,3,1,2,4,3],7))

    