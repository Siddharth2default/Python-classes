#classes and objects
#class ->attributes and behavior
#person -> obj ->vani,pramod,srerma
class Person:
    #attributes->data members
    name = None
    age = None
    id = None
    phone = None
    #behavior-methods(not functions)
    def talk(self):
        print("I am method")
    def walk(self,name):
        print("sleep",name)

    def other():
        print("I am method3n")
def another():
    print("I am function")
#objects = classname()
#self - instance of class
sriram = Person()
sriram.name="shreeram"
print(sriram.name)
sriram.talk()
pramod = Person()
amit = Person()
#nothing inmemory,exit program now