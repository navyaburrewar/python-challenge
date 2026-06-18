# 6. Insertion Sort on Strings

# Sort an array of strings alphabetically using Insertion Sort.

# Input:

# ["banana", "apple", "mango", "grape"]

# Output:

# ["apple", "banana", "grape", "mango"]

def funct(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print(funct(["banana", "apple", "mango", "grape"]))            