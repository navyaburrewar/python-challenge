# ✅ 4. Print Pattern (Right Triangle)

# Task:

# *
# **
# ***
# ****

import sys
n=5
for i in range(n):
    for j in range(i+1):
        sys.stdout.write("*" * j+"\n")