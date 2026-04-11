# ## it is the dat in the json file

import json
value = {"name" : "choti", "salary": 900000 }
with open("value.json", "w") as f:
    json.dump(value,f)

# What is json.load()?
#  json.load() is used to read data from a JSON file and convert it into a Python object (usually a dictionary).

import json
with open("value.json","r")as f:
    data =json.load(f)
print(data)    
