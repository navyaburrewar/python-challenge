# 7. Sort Strings Using Selection Sort

# Sort list of strings alphabetically.

# arr = ["banana", "apple", "grape", "cherry"]

# Expected Output:

# ['apple', 'banana', 'cherry', 'grape']

def selection_sort(arr):
    
    for i in range(len(arr)):
        min_inde=i
        for j in range(i+1,len(arr)):
            
            if arr[j]<arr[min_inde]:
                
                min_inde=j
        arr[i],arr[min_inde]=arr[min_inde],arr[i]

    return  arr
print(selection_sort(["banana", "apple", "grape", "cherry"]))  

