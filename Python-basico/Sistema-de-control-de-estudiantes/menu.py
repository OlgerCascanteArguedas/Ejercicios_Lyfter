from actions import (
    add_students,
    show_students,
    top_3,
    overall_average,
    delete_student,
    show_failed_students
)
from data import export_csv, import_csv

students = []

def menu():
    while True:
        print("\nMENU")
        print("1. Add students")
        print("2. Show students")
        print("3. Top 3")
        print("4. Overall average")
        print("5. Export CSV")
        print("6. Import CSV")
        print("7. Delete student")
        print("8. View failed students")
        print("9. Exit")

        option = input("Option: ")

        if option == "1":
            add_students(students)
        elif option == "2":
            show_students(students)
        elif option == "3":
            top_3(students)
        elif option == "4":
            overall_average(students)
        elif option == "5":
            export_csv(students)
        elif option == "6":
            import_csv(students)
        elif option == "7":
            delete_student(students)
        elif option == "8":
            show_failed_students(students)
        elif option == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
