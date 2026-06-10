"""
10. Sort List of Tuples

Sort tuples based on first element using Selection Sort.

arr = [(3, 'c'), (1, 'a'), (2, 'b')]

Expected Output:

[(1, 'a'), (2, 'b'), (3, 'c')]

"""



def sort_tuple(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]        
    return arr
print(sort_tuple([(3, 'c'), (1, 'a'), (2, 'b')]))







