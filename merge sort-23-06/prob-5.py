# 5. Sort Array in Descending Order

# Modify Merge Sort to sort in decreasing order.

def mergr_sotr(arr):
    n=len(arr)
    l=0
    r=n-1
    if n>1:
        mid=(l+r)//2
        left=arr[:mid+1]
        right=arr[mid+1:]
        mergr_sotr(left)
        mergr_sotr(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]>right[j]:
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

a=[2,4,1,5,9]
print(mergr_sotr(a))
                


