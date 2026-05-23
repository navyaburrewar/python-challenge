# Problem 8 — Password Manager

# Create a class PasswordManager.

# private variable __password
# methods:
# set_password()
# get_password()


class PasswordManager:
    def __init__(self):
        self.__password="cho@21"
    def set_password(self,newpassword):
        self.__password=newpassword
    def get_password(self):
        print(  self.__password  )   
p1 =PasswordManager()
p1.set_password("nandhu@27")
p1.get_password()      