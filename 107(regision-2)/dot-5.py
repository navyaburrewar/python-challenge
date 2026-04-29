# .  - any character

import re
text = "cat in the mat"
patt= r"c.t"
match =re.findall(patt,text)
print(match)