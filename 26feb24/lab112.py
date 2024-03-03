#multilevel
class GF:
    def home(self):
        print("5bhk")

class Father(GF):
    def home2(self):
        print("GOA - father")
class Son(Father):
    def home3(self):
        print("Pramod Bangalore")
pramod = Son()
mmd = Father()
mmd.home()
gkd = GF()
gkd.home()
pramod.home()
mmd.home2()

