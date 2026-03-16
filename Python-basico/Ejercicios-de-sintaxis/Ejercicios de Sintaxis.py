import random
# string + string
print("Hello " + "World")
# Output: Hello World
# string + int
# print("Age: " + 30)
# ERROR → TypeError: can only concatenate str (not "int") to str
# int + string
# print(30 + " years")
# ERROR → TypeError
# list + list
print([1, 2] + [3, 4])
# Output: [1, 2, 3, 4]
# string + list
# print("Hello" + [1, 2])
# ERROR → TypeError
# float + int
print(5.5 + 2)
# Output: 7.5
# bool + bool
print(True + True)
# Output: 2 (True = 1, False = 0)
##################
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
if age <= 2:
    category = "Baby"
elif age <= 12:
    category = "Child"
elif age <= 14:
    category = "Pre-teen"
elif age <= 17:
    category = "Teenager"
elif age <= 25:
    category = "Young Adult"
elif age <= 64:
    category = "Adult"
else:
    category = "Senior Adult"
print(first_name, last_name, "is a", category)
###################
secret_number = random.randint(1, 10)
guess = 0
while guess != secret_number:
    guess = int(input("Guess the secret number (1-10): "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")
###########
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
largest_number = max(number1, number2, number3)
print("The largest number is:", largest_number)
###########
total_grades = int(input("How many grades will you enter? "))
approved_count = 0
failed_count = 0
sum_all = 0
sum_approved = 0
sum_failed = 0
for i in range(total_grades):
    grade = float(input("Enter grade: "))
    sum_all += grade
    if grade >= 70:
        approved_count += 1
        sum_approved += grade
    else:
        failed_count += 1
        sum_failed += grade
average_all = sum_all / total_grades
if approved_count > 0:
    average_approved = sum_approved / approved_count
else:
    average_approved = 0
if failed_count > 0:
    average_failed = sum_failed / failed_count
else:
    average_failed = 0
print("Approved grades:", approved_count)
print("Failed grades:", failed_count)
print("Average of all grades:", average_all)
print("Average of approved grades:", average_approved)
print("Average of failed grades:", average_failed)
