def second_function():
    print("Hello from the second function 👋")
def first_function():
    print("Hello from the first function 🚀")
    second_function()  # calling the second function
first_function()
######################
def my_function():
    local_variable = 100
    print("Inside the function:", local_variable)
my_function()
# Trying to access it outside
#print(local_variable)  # This will cause an error
x = 10  # global variable
def change_value():
    global x  # tell Python we want to use the global one
    x = x + 5
change_value()
print(x)
###########
def sum_list(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total
my_list = [4, 6, 2, 29]
result = sum_list(my_list)
print(result)
###########
def reverse_string(text):
    reversed_text = ""
    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]
    return reversed_text
############
def count_case_letters(text):
    upper_count = 0
    lower_count = 0
    for character in text:
        if character.isupper():
            upper_count += 1
        elif character.islower():
            lower_count += 1
    print(f"There’s {upper_count} upper cases and {lower_count} lower cases")
count_case_letters("I love Nación Sushi")
################
def sort_hyphen_words(text):
    words = text.split("-")
    words.sort()
    sorted_text = "-".join(words)
    return sorted_text
result = sort_hyphen_words("python-variable-funcion-computadora-monitor")
print(result)
#####################
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
def get_prime_numbers(numbers):
    prime_list = []
    for number in numbers:
        if is_prime(number):
            prime_list.append(number)
    return prime_list
my_list = [1, 4, 6, 7, 13, 9, 67]
result = get_prime_numbers(my_list)
print(result)
