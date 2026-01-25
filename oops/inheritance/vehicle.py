class Vehicle:
    
    def start(self):
        print("vehicle started")

class Car(Vehicle):
    def drive(self):
        print("car is driving")
obj=Car()
obj.start()
obj.drive()