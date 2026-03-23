
numbers = []
for i in range(10):
    value = int(input("Enter a number: "))
    numbers.append(value)
highest_number = numbers[0]
for number in numbers:
    if number > highest_number:
        highest_number = number
print("Numbers entered:", numbers)
print("The highest number was:", highest_number)
