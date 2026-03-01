## Write a recursive function to find the nth Fibonacci number.

def fibo(m):
    if m==0:
        return 0
    elif m==1:
        return 1
    else:
        return  fibo(m-1)+fibo(m-2)
print(fibo(5))    
    