## Write a recursive function to find the sum of digits of a number.

def num(m):
    digit =0
    if m==0:
        return 0
    
    if m>-10 and m<10:
        return m
    
    else:
        return m%10+num(m//10)
         


    
    
print(num(3291))    
        
        