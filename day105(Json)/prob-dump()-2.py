## dump()
## which here nothimg but which will dumps() from the 
## python to json file

import json
value = {"name" : "choti", "salary": 900000 }
with open("value.json", "w") as f:
    json.dump(value,f)

import json

birth={"year:":2005,"month:": 9,"date:":21}
with open("birth.json", "w") as f:
    json.dump(birth,f)
