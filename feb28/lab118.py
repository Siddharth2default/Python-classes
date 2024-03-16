#multiple
#F,M->S
class Father:
    def father_money(self):
        return "5"
    def home(self):
        print("Father home")


class Mother:
    def mother_money(self):
        return "15"

    def home(self):
        print("Mother home")
class Son(Mother,):
    pass
    #def home(self):
     #   print("son s home priority")

obj1 = Son()
print(obj1.father_money())
print(obj1.mother_money())
obj1.home() #method resolution order - MRO
print(Son.mro())
