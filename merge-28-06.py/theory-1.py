# 1. What is Merge Sort?

# Merge Sort is a sorting algorithm that sorts an array by repeatedly dividing it into smaller parts, sorting those parts, and then merging them back together in sorted order.

# It follows the Divide and Conquer strategy.



###### 2. Why is Merge Sort called a Divide and Conquer algorithm?  ##################

# Merge Sort works in three steps:

# Divide: Split the array into two equal halves.
# Conquer: Recursively sort each half.
# Combine: Merge the two sorted halves into one sorted array.



# # 3. Explain Merge Sort using an example
# Array = [4, 2, 7, 1]

# Step 1:
# Split

# [4,2,7,1]

# ↓

# [4,2]   [7,1]

# ↓

# [4] [2] [7] [1]

# Step 2:
# Merge

# [4] + [2]
# ↓

# [2,4]

# [7] + [1]
# ↓

# [1,7]

# Step 3:
# Final Merge

# [2,4] + [1,7]

# ↓

# [1,2,4,7]


# 6. Time Complexity
# Case	Time Complexity
# Best Case	O(n log n)
# Average Case	O(n log n)
# Worst Case	O(n log n)


# Reason: The array is divided into log n levels, and merging at each level takes O(n) time.

# 7. Space Complexity

# Merge Sort requires extra memory for temporary arrays during merging
# O(n)


# Why is Merge Sort Stable?
# A sorting algorithm is stable if it preserves the relative order of equal elements.

# During merging, if two elements are equal, Merge Sort takes the element from the left subarray first.


# 9. Can Merge Sort be done in-place?

# Standard Merge Sort is not in-place because it requires additional temporary arrays while merging.

# Standard Merge Sort: No
# Advanced in-place versions exist but are much more complex and less commonly used.


