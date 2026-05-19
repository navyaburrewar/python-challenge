#Create base class:Employee
# Subclasses:Manager Developer Intern 
# Each employee has: name salary 
# Manager gets bonus salary. 
# Developer gets project allowance.
# Intern gets stipend.


class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def  calaulate_salary(self):
        print("employee",self.salary)

class manager(employee)  :
    def calaulate_salary(self):
        bonus=20000
        total =self.salary+bonus
        print(self.name,"manager salary :",total)
class developer(employee):
    def calaulate_salary(self):
        allowance=100000
        total =self.salary+allowance
        print(self.name,"developer salary:",total)
class intern(employee):
    def calaulate_salary(self):
        stipend =10000
        total =self.salary+stipend
        print(self.name,"intern :",total)
m =manager("keerthi",30000)
d=developer("nav",40000)
i=intern("neha",80000)
m.calaulate_salary()
d.calaulate_salary()
i.calaulate_salary()
              