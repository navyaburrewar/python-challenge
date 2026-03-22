# # Write a program that checks if at least two arguments are passed.
# If not, print a usage message like:

# Usage: python app.py <arg1> <arg2>


import sys
if len(sys.argv)<3:
    print("Usage: python app.py <arg1> <arg2>")
else :
    print(sys.argv)    