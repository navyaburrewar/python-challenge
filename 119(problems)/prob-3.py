 ################# prob-3 #################


# Create a class Mobile with:

# brand
# price
# color

# Create multiple objects and print all details.


class mobile:
    def __init__(self,brand,price,color):
        self.brand=brand
        self.price=price
        self.color=color
m1=mobile("samasug",20000,"black")
m2=mobile("oppo",12000,"blue")
m3=mobile("vivo",25000,"red")

print(m1.brand,m1.color,m1.price)

print(m2.brand,m2.color,m3.price)
print(m3.brand,m3.color,m1.price)

