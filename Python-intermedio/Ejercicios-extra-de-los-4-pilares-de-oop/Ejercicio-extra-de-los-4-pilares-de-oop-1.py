class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary if salary >= 0 else 0


    @property
    def name(self):
        return self._name


    @property
    def salary(self):
        return self._salary


    @salary.setter
    def salary(self, value):
        if value < 0:
            print("El salario no puede ser negativo")
        else:
            self._salary = value

    def promote(self, percentage):
        self._salary += self._salary * percentage



employee = Employee("Ana", 1000)
employee.promote(0.1)

print(employee.salary)  # 1100
