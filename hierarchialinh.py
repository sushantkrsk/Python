class Vehicle:
    def info(self):
        print("This is Vehicle")

class Car(Vehicle):
    def car_info(self,name):
        print("car name is :", name)

class Truck(Vehicle):
    def truck_info(self,name):
        print("truck name is :", name)

obj1 = Car()

obj1.info()
obj1.car_info("BMW")

obj2 = Truck()
obj2.info()
obj2.truck_info("Ford")
