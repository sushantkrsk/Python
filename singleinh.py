class Vehicle:
    def Vehicle_info(self):
        print("inside Vehicle class")

class Car(Vehicle):
    def car_info(self):
        print("Inside car class")

car=Car()

car.Vehicle_info()
car.car_info()




