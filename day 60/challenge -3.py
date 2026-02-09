## Write a function that returns the factorial of a number.


# def factorial(n):
#     if n<0:
#        return "factorial not defined for negative"
#     fact=1
#     for i in range(1,n+1):
#        fact*=i
       
#     return fact       

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        
    return fact

print(factorial(5))