# Level 1: Understanding Quick Sort
# Question 1: Dry Run Quick Sort (Must Do)

# Problem

# Given

# [7, 2, 1, 6, 8, 5, 3, 4]

# Use the last element as pivot.

# Show every partition step until the array becomes sorted.

# What interviewer checks
# Can you manually execute Quick Sort?
# Do you understand partition?



[7, 2, 1, 6, 8, 5, 3, 4]
pivot=4

left=[2,1,3]
middle=[4]
right=[7,6,8,5]


# now recursively sort left array

[2,1,3]
pivot=3

left=[2,1]
pivot=3
right=[]


## sort [2,1]

[2,1]
pivot=1

left=[]
pivot=[1]
right=[2]

# so left side array

[1,2,3]



### recursively sort on right parts of array
[7,6,8,5]
pivot=5

left=[]
middle=[5]
right=[7,6,8]


#final sorted array
[1,2,3]+[4]+[5,6,7,8]
[1,2,3,4,5,6,7,8]