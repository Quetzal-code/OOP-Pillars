class Vehicle:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def start_engine(self):
        print(f"The engine of {self.name}, Year: {self.year}, has started.")

class Car(Vehicle):
    def start_engine(self):
        print(f"The engine of the car {self.name}, Year: {self.year}, roars to life!")

class Boat(Vehicle):
    def start_engine(self):
        print(f"The boat's engine {self.name}, Year: {self.year}, starts with a gentle hum.")

def start_vehicle(vehicle):
    vehicle.start_engine()

def main():
    generic_vehicle = Vehicle("Generic Vehicle", 2020)
    my_car = Car("Honda Civic", 2018)
    my_boat = Boat("Speedy Boat", 2019)

    # Llama al mismo método en objetos de diferentes clases
    start_vehicle(generic_vehicle)  # Comportamiento de Vehicle
    start_vehicle(my_car)           # Comportamiento específico de Car
    start_vehicle(my_boat)          # Comportamiento específico de Boat

if __name__ == "__main__":
    main()
