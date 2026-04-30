# ^ whuch is here start means
import re
text = "heloo hi every one"
pattern = r"^i"

match =re.findall(pattern, text)
print(match)

## Matches only if string starts with "h"
#  r"^i" for this it gives an empty string
# []