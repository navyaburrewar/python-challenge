students = [("John", 85), ("Alice", 90), ("Bob", 75)]

sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)