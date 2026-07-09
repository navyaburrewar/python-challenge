# # Example 1:

# # Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# # Output: [2,2,2,1,4,3,3,9,6,7,19]
# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         max_value=max(arr1)
#         count=[0]*(max_value+1)

#         for i in arr1:
#             count[i]+=1   #frequences []

#         j=0
#         for i in arr2:
#             while count[i]>0:
#                 arr1[j]=i
#                 j+=1
#                 count[i]-=1
        
#         for i in range(len(count)):
#             while count[i]>0:
#                 arr1[j]=i
#                 j+=1
#                 count[i]-=1
                        
#         return arr1   