"""
9. Find kth Smallest Element

Using Selection Sort logic, find the 3rd smallest element.

arr = [7, 10, 4, 3, 20, 15]

Expected Output:

7

Because sorted array becomes:

[3, 4, 7, 10, 15, 20]
"""





def sorted_1(arr,):
    
    for i in range(len(arr)):
        min_idex=i
        for j in range(i+1,len(arr)):
            if arr[min_idex]>arr[j]:
                min_idex=j

        arr[i],arr[min_idex]=arr[min_idex],arr[i]
    return arr
sorted_array=sorted_1( [7, 10, 4, 3, 20, 15])
k=int(input())
for i in range(len(sorted_array)):
    
    if i==(k-1):
        print(sorted_array[i])



















"""
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