import re

text ="she is an good girl"
sen = r"[aeiou]"
x =re.findall(sen,text)
print(x)

## code explanation
## r is the  rawstring
# finall searches all the characters in the sentence
