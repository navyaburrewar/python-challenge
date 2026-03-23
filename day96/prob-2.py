# Write a program that exits with:
# code 0 on success
# code 1 if a file is missing



import sys

m=input( )

if m=="navya":
    print("correct password ")
    sys.exit(0)

else:
    print("wrong password")
    sys.exit(1)    

#  in cmd
#  echo %errorlevel%  to know about succesfull or not 
