class Person:
    name = "Lambo"
    age = 1
    #def __init__(self,name,age):
     #   self.name= name
      #  self.age= age

    def walk(self):
        a=10 #local variable
        print("Hi your name is",self.name)
        print("Your age is ",self.age)

obj1 = Person()
obj1.walk()
