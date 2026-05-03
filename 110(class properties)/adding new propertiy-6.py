## adding of new properties

class student:
    def __init__(self,name):
        self.name =name
p1=student("navya")

p1.age=20
p1.college="SMEC"

print(p1.name)
print(p1.age)
print(p1.college)