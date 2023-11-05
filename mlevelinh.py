class Vehicle:
    def Vehicle_info(self):
        print("inside Vehicle class")

class Car(Vehicle):
    def car_info(self):
        print("inside car class")

class SportsCar(Car):
    def sports_car_info(self):
        print("inside SportsCar class")

s_car = SportsCar()

s_car.Vehicle_info()
s_car.car_info()
s_car.sports_car_info()
