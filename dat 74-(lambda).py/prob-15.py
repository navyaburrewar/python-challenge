# Given a list of dictionaries:

# employees = [
#     {"name": "John", "salary": 50000},
#     {"name": "Alice", "salary": 70000},
#     {"name": "Bob", "salary": 45000}
# ]

# Sort the list by salary using lambda.

employees = [
    {"name": "John", "salary": 50000},
    {"name": "Alice", "salary": 70000},
    {"name": "Bob", "salary": 45000}
]


emp2 =sorted(employees, key = lambda employees :employees["salary"])
print(emp2)