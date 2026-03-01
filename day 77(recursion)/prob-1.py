## Write a recursive function to check if a string is a palindrome.


def palin(m):
    if len(m)<1:
        return True
    
    if m[0]==m[-1]:
        return palin(m[1:-1])
    else:
        return False
    
print(palin("choti"))    
print(palin("madam")) 
