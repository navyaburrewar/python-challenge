# Problem 11 — Person → Teacher

# Parent class:

# Person

# Child class:

# Teacher

# Add:

# subject
# salary

# Display all information.

class Person:
    pass


class Teacher(Person):

    def __init__(self, subject, salary):

        self.subject = subject
        self.salary = salary


t1 = Teacher("English", 200000)

print(t1.subject)
print(t1.salary)