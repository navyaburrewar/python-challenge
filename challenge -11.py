## another method


from array import array

arr=array('i',[2,3,6,8,9])

max_val=arr[0]
min_val=arr[0]

for i in arr:
    if i>max_val:
        max_val = i
    if i < min_val:
        min_val = i

print("max:", max_val)
print("min :",min_val)      

