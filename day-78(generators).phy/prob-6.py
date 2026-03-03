## Write a generator function to generate Fibonacci numbers up to n terms..

def fibonacci(n):
    for i in range(1,n+1):
     a=0
     b=1
    for _ in range(n):
     yield  a
     a,b =b,a+b
 
for  num in  fibonacci(8):
  print(num)