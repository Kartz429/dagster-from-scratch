import csv

students = []

# Read cleaned data
with open("clean_students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append(row)

# Analytics
marks = [int(student["marks"]) for student in students]

total_students = len(students)
average_marks = sum(marks) / total_students
highest_marks = max(marks)
lowest_marks = min(marks)

top_student = ""

for student in students:
    if int(student["marks"]) == highest_marks:
        top_student = student["name"]

# Display Analytics
print("\n📊 Analytics Generated")
print("-" * 30)

print(f"Total Students : {total_students}")
print(f"Average Marks  : {average_marks:.2f}")
print(f"Highest Marks  : {highest_marks}")
print(f"Lowest Marks   : {lowest_marks}")
print(f"Top Student    : {top_student}")

# Generate Report
with open("report.txt", "w") as report:

    report.write("STUDENT REPORT\n")
    report.write("=" * 30 + "\n")

    report.write(
        f"Total Students : {total_students}\n"
    )

    report.write(
        f"Average Marks : {average_marks:.2f}\n"
    )

    report.write(
        f"Highest Marks : {highest_marks}\n"
    )

    report.write(
        f"Lowest Marks : {lowest_marks}\n"
    )

    report.write(
        f"Top Student : {top_student}\n"
    )

print("\n✅ report.txt generated successfully")