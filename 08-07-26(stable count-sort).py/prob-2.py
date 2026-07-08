# Beginner Level
# 1. Perform Stable Counting Sort Manually

# Apply stable counting sort on:

# A = [4, 2, 2, 8, 3, 3, 1]

# Find:

# Frequency array
# Cumulative count array
# Output array after placing each element
# Final sorted array

def count_sort(arr):
    max_value=max(arr)

    count=[0]*(max_value+1)

    for num in arr:
        count[num]+=1
    print("Frequency array",count)    

    for i in range(1,len(count)):
        count[i]+=count[i-1]
    print("cumulative count array::",count)

    output=[0]*len(arr)

    for i in range(len(arr)-1,-1,-1):
        num=arr[i]
        output[count[num]-1]=num
        count[num]-=1
        print(i,output)
    return output
print(count_sort([4, 2, 2, 8, 3, 3, 1]))            

