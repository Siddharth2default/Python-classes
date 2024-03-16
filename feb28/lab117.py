class Father:
    def home(self):
        return "This is father home"
class Pramod(Father):
    pass
    #def home(self):
     #   return "This is pramod home"
class bro2(Father):
    def home(self):
        return "This is bro home"
    #def info(self):
     #   return "This is Cycle"
#obj1 = Car()
#obj2 = Cycle()
#print(obj1.info())
#print(obj2.info())
obj3 = Pramod()
print(obj3.home())
