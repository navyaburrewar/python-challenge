# write a decorator to implement square of a number  which was acquired by the 2 func add() & sub() these are outer functions

def decorators(func):
    def inner(a,b):
        result= func(a,b)
        print(result**2)
    return inner




@decorators
def sep(m,n):
    
    return m-n
m=int(input())
n=int(input())
sep(m,n)

@decorators
def add(k,l):
    return k+l
k=int(input())
l=int(input())
add(k,l)