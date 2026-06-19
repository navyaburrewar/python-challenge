# ##########1. What is Insertion Sort?##############
# Interview-Level Answer

# Insertion Sort is a simple comparison-based sorting algorithm that builds the final sorted array one element at a time. It works by taking each element from the unsorted portion and inserting it into its correct position in the already sorted portion of the array.

# Example:

# Array: [5, 2, 4, 6]

# Pass 1: [2, 5, 4, 6]
# Pass 2: [2, 4, 5, 6]
# Pass 3: [2, 4, 5, 6]





# ======= 2. Why is it called "Insertion" Sort?====#
# Interview-Level Answer

# It is called Insertion Sort because during each iteration, one element is picked from the unsorted part and inserted into its correct position in the sorted part of the array.

# It is similar to how people sort playing cards in their hands:

# Pick one card
# Insert it into the correct position among already sorted cards







#========   3. How does it work?  =========#
# Interview-Level Answer

# Insertion Sort divides the array into two parts:

# A sorted portion on the left.
# An unsorted portion on the right.

# Starting from the second element, it compares the current element with elements before it and shifts larger elements one position to the right until the correct position is found. Then the element is inserted there.

# Steps
# Assume first element is already sorted.
# Take next element.
# Compare with previous elements.
# Shift larger elements to the right.
# Insert element at correct position.
# Repeat until array is sorted.



#========== 4. Best Time Complexity? ======#
# Interview-Level Answer

# The best-case time complexity is O(n).

# Why?

# When the array is already sorted:

# [1, 2, 3, 4, 5]

# Each element requires only one comparison and no shifting.

# Best Case: O(n)






#=========== 5. Average Time Complexity? ==========#
# Interview-Level Answer

# The average-case time complexity is O(n²).

# Why?

# For a randomly ordered array, each element may need to be compared and shifted approximately half of the sorted portion.

# Average Case: O(n²)







#=============== 6. Worst Time Complexity? ======================
# Interview-Level Answer

# The worst-case time complexity is O(n²).

# Why?

# When the array is sorted in reverse order:

# [5, 4, 3, 2, 1]

# Every new element must be compared with all previous elements and shifted.

# Number of operations:

# 1 + 2 + 3 + ... + (n-1)
# = n(n-1)/2
# = O(n²)

# Worst Case: O(n²)




# =========== 7. Space Complexity? ==============#

# Interview-Level Answer

# The space complexity of Insertion Sort is O(1) because it sorts the array in place and requires only a few extra variables.

# Space Complexity: O(1)



# # =========== 8. Is Insertion Sort Stable ================#
# Interview-Level Answer

# Yes, Insertion Sort is a stable sorting algorithm.

# Interview-Level Answer

# Yes, Insertion Sort is a stable sorting algorithm.


# What does stable mean?

# If two elements have the same value, their relative order remains unchanged after sorting.

# Example
# (5,A) (3,B) (5,C)

# After sorting:
# (3,B) (5,A) (5,C)



# 9. Is Insertion Sort In-Place?
# Interview-Level Answer

# Yes, Insertion Sort is an in-place sorting algorithm because it does not require any significant extra memory apart from a few temporary variables.

# In-place: ✅ Yes

# Extra Space: O(1)

# 1. Small Arrays

# For small inputs (typically < 20–50 elements), Insertion Sort is often faster.

# 2. Nearly Sorted Data

# If the array is almost sorted:

# [1, 2, 3, 5, 4]

# Insertion Sort runs close to O(n).

# 3. Online Sorting

# When elements arrive one by one and need to be kept sorted.

# 4. Hybrid Algorithms

# Many advanced sorting algorithms use Insertion Sort internally for small subarrays.
