# 10. Dry Run

# Input

# [8,3,1,7,0,10,2]

# Expected Output

# Final Sorted Array:
# [0,1,2,3,7,8,10]

[8,3,1,7,0,10,2]

[1,0,2,8,3,7,10,]

left=[1,0]
middle=[2]
right=[8,3,7,10]


# left half
[1,0]
pivot=[0]
left=[]
right=[1]


# right half
[8,3,7,10]
pivot=[10]

left=[8,3,7]
right=[]

[3,7,8]
pivot=[8]
left=[3,7]
right=[]

[3,7]
pivot=[7]
left=[3]

