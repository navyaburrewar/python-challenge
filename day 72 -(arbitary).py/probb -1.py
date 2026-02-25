# Write a function that takes a fixed argument name and arbitrary positional arguments *args representing marks. Print the average marks.


def name(*marks):
    return sum(marks)/2

print(name(20,30,40,10))

