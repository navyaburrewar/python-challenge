## python json

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.


#  JSON in Python
#  Python has a built-in package called json, which can be used to work with JSON data.


#  importing the json module
import json



# Parse JSON - Convert from JSON to Python
#3 json.load

# here we use the   json.load to convert the text into the usefull formate that which will help here 
## here which will help here it performs in accessing values
## before it will not be in access formate it only in string formate

import json
x='{"name":"navya","age":30,"city":"New York"}'
y=json.loads(x)

print(y["age"])
print(y["name"])