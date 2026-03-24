
###########
def sum_list(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total
my_list = [4, 6, 2, 29]
result = sum_list(my_list)
print(result)
