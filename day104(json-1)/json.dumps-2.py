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