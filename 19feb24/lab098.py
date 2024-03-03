class Cal:
    def sum(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def div(self,a,b):
        return a/b
    def mul(self,a,b):
        return a*b
obj_ref = Cal()
result = obj_ref.sum(3,5)
print(result)