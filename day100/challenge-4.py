# 🟡 Q4. Count Words

# 📥 Input:
# i love coding very much
# 👉 Print number of words


import sys
words=sys.stdin.readline().split()
print(words)
count=0
for word in words:

    count+=1
print(count)    
