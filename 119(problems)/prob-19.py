# 7. Mini Real-Time OOP Projects
# Problem 19 — Library Management

# Features:

# add books
# issue books
# return books

# Use:

# classes
# objects
# constructors


class library:
    def __init__(self,books):
        self.books=books
    def add(self,add_books):
        self.books=self.books+add_books  
        print(self.books) 
    def issue(self,remove_books):
        self.books=self.books-remove_books   
        print(self.books)
    def get_books(self):
        print(self.books)
l1=library(10)
l1.add(5)  
l1.issue(5)
l1.get_books()      
             
        