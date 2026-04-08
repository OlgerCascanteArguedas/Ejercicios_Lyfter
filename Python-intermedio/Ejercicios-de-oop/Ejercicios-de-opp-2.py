class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} ha subido al bus.")
        else:
            print("El bus está lleno.")

    def remove_passenger(self):
        if self.passengers:
            person = self.passengers.pop()
            print(f"{person.name} ha bajado del bus.")
        else:
            print("No hay pasajeros en el bus.")

class Person:
    def __init__(self, name):
        self.name = name


