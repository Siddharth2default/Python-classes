#core cocepts of polymorphism
#method overriding -> same name in parent and child

class Animal:
    def __init__(self):
        pass
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def __init__(self):
        pass
    def sound(self):
        super().sound()
        print("Dog sound")


#obj1 = Animal()
#obj1.sound()
obj2 = Dog()
obj2.sound()