## Create a function that takes **kwargs representing product details (name, price, quantity) and prints a formatted invoice


def func(**product):
    print("----invoice----")
    print( "name" ,product["name"])
    print("price" ,product["price"])
    print("quality" ,product["quality"])

func(name = "pen" , price = "20"  , quality = "good")    