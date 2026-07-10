# 2. Construct the Count Array

# Given:

# A = [5, 1, 4, 2, 1, 3]

# Create:

# Frequency count array
# Prefix sum array

# Do not perform the final placement step.


def count_array(arr):
    max_value=max(arr)

    count=[0]*(max_value+1)

    for num in arr:
        count[num]+=1
    print(count)    

    for i in range(1,len(count)):
        count[i]+=count[i-1]  
    print("prefix sum",count)    


    return count
print(count_array([9,5,2,3,7,1,5]))

