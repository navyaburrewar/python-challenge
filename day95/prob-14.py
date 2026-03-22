# 🔟
# Write a program that joins all command-line arguments into a single sentence.

# Example:
# python join.py I love Python

# Output:
# I love Python


import sys
sen = " ".join(sys.argv)
print(sen)