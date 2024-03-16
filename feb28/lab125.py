#encapsulation
#inheritance
#polymorphism (method ovveriding, loading )
#abstraction
#abstraction - oops
#-> hiding the details and showing what is required
#do u know how engine started? how gearbox managed?
#hiding implementatin and showing only imp details
#1. abstract base class 2. abstract class methods
from abc import ABC,abstractmethod

class Animal(ABC):

    def __init__(self,name):
        self.name = name

    @abstractmethod
    def sound(self): #incomplete fn so cant inherit -> abstract meth so separate sound is used if required in dog
        pass

class Dog(Animal):
    def __init__(self,age):
        self.age = 5
    def sound(self):
       return "Bow bow",self.age
    #pass
class Cat(Dog):

    def sound(self):
        return "Meow"

obj1 = Dog("puppy")
print(obj1.sound())
obj3= Cat("kity")
print(obj3.sound())

