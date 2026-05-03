# Challenge: Class Methods
# Test your understanding of class methods by completing a small coding challenge.

# Instructions
# Inside the editor, complete the following steps:
# Create a class called Rectangle
# Add an __init__ method with width and height, and store them as properties
# Add a method called area that returns the width multiplied by the height
# Create an object r1 with width 5 and height 3
# Print the area of r1



# Create the Rectangle class
class Rectangle:
  def __init__(self,width,height):
      self.width=width
      self.height=height
  def area(self):
      return self.width*self.height
r1=Rectangle(5,3)

print(r1.area())