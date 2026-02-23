## count occurence

from array import array 
arr=array('i',[6,9,4,3,6,45])
num=6
count=0

for i in arr:
    if i==num:
        count+=1
print(count)    