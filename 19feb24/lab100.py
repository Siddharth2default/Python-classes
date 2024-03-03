class Car:
    color = None
    model = None
    def details(self):
        print("details",self.color,self.model)
car_color = input("color say:")
color_model = input("model pls:")
car_ref = Car()
car_ref.color = car_color
car_ref.model = color_model
car_ref.details()