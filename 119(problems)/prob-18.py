# Problem 18 — Shape Abstract Program

# Abstract class:

# Shape

# Abstract method:

# area()

# Child classes:

# Rectangle
# Triangle
# Circle


from  abc import ABC ,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(shape):
    def area(self):
        l=9
        b=8
        r_area=l*b
        print(r_area)
class triangle(shape):
    def area(self):
        h=5
        b=4
        s_triangle=1/2*b*h
        print(s_triangle)
class circle(shape):
     def area(self):
        r=5                    
        r_circle=3.14*r*r
        print(r_circle)
r1=Rectangle()
t1=triangle()
c1=circle()
 
r1.area()
t1.area()
c1.area()
