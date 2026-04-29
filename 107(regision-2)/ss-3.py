import re
text ="navya-21"
patter = r"\d+"

match = re.findall(patter, text)
print(match)
