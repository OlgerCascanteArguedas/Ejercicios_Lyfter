from abc import ABC, abstractmethod
import math


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("El monto a ingresar debe ser mayor que 0")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("El monto a retirar debe ser mayor que 0")
        if amount > self.balance:
            raise ValueError("Fondos insuficientes")
        self.balance -= amount


class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("El monto a retirar debe ser mayor que 0")

        if self.balance - amount < self.min_balance:
            raise ValueError(
                f"No se puede retirar ese monto porque el balance no puede quedar por debajo de {self.min_balance}"
            )

        self.balance -= amount

account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print("Balance BankAccount:", account.balance)  # 1200

savings = SavingsAccount(1000, 200)
savings.deposit(300)
print("Balance antes del retiro:", savings.balance)  # 1300

savings.withdraw(900)
print("Balance después del retiro:", savings.balance)  # 400
