# Write a recursive function to find the sum of first N natural numbers


def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
print(sum(5))    