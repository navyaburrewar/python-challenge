# 1. Maximum Sum Subarray of Size K
# Problem

# Given an array and an integer k, find the maximum sum of any contiguous subarray of size k.

# Example
# Input:
# arr = [2, 1, 5, 1, 3, 2]
# k = 3

# Output:
# 9

# Explanation:
# [5,1,3] = 9



def max_sum_subarray(nums,k):
    window_sum=sum(nums[:k])
    max_sum=window_sum

    for i in range(k,len(nums)):
        window_sum+=nums[i]-nums[i-k]

        max_sum=max(max_sum,window_sum)

    return max_sum

nums=[2, 1, 5, 1, 3, 2]
print(max_sum_subarray(nums,3))





     
