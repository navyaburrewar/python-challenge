# 3. Implement Recursive Merge Sort

# Sort an unsorted array using Merge Sort.

# Example:

# [5,2,8,1,9]
# → [1,2,5,8,9]


def merge_sort(arr):
    n=len(arr)
    l=0
    r=n-1
    if n>1:
        mid=(l+r)//2
        left=arr[:mid+1]
        right=arr[mid+1:]
        merge_sort(left)
        merge_sort(right)

        i=j=k=0
        while i<len(left)  and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]    
            j+=1
            k+=1
    return arr

a=[5,2,8,1,9]
print(merge_sort(a))        
