# Given a list of tuples:

# students = [("John", 85), ("Alice", 92), ("Bob", 78)]
# Sort the list by marks in descending order using lambda.



students = [("John", 85), ("Alice", 92), ("Bob", 78)]

order = sorted(students , key = lambda x :x[1] , reverse=True )
print(order)