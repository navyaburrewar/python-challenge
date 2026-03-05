## Write a generator that uses yield from to combine two generators

def gen1(m):
    for i in range(1,m+1):
        yield i
        
        
def gen2(n):
    for a in range(1,n+1):
        yield a

            

def comb(m,n):
      
      
      yield from gen1(m)    
      yield from gen2(n)


for num in comb(5,3):
    print(num)
      