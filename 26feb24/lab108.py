class Secureclass:
    #def __init__(self):
    def submit(self):
        self.__password = "#@123"
        self.__username = "admin"
        self.heading = "VWO login page"

obj1 = Secureclass()
obj1.submit()
print(obj1.heading)
