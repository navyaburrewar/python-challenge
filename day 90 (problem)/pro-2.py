# print a string "Hi I'm Bhavanidevi Btech ECE with 80%"
#fun(name="Bhavanidevi",course="Btech", branch="ECE", perc=80%)

def funct(**value ):
    return "hi I m"+" "+value["name"]+" "+value["course"]+" "+value["branch"]

print(funct(name="navya",course="btech",branch="csm",perc="80%"))    