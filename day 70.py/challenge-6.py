## sum of elements

from array import array

arr=array('i',[2,3,6,8,9])
sum=0
for i in arr:
    sum=sum+i
    i+=1
print(sum)
