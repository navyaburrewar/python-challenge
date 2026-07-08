def count_sort(arr):
    max_value=max(item[1]for item in arr)
    
    count=[0]*(max_value+1)
    
    for item in arr:
        count[item[1]]+=1
        
    for i in range(1,len(count)):
        count[i]+=count[i-1]
        
    output=[0]*len(arr)
    
    for i in range(len(arr)-1,-1,-1):
        item=arr[i]
        key=item[1]
        output[count[key]-1]=item
        count[key]-=1
    return output
print(count_sort( [
    ("Amit", 2),
    ("Rahul", 6),
    ("Priya", 3),
    ("John", 6),
    ("Sara", 1),
    ("Tom", 2)
]))