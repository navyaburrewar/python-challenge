## reading a file show the values on the output screen 


## it creating a file  in the  json storing the data

import json

birth = {"year": 2005, "month": 9, "date": 21}

with open("birth.json", "w") as f:
    json.dump(birth, f)



##  which is here  reads the data from json file on the screen

import json

with open("birth.json", "r")as f:
    data=json.load(f)
print(data)   

