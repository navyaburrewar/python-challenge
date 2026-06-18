# 2. Sort in Descending Order

# Modify Insertion Sort to sort the array in descending order.

# Input:

# [5, 2, 4, 6, 1, 3]

# Output:

# [6, 5, 4, 3, 2, 1]


def funct(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]<key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print(funct([5, 2, 4, 6, 1, 3]))            