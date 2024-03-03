#encapsulation
#data members/ clas variable
#fns - they are closed within single blue print
#wrapping or binding the data variables with methods

class Car:
    name = None
    #password = "123"
    def __init__(self,name):
        self.name = name
        self.public_name = "publicname" #anyone can access
        self._protected = "prot12"
        self.__private_var = "priv123"
        self.__password = "##$44"

    def _proto(self):
        print("Protected!"+self._protected)
    def __priv(self):
        print("Privat!"+self.__private_var+self.__password)
    def printName(self):
        print("Allowed to use private variable since its inside class"+self.__password)
xuv = Car("XUV")
xuv.printName()
print(xuv.public_name)
#print(xuv.password)
#print(xuv.public_name)
#print(xuv.password)
xuv.printName()
xuv._proto()


