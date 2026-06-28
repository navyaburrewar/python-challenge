# 3. Count number of merge operations

#  Sort an array in descending order using Merge Sort

merge_count=0
def merge_sort(arr):
    global merge_count
    n=len(arr)
    l=0
    r=n-1
    if n>1:
        mid=(l+r)//2
        left=arr[:mid+1]
        right=arr[mid+1:]
        merge_sort(left)
        merge_sort(right)
        merge_count+=1
        i=j=k=0
       
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=right[j]
                j+=1
            else:
                arr[k]=left[i]
                i+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
            
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
            
arr=[0,4,8,2,1]
merge_sort(arr)
print(merge_count)        
