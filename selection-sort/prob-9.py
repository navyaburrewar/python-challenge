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



















