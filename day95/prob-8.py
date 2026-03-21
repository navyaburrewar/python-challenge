# Write a program that prints the script filename and the total number of arguments passed.


import sys
filename = sys.argv[0]

arg_count =len(sys.argv)-1

print(filename,arg_count)