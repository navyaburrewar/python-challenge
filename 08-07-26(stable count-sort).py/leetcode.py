# # ## hight checker
# # Input: heights = [1,1,4,2,1,3]
# # Output: 3
# # Explanation: 
# # heights:  [1,1,4,2,1,3]
# # expected: [1,1,1,2,3,4]
# # Indices 2, 4, and 5 do not match.

# class Solution:
#     def heightChecker(self, heights: List[int]) -> int:
#         arr=heights.copy()
#         max_value=max(arr)

#         count=[0]*(max_value+1)

#         for num in arr:
#             count[num]+=1

#         j=0
#         for i in range(len(count)):
#             while count[i]>0:
#                 arr[j]=i
#                 j+=1
#                 count[i]-=1
#         box=0
#         for i in range(len(arr)):
#             if arr[i]!=heights[i]:
#                 box+=1
#         return box            
