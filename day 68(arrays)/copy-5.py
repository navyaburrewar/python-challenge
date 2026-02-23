from numpy import*

arr1= array([1,2,3,4,5])
arr2 =arr1.copy()


arr1[1]=3
print(arr1)
print(arr2)


print(id(arr1))
print(id(arr2))    


### here about the the modification is done only in the arr1 which called deep copy

