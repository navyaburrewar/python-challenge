## Create a generator that yields characters of a given string one at a time.

def str(m):
    for ch in m:
        yield ch

for ch in str("navya"):
    print(ch)        