
#  Types of Two Pointer Techniques

# 1. Opposite Direction Pointers
# 2. Same Direction Pointers (Fast and Slow Pointers)
# 3. Sliding Window (Dynamic Window)
# 4. Fast and Slow Pointer in Linked Lists



# 1. Opposite Direction Pointers

"""
Pointers start from both ends and move toward each other.

1 2 3 4 5 6
^         ^
L         R

Used in:

Pair sum in sorted array
Palindrome
Reverse array
"""

"""
arr=[1,2,3,4,5]
left=0
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]

    left+=1
    right-=1
print(arr)    
"""



# 2. Same Direction Pointers (Fast and Slow Pointers)

# Both pointers move in the same direction.

# 1 2 3 4 5
# ^ ^
# s f

# Used in:

# Remove duplicates
# Move zeros
# Linked list cycle detection

# Example: Remove duplicates from sorted array.
"""
nums=[1,1,2,2,3,3,4,4,5,5]
slow=0
for fast in range(1,len(nums)):
    if nums[fast]!=nums[slow]:
        slow+=1
        nums[slow]=nums[fast]
print(nums[:slow+1])        
"""



# 3. Sliding Window (Dynamic Window)

# Two pointers define a window.

# 1 2 3 4 5 6
#   ^-----^
#  left   right

# Used for:

# Longest substring
# Maximum sum subarray
# Minimum window substring


