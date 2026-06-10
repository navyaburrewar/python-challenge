# 8. Selection Sort Without Using Python Swapping Shortcut

# Do not use:

# a, b = b, a

# Use temporary variable instead.


def function_1(arr):
    
    for i in range(len(arr)):
       
        min_index=i
        for j in range(i+1,len(arr)):
            
            if arr[min_index]>arr[j]:
                min_index=j
        temp=arr[i]            # save original value
        arr[i]=arr[min_index]   # overwrite with smaller value
        arr[min_index]=temp   # restore  saved value

    return arr
print(function_1([2,1,8,4,5]))    











