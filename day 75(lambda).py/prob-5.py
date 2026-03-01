# Create a lambda-based function generator that:

# Takes a number n
# Returns a function that checks if a number is divisible by n


divisible_by = lambda n : lambda x:x%n ==0
check_by_3 = divisible_by(3)
check_by_5 = divisible_by(5)


print(check_by_3(9))   # True
print(check_by_3(10))  # False
print(check_by_5(20))  # True
print(check_by_5(14))  # False