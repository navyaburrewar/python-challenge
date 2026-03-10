# 
# fibonacci series



def fib(m):
    if m ==0:
        return 0
    if m==1:
        return 1
    
    else :
        return fib(m-1)+fib(m-2)
    


print(fib(5))


### since f(n)==f(n-1)+f(n-2) this  is corect, but not this f(n)=(n-1)+(n-2)






