# 7. Sort Strings Using Selection Sort

# Sort list of strings alphabetically.

# arr = ["banana", "apple", "grape", "cherry"]

# Expected Output:

# ['apple', 'banana', 'cherry', 'grape']

def selection_sort(arr):
    
    for i in range(len(arr)):
        min_inde=i
        for j in range(i+1,len(arr)):
            
            if arr[j]<arr[min_inde]:
                
                min_inde=j
        arr[i],arr[min_inde]=arr[min_inde],arr[i]

    return  arr
print(selection_sort(["banana", "apple", "grape", "cherry"]))  














"""







































8. Selection Sort Without Using Python Swapping Shortcut

Do not use:

a, b = b, a

Use temporary variable instead.

9. Find kth Smallest Element

Using Selection Sort logic, find the 3rd smallest element.

arr = [7, 10, 4, 3, 20, 15]

Expected Output:

7

Because sorted array becomes:

[3, 4, 7, 10, 15, 20]
10. Sort List of Tuples

Sort tuples based on first element using Selection Sort.

arr = [(3, 'c'), (1, 'a'), (2, 'b')]

Expected Output:

[(1, 'a'), (2, 'b'), (3, 'c')]
Bonus Challenge Problems

If you finish all 10:

Bonus 1

Optimize Selection Sort to avoid unnecessary swaps.

Bonus 2

Implement Selection Sort recursively.

Bonus 3

Visualize Selection Sort step-by-step using prints.

Example:

After Pass 1: [11, 25, 12, 22, 64]
After Pass 2: [11, 12, 25, 22, 64]
Recommended Order

Solve in this order:

1 → 2 → 3 → 4 → 5 → 6 → 8 → 7 → 9 → 10
Important Concepts These Problems Cover
Problem	Concept
1	Basic sorting
2	Descending sort
3	Swaps
4	Comparisons
5	User input
6	Dry run understanding
7	String sorting
8	Manual swapping
9	Logic application
10	Custom sorting

After you solve them, I can also give:

Beginner → Advanced Selection Sort problems
Interview questions
Dry run exercises
MCQs
Debugging problems
Time complexity questions
Pattern-based sorting questions
LeetCode-style questions       
"""