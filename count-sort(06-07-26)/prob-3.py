## count probleem

# input=[2,4,6,3,9,2]
# output =[2,2,3,4,6,9]

def count_sort(arr):
    max_value=max(arr)

    count=[0]*(max_value+1)

    for num in arr:
        count[num]+=1
    
    j=0
    for i in range(len(count)):
        while count[i]>0:
            arr[j]=i
            j+=1
            count[i]-=1

    return arr
arr=[2,4,6,3,9,2]
print(count_sort(arr))

        







