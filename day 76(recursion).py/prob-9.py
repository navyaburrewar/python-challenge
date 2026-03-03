
##  Write a generator function that yields numbers from 1 to 20.
def function(m):
    for i in range(1,m+1):
     yield i
function(5)
for i in function(5):
   print(i)     




