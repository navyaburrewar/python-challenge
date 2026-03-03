## Create a generator that yields the squares of numbers from 1 to 10.

def square(m):
    for i in range(1,11):
        n=i*i
        yield n

for i in square(10):
    print(i)        