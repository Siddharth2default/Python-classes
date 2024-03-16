#polymorphism - oops
# (poly)many - forms(morphism)
class Shape :
    def area(self):
        print("Area of Shape")
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius


obj1 = Rectangle(3,4)
print(obj1.area())

obj2 = Circle(10)
print(obj2.area())
print(Circle.mro())
obj3 = Shape()
obj3.area()

#area - name remains same but purpose is different -> polymorphism



