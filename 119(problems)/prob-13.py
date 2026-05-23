# 5. Polymorphism Problems

###########3 Problem 13 — Method Overriding ###########

# Create:

# parent class Shape
# child classes:
# Circle
# Square

# Override method area().


class shape:
    def area(self):
        print("area of shape")
class circle(shape):
    def area(self):
        r=10
        c_area=3.14*r*r
        print(c_area)  
class square(shape):
    def area(self):
        s=10
        s_area=s*s
        print(s_area)
c1=circle()
c1.area()
s1=square()
s1.area()                    
