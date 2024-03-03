#web automation - selenium
# page - You are automating
class VWLogin():
    email_a = None
    password = None
    def __init__(self,o_email,password):
        self.email_a = o_email
        self.password = password
        print(self.password)
    def loginconfirm(self):
        if self.password == "pwd123":
            print("allowed")
        else:
            print("Not allowed")
amit = VWLogin("sidd",23)
#amit.submit()
pramod = VWLogin("pp@aam.com","pwd123")
pramod.loginconfirm()
amit.loginconfirm()
#sidd = VWLogin("hik",23)
print(id(amit))
print(id(pramod))