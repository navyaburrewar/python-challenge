## Write a generator function that yields numbers in reverse order from n to 1.

def function(m):
    for i in range(m+1,1,-1):
    
        
        yield i
for a in function(20):
    print(a)        

