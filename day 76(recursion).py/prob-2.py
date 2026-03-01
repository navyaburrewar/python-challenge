## Print numbers from N to 1

def num(m):
    if m==0:
        return 
    print(m)
    num(m-1)


print(num(6))    