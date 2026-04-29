
import re

text = "age: 20"
pattern = r"\d+"

match=re.findall(pattern,text)
print(match)










# # \d → any digit (0–9)
# + → one or more times
# \d+ → group of digits (numbers)
# re.findall() → returns all matches in a list