#  heap queue is an priority queue

# Priority- process the element according to its priority
#Heap - a data structure commonly used to implement a priority queue efficient


# heap---

import heapq
a=[]
heapq.heappush(a,8)
heapq.heappush(a,4)
heapq.heappush(a,0)
heapq.heappush(a,6)

print(a)
print(a[0])


## parent <=child nodes

### hea[ifying an num a list of numbers]

import heapq
num=[10,3,9,40,8]
heapq.heapify(num)
print(num)



### min heap 
import heapq
num=[10,4,7,9,34,6]
heapq.heapify(num)
print(num)




## max heap 
import heapq
m=[]

num=[10,3,6,9,5]

for i in num:
    heapq.heappush(m,-i)
while m:
    print(-heapq.heappop(m))

  
##3 last 3 largest numbers

import heapq
num=[10,30,59,50,39]

res=heapq.nlargest(3,num)
print(res)


#  n number smallest elements

import heapq
num=[20,39,58,10,84]

m=heapq.nsmallest(3,num)

print(m)



import heapq
num=list(map(int,input().split()))
k=int(input())

heap=[]
for i in num:
    heapq.heappush(heap,-i)

    if len(heap)>k:
        heapq.heappop(heap)

print("k th samllest",-heap[0])        


## all about are heap sort examples