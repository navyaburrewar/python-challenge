
def kangaroo(x1, v1, x2, v2):
    n=0
    while n<10000:
        d1=x1+(n*v1)
        d2=x2+(n*v2)
        if d1==d2:
            return "YES"
        
        n+=1
    
    return "NO"
print(kangaroo(0,4,2,2))
print(kangaroo(0,2,2,4))