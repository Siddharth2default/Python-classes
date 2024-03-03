#car
#objects - tesla,lambo
class Car:
    name = None
    color = None
    model = None
    def start_engine(self):
        print("starting engine")
    def car_break(self):
        print("Applying break")
    def who(self):
        print("I am driving"+self.name)
tesla = Car()
lambo = Car()
tesla.name = "Tesla"
lambo.name = "lamb"
tesla.who()
lambo.who()