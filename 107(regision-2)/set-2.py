import re

rollno = "23k81a6615"
num = r"[1-9]"

match =re.findall(num,rollno)
print(match)
