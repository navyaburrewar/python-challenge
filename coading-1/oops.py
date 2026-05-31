class parent:
    def hands(self):
        print("two hands")
class child(parent):
    def legs(self):
        print("two legs")
c1=child()
c1.hands()
c1.legs()                
