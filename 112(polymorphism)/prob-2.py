          
#Create abstract class:Shape ,Abstract method:area()
#  Subclasses:Circle, Rectangle, Triangle Calculate respective areas.

from abc import ABC,abstractmethod
class shape:
    @abstractmethod
    def area(self):
        print("area of shape")

class circle(shape):
    def area(self):
        r=2
        print(3.141*r*r)
class rectangle(shape):
    def area(self):
        l=4
        b=8
        print(l*b)  
class triangle(shape):
    def area(self):
        b=7
        h=2
        print((b*h)/2)
t=triangle()
r=rectangle()
c=circle()
t.area()
r.area()
c.area()
