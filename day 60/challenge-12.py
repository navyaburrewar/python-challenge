##    Write a function that returns the Fibonacci sequence up to n terms.

def fibonacci(n):
    a=0
    b=1
    for i in range(n):
       print(a,end=" ")
       a,b=b,a+b
fibonacci(12)       
