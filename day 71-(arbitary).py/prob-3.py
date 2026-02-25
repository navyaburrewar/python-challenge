## Write a function that accepts any number of strings using *args and prints them in uppercase.


def function(*num):
    for char in num :
        print(char.upper())

function("a","b","c","d","y")

