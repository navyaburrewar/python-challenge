# Print numbers from 1 to N
def num (m,n):
    if m==n:
        return
    print(m)
    num(m+1,n)

num(1,5)


## Print numbers from 1 to n

def num(m):
    if m==0:
        return 
  
    num(m-1)
    print(m)
 
print(num(6))    