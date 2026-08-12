# what is the heap sort?

"""
1. What is Heap Sort?

Heap Sort is a comparison-based sorting algorithm that uses a special binary tree structure called a Heap.

It sorts an array by:

Converting the array into a heap.
Taking the largest/smallest element from the heap.
Moving that element to its correct position.
Rebuilding/adjusting the heap.
Repeating until the array is sorted.

For ascending order, we normally use a Max Heap.

For descending order, we normally use a Min Heap.
"""



"""
2. Why do we need Heap Sort?

Suppose you have:

[10, 5, 20, 2, 8, 15]

You want:

[2, 5, 8, 10, 15, 20]

There are many sorting algorithms:

Bubble Sort
Selection Sort
Insertion Sort
Merge Sort
Quick Sort
Heap Sort

The question is:

Why use Heap Sort when we already have other sorting algorithms?

The main reason is its combination of:

O(n log n) worst-case time
O(1) auxiliary space when implemented in-place
No need for recursion
Predictable performance

So Heap Sort is particularly useful when you want guaranteed O(n log n) time without allocating another array.
"""



"""
3. What is a Binary Tree?

Before understanding Heap, understand a binary tree.

A binary tree is a tree where each node has at most two children.

Example:

        10
       /  \
      5    20
     / \   /
    2   8 15

Each node can have:

left child
right child
"""



"""
4. What is a Complete Binary Tree?

A Heap is based on a Complete Binary Tree.

A complete binary tree has these properties:

Every level is completely filled except possibly the last.
The last level is filled from left to right.

Example:

        10
       /  \
      5    20
     / \  /
    2   8 15

This is complete.

But:

        10
       /  \
      5    20
       \     \
        8     15

is not complete because nodes aren't filled from left to right.
"""

"""
5. What is a Heap?

A Heap is a complete binary tree that satisfies a special ordering property.

There are two major types:

Max Heap

Parent is greater than or equal to its children.

        50
       /  \
      30   40
     / \   /
    10 20 35

Here:

50 > 30
50 > 40
30 > 10
30 > 20
40 > 35

Therefore, it is a Max Heap.

The largest element is always at the root.

Min Heap

Parent is smaller than or equal to its children.

        10
       /  \
      20   15
     / \   /
    30 40 25

The smallest element is always at the root.
"""

