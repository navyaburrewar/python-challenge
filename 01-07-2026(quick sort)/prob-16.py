# 2. Hoare Partition

# Input

# [9,4,8,3,1,2,5]
# Expected Output
# Partitioned Array
# (Pivot position depends on implementation.)


def hoare_partition(arr,low,high):
    pivot=arr[low]
    i=low+1
    j=high

    while True:
        while i<=high and arr[i]<pivot:
            i+=1
        while j>=low and arr[j]>pivot:
            j-=1    
        if i>=j:
            break
        arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j        

arr=[9,4,8,3,1,2,5]
print(hoare_partition(arr,0,len(arr)-1))

