#Fibonacci series using a for loop
n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

n = int(input("Enter number of terms: "))

#Fibonacci series using while loop
a = 0
b = 1
count = 0

print("Fibonacci series:")

while count < n:
    print(a, end=" ")
    a = b
    b = a + b
    count += 1