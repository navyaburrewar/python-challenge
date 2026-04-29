# ^ whuch is here start means
import re
text = "heloo hi every one"
pattern = r"^i"

match =re.findall(pattern, text)
print(match)