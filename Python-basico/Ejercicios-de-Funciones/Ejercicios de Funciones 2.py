
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
