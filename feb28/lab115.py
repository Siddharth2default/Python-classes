#multi level inheritance
# a->b->c->>>
class GF():
    def grand(self):
        return "Grand father method!"

class Father(GF):
    def parent(self):
        return "Parents method!"

class Son(Father):
    def child(self):
        return "Sons method"

obj1 = GF()
print(obj1.grand())
obj2 = Father()
print(obj2.parent(),obj2.grand())
obj3 = Son()
print(obj3.grand(),obj3.parent(),obj3.child())