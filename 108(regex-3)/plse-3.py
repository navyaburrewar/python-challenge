import re
text ="she is a good girl"
pattern = r"s.+h"
x=re.findall(pattern,text)
print(x)



import re
text ="she is a good girl"
pattern = r"g.+d"
x=re.findall(pattern,text)
print(x)