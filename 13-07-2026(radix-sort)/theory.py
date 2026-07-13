# Why Do We Need Different Sorting Algorithms?

# Imagine you want to travel.

# For short distances, walking is fine.
# For medium distances, a bike is better.
# For long distances, an airplane is better.

# Similarly, no single sorting algorithm is best for every situation.

# Algorithm	Average Time Complexity
# Bubble Sort	O(n²)
# Selection Sort	O(n²)
# Insertion Sort	O(n²)
# Merge Sort	O(n log n)
# Quick Sort	O(n log n)
# Radix Sort	O(d × (n + k))

# Different algorithms perform better for different types of data.


# The Main Idea Behind Radix Sort

# Most sorting algorithms compare elements with each other.

# For example:

# 45 > 24
# 75 > 45
# 90 > 75

# They keep comparing numbers until everything is sorted.

# Radix Sort works differently.

# It does not compare numbers directly.
# Instead, it sorts numbers digit by digit.
# This is why Radix Sort is called a Non-Comparison Sorting Algorithm.


# Meaning of the Word "Radix"

# The word Radix means:

# Base of a number system.

# Examples:

# Decimal numbers use base 10.
# Binary numbers use base 2.
# Hexadecimal numbers use base 16.

# Since computers usually store decimal integers as digits from 0-9, Radix Sort processes digits from 0 to 9.



# Visual Representation

# Original:
# 170 45 75 90 802 24 2 66

# After one's digit sort:
# 170 90 802 2 24 45 75 66

# After ten's digit sort:
# 802 2 24 45 66 170 75 90

# After hundred's digit sort:
# 2 24 45 66 75 90 170 802



# What is the Need for Radix Sort?

# This is the most important question.

# Traditional sorting algorithms use comparisons

# For n elements:

# Theoretical lower bound:

# O(n log n)




# Radix Sort avoids comparisons

# Because it sorts digits instead of comparing values, it can achieve nearly linear performance.

# Its complexity is:

# O(d × (n + k))

# where:

# n = number of elements
# d = number of digits in the largest number
# k = range of digits (0-9, so k = 10)

# If d and k are small constants:
# O(n)

# This is faster than:
# O(n log n)

# Where Is Radix Sort Used?

# Radix Sort is useful for:

# Sorting employee IDs
# Sorting roll numbers
# Sorting phone numbers
# Sorting zip codes
# Sorting account numbers
# Sorting integers in databases
# Large datasets containing fixed-length numbers


# Example

# Suppose a university wants to sort:

# 20240015
# 20240001
# 20240010
# 20240005

# Since all values have the same number of digits, Radix Sort works extremely well.