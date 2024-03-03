class Mul_param:
    name = None #class var

    def print(self,first,last,age):
        a=10 #local
        print("Your name is",first,last,age)
        print(self.name)
obj_ref = Mul_param()
obj_ref.print("SIDD","amante",68)