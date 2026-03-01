# 1️⃣ Factorial of a number

def factorial(m):
    if m==0:
        return 1
    else :
        return m*factorial(m-1)
print(factorial(5))    
    


## using lambda

factorial2 = lambda n : 1 if n==0 else n*factorial2(n-1)
print(factorial2(3))
