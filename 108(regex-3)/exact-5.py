#  exact number

import re 
text = "helo"
pattern =r"h.{2}o"
x =re.findall(pattern,text)
print(x)