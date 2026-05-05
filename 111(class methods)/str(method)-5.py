#before going to strings just analyse it in simple way to understand more better way 



# Think of a student:

# p1.name → asking: “What’s your name?”
# p1.age → asking: “What’s your age?”

# But:
# print(p1) → asking:
# 👉 “Introduce yourself properly”

# And __str__ decides that introduction:
# “Hi, I’m Tobias (36)”

### string method
class person:
    def __init__(self,name,place):
        self.name=name
        self.place=place
    def __str__(self):
        return f"my name is {self.name} and i am from {self.place}"

p1=person("navya","bkd")
print(p1)        





