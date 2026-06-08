# Here are the best case, average case, and worst case time complexities for Linear Search, Binary Search, and Bubble Sort:

# Algorithm	Best Case	Average Case	Worst Case
# Linear Search	O(1)	O(n)	        O(n)
# Binary Search	O(1)	O(log n)        O(log n)
# Bubble Sort	O(n)	O(n²)	        O(n²)
                         

# Explanation
# 1. Linear Search
# Checks elements one by one.
# Best Case: Element found at the first position → O(1)
# Average Case: Element found in the middle → O(n)
# Worst Case: Element at last position or not present → O(n)


# 2. Binary Search
# Works only on sorted arrays.
# Repeatedly divides the search space into half.
# Best Case: Middle element is the target → O(1)
# Average/Worst Case: Keeps dividing array → O(log n)


# 3. Bubble Sort
# Repeatedly swaps adjacent elements if they are in the wrong order.
# Best Case: Array already sorted (with optimized bubble sort) → O(n)
# Average Case: Random order → O(n²)
# Worst Case: Reverse sorted array → O(n²)