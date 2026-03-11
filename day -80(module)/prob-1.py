# 
# fibonacci series 
# n=5
# 0 ,1, 1,2,3



def fib(m):  # m=5
  
    if m ==0:
        return 0
    if m==1:
        return 1
       
    else :
        
        return fib(m-1)+fib(m-2)
    

n=int(input())
for i in range(n):
  print(fib(i),end=" ")


### since f(n)==f(n-1)+f(n-2) this  is corect, but not this f(n)=(n-1)+(n-2)







