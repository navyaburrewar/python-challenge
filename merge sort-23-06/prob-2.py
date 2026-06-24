# Level 1: Understand Merge Sort Basics
# 1. Merge Two Sorted Arrays

# Given two sorted arrays, merge them into a single sorted array.

# Example:

# A = [1,3,5]
# B = [2,4,6]

# Output:
# [1,2,3,4,5,6]



def merge_sort(A,B,arr):
    
    
    i=j=k=0
    while i<len(A) and j <len(B):
        if A[i]<B[j]:
            arr[k]=A[i]
            i+=1
        else:
            arr[k]=B[j]
            j+=1
        k+=1

    while i<len(A):
        arr[k]=A[i]
        i+=1
        k+=1
    while j<len(B):
        arr[k]=B[j]
        j+=1
        k+=1

    return arr
A=[1,3,5]
B=[2,4,6]
arr=A+B
print(merge_sort(A,B,arr))

    