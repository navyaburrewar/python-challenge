 #############   coping araay two types shallow and deep copy by view() & #copy()########33333333333


## shallow

from numpy import *
arr1=array([3,5,8,9])
arr2=arr1.view()

arr1[1]=3
print(arr1)
print(arr2)