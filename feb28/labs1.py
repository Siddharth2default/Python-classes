##abstraction
#hiding the details and showing what is required
#abstract base class and abstract base methods are 2 concepts

from abc import ABC,abstractmethod

class ATB(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def task1(self):
        pass
    @abstractmethod
    def task2(self):
        pass

class Amit(ATB):
    def task1(self):
        return "Bow bow"
    def task2(self):
        return "Meow"
obj1 = Amit("amit")
print(obj1.task2())
print(obj1.task1()) #amit need to perform task to avoid instantanius error
