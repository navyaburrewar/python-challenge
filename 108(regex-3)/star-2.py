import re

text ="she is an goood girl"
pattern = "she.*girl"

x= re.findall(pattern,text)
print(x)




# ex-2

import re

text ="she is an goood girl"
pattern = "s.*h"

x= re.findall(pattern,text)
print(x)