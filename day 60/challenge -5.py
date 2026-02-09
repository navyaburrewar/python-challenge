## Write a function that checks whether a number is prime.

def prime(m):
    if m<=1:
        return False
    for i in range(2,m):
        if m%i==0:
            return False
        
    return True
print(prime(2))    
    


