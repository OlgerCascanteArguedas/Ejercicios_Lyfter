import random

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
#
      
