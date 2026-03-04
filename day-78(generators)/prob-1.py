##  Write a generator function that yields numbers from 1 to 20.
def function(m):
    for i in range(1,m+1):
     yield i
for i in function(20):
   print(i)     

