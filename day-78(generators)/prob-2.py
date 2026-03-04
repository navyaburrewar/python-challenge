## Write a generator that yields all even numbers between 1 and n.

def fucntion(m):
    for i in range(1,m+1):
        if i%2==0:
            yield i

for i in fucntion(20):
  print(i)            