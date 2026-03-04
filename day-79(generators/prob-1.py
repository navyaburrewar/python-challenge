## Create a generator that mimics the behavior of range() using yield.


def function(start,stop):
    current = start
    while current <stop:
        yield current
        current+=1

for i in function(1,6):
    print(i)        