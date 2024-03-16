#hierarchial inheritance
#class a->b and c (b->d and e
class Vehicle:
    def info(self):
        return "This is vehicle"
class Car(Vehicle):
    def info(self):
        return "This is Car"
class Cycle(Vehicle):
    pass
    #def info(self):
     #   return "This is Cycle"
obj1 = Car()
obj2 = Cycle()
print(obj1.info())
print(obj2.info())