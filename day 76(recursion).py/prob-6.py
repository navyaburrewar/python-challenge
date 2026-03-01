## Write a recursive function to count the number of digits in a number.

def count(m):
    if m<10 and m>-10:
        return 1
    return 1+count(m//10)
print(count(3042229))

        
    