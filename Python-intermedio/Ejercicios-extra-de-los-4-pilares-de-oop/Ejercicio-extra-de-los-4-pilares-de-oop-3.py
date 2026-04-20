class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return f"{self._brand} ({self._year})"

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def get_info(self):
        return f"{self._brand} ({self._year}) - {self.doors} puertas"


class Motorcycle(Vehicle):
    def __init__(self, brand, year, type_):
        super().__init__(brand, year)
        self.type_ = type_

    def get_info(self):
        return f"{self._brand} ({self._year}) - {self.type_}"


vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")

print(vehicle1.get_info())  # Toyota (2020) - 4 puertas
print(vehicle2.get_info())  # Yamaha (2022) - Deportiva
