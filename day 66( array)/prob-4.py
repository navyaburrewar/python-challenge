## accessing index of element using the genereal method

from array import *
arr =array('i', [1,2,3,4,5,6])
k=0

n =int(input())
for value in arr:
    if value==n:
        print(k)
    k+=1

