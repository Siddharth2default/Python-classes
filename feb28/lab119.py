#hybrid - multi level +multiple/hirearchial
class A:
    def method_a(self):
        return "Method A"
class B(A):
    def method_b(self):
        return "Method B"
class C(A):
    def method_c(self):
        return "Method C"
class D(B,C):
    pass
    #def method_d(self):
     #   return "Method D"

d = D()
print(d.method_a())
print(d.method_b())
print(d.method_c())
#print(d.method_d())

