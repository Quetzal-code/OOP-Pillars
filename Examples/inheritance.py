class Vehicle:
    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year

    def display_info(self):
        print(f"Vehicle Name: {self.name}, Color: {self.color}, Year: {self.year}")

class Car(Vehicle):
    def __init__(self, name, color, year, mileage):
        super().__init__(name, color, year)  # Llama al constructor de la clase base
        self.mileage = mileage

    def display_car_info(self):
        self.display_info()  # Llama al método de la clase base
        print(f"Mileage: {self.mileage} miles")

def main():
    # Crea una instancia de Vehicle
    my_vehicle = Vehicle("Generic Vehicle", "White", 2020)
    my_vehicle.display_info()

    # Crea una instancia de Car
    my_car = Car("Honda Civic", "Blue", 2018, 30000)
    my_car.display_car_info()

if __name__ == "__main__":
    main()
