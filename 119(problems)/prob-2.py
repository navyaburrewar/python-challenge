
#   prob-2 ----> rectangle
# Create a class Rectangle with:

# length
# breadth

# Methods:

# area()
# perimeter()

class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        rec_area=self.length*self.breadth
        print( rec_area)  
    def perimeter(self):
        rec_perimeter=2*(self.length+self.breadth)
        print(rec_perimeter)
r1=rectangle(5,5)
r1.area()
r1.perimeter()