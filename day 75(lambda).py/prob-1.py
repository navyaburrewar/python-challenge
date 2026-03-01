## Create a lambda that returns another lambda to calculate power.

# Power factory (creates power machines)
power = lambda n: lambda x: x ** n

# Create different power machines
square_machine = power(2)   # Machine to calculate square
cube_machine = power(3)     # Machine to calculate cube
fourth_machine = power(4)   # Machine to calculate power of 4

# Use the machines
print("Square of 5:", square_machine(5))   # 5^2 = 25
print("Cube of 3:", cube_machine(3))       # 3^3 = 27
print("4th power of 2:", fourth_machine(2)) # 2^4 = 16