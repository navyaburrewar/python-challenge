import json
x={
    "name": "navya",
    "age": 20,
    "city": "hyd"
}

y=json.dumps(x)
print(y)


##3 the output code will be in the formate of string where we will not understand the values here 
## it is just a text, we wil not access the values


import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))




## prob-2

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}



print(json.dumps(x, indent=4))


### a small explanation for the about code that 

## rules for the indentation it was taking here

## Rule 1: Each key goes to a new line
##      "name": "John",
#        "age": 30,
## rule-2 : Nested data gets extra indentation
#      "cars": [
#     {
#         "model": "BMW 230",
#         "mpg": 27.5
#     }
# ]
#        cars → 4 spaces
#        inside {} → 8 spaces

#  Rule 3: Lists (arrays) also break into lines
#   "children": [
#     "Ann",
#     "Billy"
# ]
#   Each item gets its own line



# | Python            | JSON              |
# | ----------------- | ----------------- |
# | `True`            | `true`            |
# | `False`           | `false`           |
# | `None`            | `null`            |
# | `("Ann","Billy")` | `["Ann","Billy"]` |

#  Your tuple becomes a list in JSON