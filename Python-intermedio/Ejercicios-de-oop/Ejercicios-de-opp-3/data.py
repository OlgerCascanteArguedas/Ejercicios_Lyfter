import csv
import os
from student import Student
from actions import student_exists

FILE = "students.csv"


def export_csv(students):
    if len(students) == 0:
        print("No data to export.")
        return

    try:
        with open(FILE, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "section", "spanish", "english", "social", "science"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for student in students:
                writer.writerow(student.to_dict())

        print("Data exported successfully.")
    except:
        print("Error exporting file.")


def import_csv(students):
    if not os.path.exists(FILE):
        print("No previously exported file was found.")
        return

    try:
        imported_count = 0
        skipped_count = 0

        with open(FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row["name"].strip()
                section = row["section"].strip().upper()

                if student_exists(students, name, section):
                    skipped_count += 1
                    continue

                student = Student(
                    name,
                    section,
                    float(row["spanish"]),
                    float(row["english"]),
                    float(row["social"]),
                    float(row["science"])
                )

                students.append(student)
                imported_count += 1

        print("Imported:", imported_count)
        print("Skipped duplicates:", skipped_count)

    except:
        print("Error importing file.")
