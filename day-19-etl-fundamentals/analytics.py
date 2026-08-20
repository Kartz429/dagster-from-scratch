import csv

total_students = 0
total_marks = 0
highest_marks = 0
top_student = ""

with open("clean_students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        marks = int(row["marks"])

        total_students += 1
        total_marks += marks

        if marks > highest_marks:
            highest_marks = marks
            top_student = row["name"]

average_marks = total_marks / total_students

print("\n📊 Student Analytics Report")
print("-" * 30)

print(f"Total Students : {total_students}")
print(f"Average Marks  : {average_marks:.2f}")
print(f"Top Student    : {top_student}")
print(f"Highest Marks  : {highest_marks}")