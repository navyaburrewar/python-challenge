## reversing array

from array import array

arr=array('i',[2,3,6,8,9])

arr.reverse()
print(arr)




## problem-2

arr=array('i',[2,5,8,3,6,9])

start =0
end=len(arr)-1

while start <end:
    arr[start],arr[end]=arr[end],arr[start]

    start+=1
    end-=1
print(arr)    