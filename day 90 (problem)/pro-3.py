### #find the prime numbers for the given range---100



## find the prime numbers for the given range

def prime(m):
    if m <= 1:
        return False
    if m == 2:
        return True
    
    for i in range(2, m):
        if m % i == 0:
            return False
    
    return True


n = int(input("Enter range: "))
for i in range(1, n + 1):
    if prime(i):
        print(i)
        print(i)