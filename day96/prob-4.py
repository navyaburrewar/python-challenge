# 2️⃣8️⃣ Write code where:
# a loop stops
# and program also terminates


import sys

n=int(input())

for i in range (1,n):
    if i==5:
        
        sys.exit()
    print(i)

print("exit")


