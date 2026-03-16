import random
price = float(input("Enter product price: "))
if price < 100:
    discount = price * 0.02
else:
    discount = price * 0.10
final_price = price - discount
print("Final price:", final_price)
#########
seconds = int(input("Enter time in seconds: "))
if seconds < 600:
    missing_seconds = 600 - seconds
    print(missing_seconds)
elif seconds > 600:
    print("Mayor")
else:
    print("Igual")
##########
number = int(input("Enter a number: "))
total_sum = 0
for i in range(1, number + 1):
    total_sum += i
print("Total sum:", total_sum)
##############
secret_number = random.randint(1, 10)
guess = 0
while guess != secret_number:
    guess = int(input("Guess the number (1-10): "))

    if guess != secret_number:
        print("Try again!")
print("Correct! You guessed the number.")
###############
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 == 30 or num2 == 30 or num3 == 30:
    print("Correct")
elif num1 + num2 + num3 == 30:
    print("Correct")
else:
    print("Incorrect")
#################
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
print("Fahrenheit:", fahrenheit)
print("Kelvin:", kelvin)
#################
number = int(input("Enter a number (1-10): "))
for i in range(1, 13):
    print(number, "x", i, "=", number * i)
