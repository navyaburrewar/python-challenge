def print_numbers(n):
    if n == 0:        # base condition
        return
    print(n)
    print_numbers(n-1)  # recursive call

print_numbers(5)

#Factorial using recursion
def factorial(n):
    if n == 1:        # base condition
        return 1
    else:
        return n * factorial(n-1)

num = 5
print("Factorial:", factorial(num))


#Fibonacci using recursion
def fibonacci(n):
    if n <= 1:        # base condition
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 6
print("Fibonacci series:")
for i in range(n):
    print(fibonacci(i), end=" ")