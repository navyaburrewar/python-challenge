## 3️⃣

# Write a program that checks how many arguments are passed and prints:

# “No extra arguments” if only script name is present
# “Arguments received” otherwise


import sys

if len(sys.argv )<2:
    print("no extra aruments")
else :      
  print("argument recieved")
