first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']
for i in range(len(first_list)):
    print(first_list[i], second_list[i])
##################
my_string = "Pizza con piña"
for i in range(len(my_string) - 1, -1, -1):
    print(my_string[i])
#################
my_list = [4, 3, 6, 1, 7]
if len(my_list) > 1:
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)
################
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = []
for number in my_list:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)
################
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
