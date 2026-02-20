## Pass the result of one function as an argument to another


def add(a,b):
    return a+b

def multi(c):
    return c

result=add(multi(20),5)
print(result)
    