class Car:
    name = None
    make = None
    model = None
    def __init__(self,o_name,o_make,o_model): #spexccial f(n),auto call
        self.name = o_name
        self.make = o_make
        self.model = o_model
    def start_engine(self):
        print("Start car with name"+self.name)
        print("Start car with make"+self.make)
        print("Start with model"+self.model)
lambo = Car("lambo","V2","2023")
lambo.start_engine()
print("----")
suv = Car("SUVx","Japan","2019")
suv.start_engine()
