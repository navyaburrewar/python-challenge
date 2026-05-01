## single inheritance   ### one parent one child relation ship

class parent:
    def aa(self):
        print("elders")

class child(parent):
    def bb(self):
        print("childern")  

c1=parent()
c2=child()
c1.aa()
c2.bb()



##3 multiple inheritance    ### two parents and one childdren

class grandparent:
    def aa(self):
        print("thatha")
class dad:
    def bb(self):
        print("nana")

class child(grandparent,dad):
    def cc(self):
        print("kids")

A1= child()
A1.bb()
A1.cc()     


# ### multilevel inheritance         ### grandfather --> father --> son
class grandfather:
    def zz(self):
        print("older")
class parent(grandfather):
    def aa(self):
        print("elders")

class child(parent):
    def bb(self):
        print("childern") 

A1=child()
A1.aa()        



# ### hierachical inheritance            ## one parent two children

class father:
    def men(self):
        print("piller of home")
class daughter(father):
    def girl(self):
        print("cute girl") 
class son (father):
    def boy(self):
        print("cute boy")
A1=son()
A1.men()       