class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Hace un sonido"


class Dog(Animal):
    def speak(self):
        return "Guau"


class Cat(Animal):
    def speak(self):
        return "Miau"


# --- Ejemplo ---
dog = Dog("Firulais")
print(dog.speak())  # Guau

cat = Cat("Michi")
print(cat.speak())

animal = Animal("Animal")
print(animal.speak())  # Miau
