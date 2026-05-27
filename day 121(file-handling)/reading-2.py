#============================Reading==========================

# file = open("hi.txt", "r")
# print(file.read())
# file.close()


"""

file =open("moon","r")
print(file.read())
file.close()
"""

### so to read the file 1 st the file sholud be exisit their
## hence the about give the error filenotfound error


file=open("walk","w")
file.write("he is walking")
file.close()


file =open("walk","r")
print(file.read())
file.close()