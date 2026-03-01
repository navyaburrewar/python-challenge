## Write a recursive function to calculate power (x^n).


def func(m,n):
    if n==0 & m==0:
        return 1
    else:
        return m**n
    
print(func(3,3))    