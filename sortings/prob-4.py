# Use Bubble Sort logic to determine whether an array is already sorted.

# Example:

# Input: [1, 2, 3, 4]
# Output: Already Sorted

def al_sorted(arr):
    sort_arr=arr
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr
al_sorted([1,2,3,4])

if sort_arr==arr:    
    print("Already Sorted")
else:
        print(al_sorted([1,2,3,4]))            

                       
