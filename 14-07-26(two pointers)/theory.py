# Two Pointers Technique in Python
# The Two Pointers technique is a problem-solving approach where we use two variables (pointers or indices) to traverse a data structure, usually an array or string, instead of using nested loops.
# It is mainly used to reduce time complexity, often changing an O(n²) solution into an O(n) solution.



"""
Basic Idea of Two Pointers

Instead of scanning the array multiple times, we maintain two indices and move them according to certain conditions.

Array: [1, 2, 3, 4, 5]

left = 0
right = 4

1  2  3  4  5
^           ^
left      right

Depending on the problem:

Move left forward (left += 1)
Move right backward (right -= 1)
Move both pointers
"""




"""
Why Do We Use Two Pointers?
1. Reduce Time Complexity
Brute Force Approach

Finding a pair with sum = target:

arr = [1, 2, 3, 4, 5]
target = 6

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])

Time Complexity:

O(n²)
  
"""  


# Two Pointer Approach
"""
arr=[1,2,3,4,5]
target=6
left=0
right=len(arr)-1

while left<right:
    current_sum =arr[left]+arr[right]

    if current_sum==target:
        print(arr[left],arr[right])
        break
    elif current_sum<target:
        left+=1
    else:
        right-=1


        # time complexity 0(n)
"""




"""
2. Saves Extra Memory

Many two-pointer solutions use:

Space Complexity = O(1)

because only two variables are used.
"""



# When Should We Use Two Pointers?

# 1. Problem involves arrays or strings.

"""
Examples:

Find pairs
Remove duplicates
Reverse array/string
Palindrome checking
"""



"""
2. Input is sorted.

This is one of the biggest hints.

Example keywords:

"sorted array"
"sorted list"
"ascending order"
"""


"""
3. Need to find pairs or triplets.

Examples:

Pair sum
Three sum
Four sum
"""



"""
4. Need to compare elements from both ends.

Examples:

Palindrome checking
Reversing an array
"""


"""
5. Need to process a continuous subarray/window.

This leads to the sliding window, which is a variation of two pointers.
"""

## contineouation
