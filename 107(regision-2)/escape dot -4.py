## escape dot \.
## which actually means prints only the dot nothing else

import re
tect ="navya.22.3"
patt =r"\."
match = re.findall(patt,tect)
print(match)
