
import csv
import os
students = []
def get_int(message):
    while True:
        try:
            value = int(input(message))
            return value
        except:
            print("Invalid number, try again.")
def get_grade(message):
    while True:
        try:
            grade = float(input(message))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except:
            print("Invalid input, enter a number.")
def add_students():
    n = get_int("How many students? ")

    for i in range(n):
        print("\nStudent", i + 1)

        name = input("Name: ")
        section = input("Section: ")

        spanish = get_grade("Spanish: ")
        english = get_grade("English: ")
        social = get_grade("Social Studies: ")
        science = get_grade("Science: ")

        student = {
            "name": name,
            "section": section,
            "spanish": spanish,
            "english": english,
            "social": social,
            "science": science
        }
        students.append(student)
def show_students():
    if len(students) == 0:
        print("No students.")
        return
    for s in students:
        avg = (s["spanish"] + s["english"] + s["social"] + s["science"]) / 4
        print("\nName:", s["name"])
        print("Section:", s["section"])
        print("Average:", round(avg, 2))
def top_3():
    if len(students) == 0:
        print("No students.")
        return
    sorted_list = sorted(
        students,
        key=lambda x: (x["spanish"] + x["english"] + x["social"] + x["science"]) / 4,
        reverse=True
    )
    print("\nTop 3:")
    for i in range(min(3, len(sorted_list))):
        s = sorted_list[i]
        avg = (s["spanish"] + s["english"] + s["social"] + s["science"]) / 4
        print(i + 1, "-", s["name"], "-", round(avg, 2))
def overall_average():
    if len(students) == 0:
        print("No students.")
        return
    total = 0
    for s in students:
        avg = (s["spanish"] + s["english"] + s["social"] + s["science"]) / 4
        total += avg
    print("Overall average:", round(total / len(students), 2))
def export_csv():
    if len(students) == 0:
        print("No data.")
        return
    try:
        with open("students.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["name", "section", "spanish", "english", "social", "science"]
            )
            writer.writeheader()
            writer.writerows(students)
        print("Exported successfully!")
    except:
        print("Error exporting file.")
def import_csv():
    if not os.path.exists("students.csv"):
        print("File not found.")
        return
    try:
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = {
                    "name": row["name"],
                    "section": row["section"],
                    "spanish": float(row["spanish"]),
                    "english": float(row["english"]),
                    "social": float(row["social"]),
                    "science": float(row["science"])
                }
                students.append(student)
        print("Imported successfully!")
    except:
        print("Error importing file.")
def menu():
    while True:
        print("\nMENU")
        print("1. Add students")
        print("2. Show students")
        print("3. Top 3")
        print("4. Overall average")
        print("5. Export CSV")
        print("6. Import CSV")
        print("7. Exit")
        option = input("Option: ")
        if option == "1":
            add_students()
        elif option == "2":
            show_students()
        elif option == "3":
            top_3()
        elif option == "4":
            overall_average()
        elif option == "5":
            export_csv()
        elif option == "6":
            import_csv()
        elif option == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option")
menu()
