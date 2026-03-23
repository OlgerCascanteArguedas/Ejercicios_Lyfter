def show_menu():
    print("\n=== CALCULATOR MENU ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear result")
    print("6. Exit")


def get_number():
    while True:
        try:
            number = float(input("Enter a number: "))
            return number
        except ValueError:
            print("Error: Invalid number. Please enter a valid numeric value.")


def get_option():
    valid_options = {"1", "2", "3", "4", "5", "6"}
    while True:
        option = input("Select an option (1-6): ")
        if option in valid_options:
            return option
        print("Error: Invalid option. Please select a number from 1 to 6.")


def add(current, value):
    return current + value


def subtract(current, value):
    return current - value


def multiply(current, value):
    return current * value


def divide(current, value):
    if value == 0:
        print("Error: Cannot divide by zero.")
        return current
    return current / value


def clear_result():
    print("Result cleared.")
    return 0.0


def print_current(current):
    print("Current number:", current)


def run_operation(option, current):
    if option == "5":
        current = clear_result()
        print_current(current)
        return current

    value = get_number()

    if option == "1":
        current = add(current, value)
    elif option == "2":
        current = subtract(current, value)
    elif option == "3":
        current = multiply(current, value)
    elif option == "4":
        current = divide(current, value)

    print("Result:", current)
    return current


def main():
    current_number = 0.0
    print("Calculator started.")
    print_current(current_number)

    while True:
        show_menu()
        option = get_option()

        if option == "6":
            print("Exiting calculator...")
            break

        current_number = run_operation(option, current_number)


if __name__ == "__main__":
    main()
