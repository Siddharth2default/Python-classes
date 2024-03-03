class Password:
    def __init__(self,password):
        self.__password = password
        self.public_var =10
    def get_pass(self,is_auth):
        if is_auth:
            return self.__password
        else:
            print("Invalid !")
    def set_pass(self,password):
        if len(password) >10:
            self.__password=password
            print("Updated password",self.__password)
        else:
            print("Not allowed weak pasword")
pwd = Password("HACK12")
#print(pwd.public_var)

print(pwd.get_pass(True))
pwd.set_pass("MASS$$$$3####72")
