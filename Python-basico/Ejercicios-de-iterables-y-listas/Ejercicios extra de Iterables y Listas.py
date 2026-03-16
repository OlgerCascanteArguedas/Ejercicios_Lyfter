numbers_input = input("Enter a list of numbers separated by commas: ")
my_list = [int(number) for number in numbers_input.split(",")]
number_to_search = int(input("Enter the number to search: "))
count = my_list.count(number_to_search)
print(f"The number {number_to_search} appears {count} times")
##########
numbers_input = input("Enter a list of numbers separated by commas: ")
my_list = [int(number) for number in numbers_input.split(",")]
all_positive = True
for number in my_list:
    if number <= 0:
        all_positive = False
        break
if all_positive:
    print("All numbers are positive")
else:
    print("There is at least one negative number or zero")
################
numbers_input = input("Enter a list of numbers separated by commas: ")
my_list = [int(number) for number in numbers_input.split(",")]
smallest = my_list[0]
for number in my_list:
    if number < smallest:
        smallest = number
print(f"The smallest value is {smallest}")
###############
numbers_input = input("Enter a list of numbers separated by commas: ")
my_list = [int(number) for number in numbers_input.split(",")]
total = 0
for number in my_list:
    total = total + number
average = total / len(my_list)
new_list = []
for number in my_list:
    if number > average:
        new_list.append(number)
print("Average:", average)
print("New list:", new_list)
###########
words = []
for i in range(5):
    word = input(f"Enter word {i + 1}: ")
    words.append(word)
new_list = []
for word in words:
    if len(word) > 4:
        new_list.append(word)
print("New list:", new_list)
