#  end with -$
import re

text ="she is a good girl"

pattern =r"girl$"

match = re.findall(pattern,text)
print(match)#  end with -$

## output ==girl since it is correct

#   ex-2

import re
text ="she is a good girl"
pattern =r"girls$"
match = re.findall(pattern,text)
print(match)

## output will be [] empty set since it is last word is not the girls