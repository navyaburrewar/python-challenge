## access properties
# You can access object properties using dot notation:

class Car:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
car1=Car("bmw","2005")

print(car1.brand)
print(car1.model)
