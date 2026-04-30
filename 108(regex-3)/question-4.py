
#  ?	Zero or one occurrences

import re
text ="navya"
patt = r'n.?y'
x=re.findall(patt, text)
print(x)





import re
text ="navya"
patt = r'n.?v'
x=re.findall(patt, text)
print(x)