# 3. Count Shifts

# Implement Insertion Sort and return the total number of shifts performed.

# Input:

# [2, 1, 3, 1, 2]

# Output:

# 4

def funct(arr):
    count=0
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        count+=1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        
    return count
print(funct([2, 1, 3, 1, 2]))        