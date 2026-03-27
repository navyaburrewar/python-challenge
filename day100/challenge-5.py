# Q5. Multiple Inputs

# 📥 Input:

# 3
# hello
# world
# choti

# 👉 Print each word in uppercase


import sys
n=int( sys.stdin.readline())

for i in range(n):
    word=sys.stdin.readline().strip()
    print(word.upper())



