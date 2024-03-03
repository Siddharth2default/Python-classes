#single inheritance
class Father:
    gold = 5
    __private_villa = "Goa"
    def car(self):
        print("lambo of father")

    def flat(self):
        print("3BHK flat of father")
    def villa_access(self,flag):
        if flag:
            print("Yes! Allowed :",self.__private_villa)
        else:
            print("Not AllOWED")

class Son(Father):
    pass

john = Son()
john.car()
print("gold of father ",john.gold)

ron = Father()
print(ron.gold)
ron.flat()
ron.car()
ron.villa_access(True)
john.villa_access(False)