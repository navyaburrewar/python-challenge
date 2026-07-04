# 1. Lomuto Partition

# Input

# [9,4,8,3,1,2,5]

# Expected Output

# Partition Index:
# 4

# Array:
# [4,3,1,2,5,8,9]



def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
arr=[7,1,4,8,3,2]
partition(arr,0,len(arr)-1)
print(arr) 





