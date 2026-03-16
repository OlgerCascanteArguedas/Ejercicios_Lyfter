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


def main():
    current_number = 0.0
    print("Calculator started.")
    print("Current number:", current_number)

    while True:
        show_menu()

        option = input("Select an option (1-6): ")

        if option not in ["1", "2", "3", "4", "5", "6"]:
            print("Error: Invalid option. Please select a number from 1 to 6.")
            continue

        if option == "6":
            print("Exiting calculator...")
            break

        if option == "5":
            current_number = 0.0
            print("Result cleared.")
            print("Current number:", current_number)
            continue

        new_number = get_number()

        if option == "1":
            current_number += new_number
            print("Result:", current_number)

        elif option == "2":
            current_number -= new_number
            print("Result:", current_number)

        elif option == "3":
            current_number *= new_number
            print("Result:", current_number)

        elif option == "4":
            if new_number == 0:
                print("Error: Cannot divide by zero.")
            else:
                current_number /= new_number
                print("Result:", current_number)


if __name__ == "__main__":
    main()
