import random


###########
total_grades = int(input("How many grades will you enter? "))
approved_count = 0
failed_count = 0
sum_all = 0
sum_approved = 0
sum_failed = 0
for i in range(total_grades):
    grade = float(input("Enter grade: "))
    sum_all += grade
    if grade >= 70:
        approved_count += 1
        sum_approved += grade
    else:
        failed_count += 1
        sum_failed += grade
average_all = sum_all / total_grades
if approved_count > 0:
    average_approved = sum_approved / approved_count
else:
    average_approved = 0
if failed_count > 0:
    average_failed = sum_failed / failed_count
else:
    average_failed = 0
print("Approved grades:", approved_count)
print("Failed grades:", failed_count)
print("Average of all grades:", average_all)
print("Average of approved grades:", average_approved)
print("Average of failed grades:", average_failed)
