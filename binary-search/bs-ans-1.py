# # # arr=[1,2,3,4,5]
# # # 🍌 Koko Eating Bananas — Question

# # You are given an array:

# # piles = [3, 6, 7, 11, 6]

# # Each element represents:

# # number of bananas in one pile.

# # So:

# # pile 1 has 3 bananas
# # pile 2 has 6 bananas
# # pile 3 has 7 bananas
# # pile 4 has 11 bananas
# # pile 5 has 6 bananas

# # Koko can eat bananas at a speed of:

# # k bananas per hour

# # Important rule:

# # In one hour, Koko chooses ONLY ONE pile.
# # She eats up to k bananas from that pile.
# # If the pile has fewer than k bananas, she finishes the entire pile in that hour.

# # You are also given:

# # h = 8

# # which means:

# # Koko has only 8 hours to finish ALL piles.
# # Task

# # Find the:

# # minimum eating speed k

# # such that:

# # Koko can finish all bananas within h hours.
# import math

# def eating(piles,h,s):
#     total_hours=0
#     for bananas in piles:
#         hour=math.ceil(bananas/s)
#         total_hours+=hour

#     return total_hours<=h
   
# def function(piles,h):
#     low=1
#     high=max(piles)
#     ans=high 
#     while low<=high:
#         mid=(low+high)//2
#         if eating(piles,h,mid):
#             ans=mid    
#             high=mid-1
#         else:
#             low=mid+1

#     return ans                
# piles=[1,2,3,4,5]
# h=8
# print(function(piles,h))





def can_place(stalls, k, distance):

    count = 1

    last_position = stalls[0]

    for i in range(1, len(stalls)):

        if stalls[i] - last_position >= distance:

            count += 1

            last_position = stalls[i]

    return count >= k


def aggressive_cows(stalls, k):    

    stalls.sort()            

    low = 1                  

    high = stalls[-1] - stalls[0]  

    answer = 0

    while low <= high:      

        mid = (low + high) // 2      

        if can_place(stalls, k, mid):     

            answer = mid

            low = mid + 1

        else:

            high = mid - 1

    return answer


stalls = [1,2,4,8,9,7,4]
k = 3

print(aggressive_cows(stalls, k))