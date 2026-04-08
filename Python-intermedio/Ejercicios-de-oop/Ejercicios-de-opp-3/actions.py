import re
from student import Student


def get_int(message):
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            else:
                print("The number must be greater than 0.")
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


def is_valid_name(name):
    if name.strip() == "":
        return False

    for char in name:
        if char.isdigit():
            return False

    return True


def is_valid_section(section):
    pattern = r"^\d{1,2}[A-Za-z]$"
    return re.match(pattern, section) is not None


def student_exists(students, name, section):
    for student in students:
        if student.name.lower() == name.lower() and student.section.upper() == section.upper():
            return True
    return False


def add_students(students):
    n = get_int("How many students? ")

    for i in range(n):
        print("\nStudent", i + 1)

        while True:
            name = input("Name: ").strip()
            if is_valid_name(name):
                break
            else:
                print("Invalid name. It cannot be empty or contain numbers.")

        while True:
            section = input("Section: ").strip().upper()
            if is_valid_section(section):
                break
            else:
                print("Invalid section. Use format like 10A, 11B, 9C.")

        if student_exists(students, name, section):
            print("This student already exists. Duplicate students are not allowed.")
            continue

        spanish = get_grade("Spanish: ")
        english = get_grade("English: ")
        social = get_grade("Social Studies: ")
        science = get_grade("Science: ")

        student = Student(name, section, spanish, english, social, science)
        students.append(student)

        print("Student added successfully.")


def show_students(students):
    if len(students) == 0:
        print("No students.")
        return

    for student in students:
        print("\nName:", student.name)
        print("Section:", student.section)
        print("Spanish:", student.spanish)
        print("English:", student.english)
        print("Social Studies:", student.social)
        print("Science:", student.science)
        print("Average:", round(student.calculate_average(), 2))


def top_3(students):
    if len(students) == 0:
        print("No students.")
        return

    sorted_list = sorted(students, key=lambda student: student.calculate_average(), reverse=True)

    print("\nTop 3:")
    for i in range(min(3, len(sorted_list))):
        student = sorted_list[i]
        print(i + 1, "-", student.name, "-", student.section, "-", round(student.calculate_average(), 2))


def overall_average(students):
    if len(students) == 0:
        print("No students.")
        return

    total = 0

    for student in students:
        total += student.calculate_average()

    print("Overall average:", round(total / len(students), 2))


def delete_student(students):
    if len(students) == 0:
        print("No students.")
        return

    name = input("Enter the student's name: ").strip()
    section = input("Enter the student's section: ").strip().upper()

    found_student = None

    for student in students:
        if student.name.lower() == name.lower() and student.section.upper() == section.upper():
            found_student = student
            break

    if found_student is None:
        print("Student not found.")
        return

    print("\nStudent found:")
    print("Name:", found_student.name)
    print("Section:", found_student.section)

    confirm = input("Are you sure you want to delete this student? (yes/no): ").strip().lower()

    if confirm == "yes":
        students.remove(found_student)
        print("Student deleted successfully.")
    else:
        print("Deletion cancelled.")


def show_failed_students(students):
    if len(students) == 0:
        print("No students.")
        return

    found_failed = False

    for student in students:
        failed_subjects = student.get_failed_subjects()

        if len(failed_subjects) > 0:
            found_failed = True
            print("\nName:", student.name)
            print("Section:", student.section)
            print("Failed subjects:")

            for subject, grade in failed_subjects:
                print("-", subject, ":", grade)

    if not found_failed:
        print("There are no failed students.")
