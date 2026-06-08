# Before Bubble Sort — Important Idea


# Most sorting algorithms work using:

# comparisons
# swapping


#========== Bubble Sort Algorithm===========#
"""
For every pass:

compare neighboring elements
swap if needed
largest unsorted element moves to the end

Repeat until sorted.
"""


## prob-1

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr
print(bubble_sort([2,3,4,5,6,1]))            