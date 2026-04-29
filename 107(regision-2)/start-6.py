# ^ whuch is here start means
import re
text = "heloo hi every one"
pattern = r"^h"

match =re.findall(pattern, text)
print(match)