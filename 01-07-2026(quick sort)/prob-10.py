
# Count the number of swaps performed.
count=0
def quick_sort(arr,low,high):
    global count
    i=low-1
    pivot=arr[high]
   
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
            count+=1
    if i+1!=high:        
        arr[i+1],arr[high]=arr[high],arr[i+1]
        count+=1
    return i+1
    
def sort(arr,low,high):
    
    if low<high:  

        pi=quick_sort(arr,low,high)

        sort(arr,low,pi-1)
        sort(arr,pi+1,high)

        

arr=[2,4,15,7,9]
sort(arr,0,len(arr)-1)
print(arr,count)


