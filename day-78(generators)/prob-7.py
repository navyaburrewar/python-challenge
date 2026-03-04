## Create a generator that yields prime numbers up to a given limit.

def prime (limit):
    for num in range(2,limit+1):
        count =0
        for i in range (1,num+1):
            if num%i==0:
                count+=1
        if count ==2:
            yield num
for m in prime(20):
    print(m)                    
