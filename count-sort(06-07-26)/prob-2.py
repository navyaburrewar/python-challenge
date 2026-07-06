# Input
# arr = [4, 2, 2, 8, 3, 3, 1]

# Expected Output

# [1, 2, 2, 3, 3, 4, 8]


def counting_sort(arr):
    max_value=max(arr)  ## finding the max element

    count=[0]*(max_value+1)   # creating a count array

    for num in arr:
        count[num]+=1

    j=0
    for i in range(len(count)):
        while count[i]>0:
            arr[j]=i
            j+=1
            count[i]-=1
+
    return arr
a=[4, 2, 2, 8, 3, 3, 1]
print(counting_sort(a))            

