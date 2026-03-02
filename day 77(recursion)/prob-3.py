## Write a recursive function to find the greatest common divisor (GCD) of two numbers.


def gcd(m,n):
    if n==0:
        return m
    else :
        return gcd(n, m%n)
print(gcd(3,43))    