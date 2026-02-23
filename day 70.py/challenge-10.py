## linear search
from array import array

arr=array('i',[2,4,6,8,9,12,34])

k=4
for i in range(len(arr)):
    if arr[i]==k:
        print(k)
        break
