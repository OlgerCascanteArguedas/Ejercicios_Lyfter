class Flyable:
    def fly(self):
        return "Estoy volando"


class Swimmable:
    def swim(self):
        return "Estoy nadando"


class Duck(Flyable, Swimmable):
    def quack(self):
        return "Cuac cuac"

duck = Duck()
print(duck.fly())    # Estoy volando
print(duck.swim())   # Estoy nadando
print(duck.quack())  # Cuac cuac
