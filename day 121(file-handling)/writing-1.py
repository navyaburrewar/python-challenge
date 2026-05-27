#=================================writing=======================
# if file exists file overwrites 
# if file doesn't -w creates it
# file = open("m1.txt", "w")
# file.write("mentoring 3")
# file.close()


########### another method  ############ 
# with open("hi.txt", "w") as file:
#    file.write("hi everyone")



file=open("navya.txt","w")
file.write("dancing")
file.close()


######### another method #################
with open("choti","w") as file:
    file.write("good girl")