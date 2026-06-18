# 4. Count Comparisons

# Write a program that counts the number of comparisons made during Insertion Sort.

# Input:

# [5, 4, 3, 2, 1]

# Output:

# 10


def funct(arr):
    count=0
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            count+=1
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return count
print(funct([5, 4, 3, 2, 1]))            