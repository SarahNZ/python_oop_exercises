from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        return f"{self.make} {self.model}"
    
    @abstractmethod
    def get_wheels(self):
        pass

class Car(Vehicle):
    def get_wheels(self):
        return 4

class Motorcycle(Vehicle):
    def get_wheels(self):
        return 2

class Truck(Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model)
        self.payload = payload

    def get_wheels(self):
        return 6
    
# Tests
toyota = Car('Toyota', 'Corolla')
harley = Motorcycle('Harley', 'Turbo')
hilux = Truck('Nissan', 'Hilux', '6 tonnes')

print(toyota.info())  # Toyota Corolla
print(harley.info())  # Harley Turbo
print(hilux.info())   # Nissan Hilux

print(toyota.get_wheels())  # 4
print(harley.get_wheels())  # 2
print(hilux.get_wheels())   # 6