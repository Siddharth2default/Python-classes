#method overloading
#python does not support in traditional sense for methd overloading
#same name of fn with differnet parameter
class Mathutil:
    def add(self,a,b=1,c=0):
        return a+b+c
    #def add(self,a):
     #   pass   #not possible in py#
obj1 = Mathutil()
a = obj1.add(1)
b = obj1.add(2,3)
y = obj1.add(5,6,7)
print(a,b,y)

