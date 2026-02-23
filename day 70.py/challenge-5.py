## length without len()


from array import array

arr=array('i',[2,3,6,8,9])

count=0
for i in arr:
    count+=1
print("length:",count)