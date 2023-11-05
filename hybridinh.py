class Vehicle:
    def Vehicle_info(self):
        print("inside vehicle class")

class Car(Vehicle):
    def car_info(self):
        print("inside Car class")

class Truck(Vehicle):
    def truck_info(self):
        print("inside truck class")

class SportsCar(Car,Vehicle):
    def sports_car_info(self):
        print("inside Sports car class")

s_car = SportsCar()

s_car.Vehicle_info()
s_car.car_info()
s_car.sports_car_info()