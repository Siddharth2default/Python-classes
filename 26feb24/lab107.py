class Myclass:
    def __init__(self):
        self.name = "Amit" #publc
    def public_func(self):
        print("Public functions")
    def __private_func(self):
        print("Private functyion!!!")
    def pub_f_private(self):#to access private function separate method is used
        self.__private_func()
#security -> not everyone can access your variables and functions
a = Myclass()
a.public_func()
a.pub_f_private()