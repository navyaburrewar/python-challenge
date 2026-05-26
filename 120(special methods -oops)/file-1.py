# #    
# # What Are Special Methods and What Are They Used For?

# Special methods in Python, also known as "magic methods" or "dunder methods", are special Python methods that start and end with double underscores (__). The word "dunder" itself comes from double underscores (d for double, under for underscores).

# You've probably used special methods already without knowing it. Every time you write something like 3 + 4, Python quietly runs 3.__add__(4) under the hood. That's a special method in action. So while you can call special methods directly, you rarely do. Something like 3 + 4 is much clearer and easier to read than calling 3.__add__(4) yourself.

# Apart from __add__, __init__() is another special method you'll see and use the most, as it's a class initializer. There are also others like __len__() and __str__().

# Think of special methods as the directors of the activities between a person programming and the Python language interpreter itself.

# Remember, you don't need to call special methods directly. Instead, Python automatically calls them when certain actions happen. These operations include




# 1.   Arithmetic operations like addition, subtraction, multiplication, division, and others. For addition, __add__() is called, __sub__() for subtraction, __mul__() for multiplication, and __truediv__() for division.

# 2.   String operations like concatenation, repetition, formatting, and conversion to text. __add__() is called for concatenation, __mul__() for repetition, __format__() for formatting, __str__() and __repr__() for text conversion, and so on.

#  3.  Comparison operations like equality, less-than, greater-than, and others. __eq__() is called for equality checks, __lt__() for less-than, __gt__() for greater-than, and so on.

#  4.   Iteration operations like making an object iterable and advancing through items. __iter__() is called to return an iterator and  __next__() to fetch the next item.



# Normally, Python data types like strings and numbers already know how to add things, do concatenation, compare for equality, be used in loops, and others.

# But when you create your own class, Python won't know how to handle things automatically.

# This is where special methods come in — they let you customize Python's built-in behavior.

# Let's say you want to get the number of pages in book objects created with the class below, or compare them and get a readable string of the objects. Here's what happens without special methods:


## without the speacial methods.....
"""

class Book:
   def __init__(self, title, pages):
       self.title = title
       self.pages = pages

book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)


print(len(book1)) # TypeError: object of type 'Book' has no len()
print(str(book1)) # <__main__.Book object at 0x102ed2900>
print(book1 == book2) # False even though they have the same number 

"""


# #  for the about  y it was given errors let we understand detailly
# #  --->len(book1) failed because Python doesn't know how to get the length of your book object without __len__()

# str(book1) printed something like <__main__.Book object at 0x102ed2900> because that's the default representation when you don't use __str__()

# book1 == book2 resulted in False because Python just checks if both objects are the same in memory, not by content.  


# ex-2   ##########
# Here's how you can define your own __len__(), __str__(), and __eq__() special methods to make working with objects created from the Book class easier:

class book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
    def __len__(self):
        return self.pages

    def __str__(self):
        return f"{self.title} has {self.pages}"

    def __eq__(self,other):
        return self.pages ==other.pages


book1=book("the moon",80)
book2=book("the sun",100)

print(len(book1))
print(str(book1))

print(len(book2))
print(str(book2))
print(book1==book2)