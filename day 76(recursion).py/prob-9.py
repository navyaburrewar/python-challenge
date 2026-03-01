## Write a recursive function to reverse a string

def rev(m):
    if m==0 :
        return  None
    if m==1:
        return 1
    else:
        return m[: :-1]
print(rev("navya"))    