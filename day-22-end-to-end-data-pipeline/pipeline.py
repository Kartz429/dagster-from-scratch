import csv

valid_students = []
invalid_students = []

# Extract

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        marks = int(row["marks"])

        # Validation

        if 0 <= marks <= 100:

            row["name"] = row["name"].title()
            row["city"] = row["city"].title()

            valid_students.append(row)

        else:
            invalid_students.append(row)

# Load Clean Data

with open("clean_students.csv", "w", newline="") as file:

    fieldnames = ["name", "city", "marks"]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(valid_students)

# Top Students

top_students = []

for student in valid_students:

    if int(student["marks"]) >= 90:
        top_students.append(student)

with open("top_students.csv", "w", newline="") as file:

    fieldnames = ["name", "city", "marks"]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(top_students)

# Analytics

marks_list = [
    int(student["marks"])
    for student in valid_students
]

total_students = len(valid_students)

average_marks = sum(marks_list) / total_students

highest_marks = max(marks_list)

# Report

with open("report.txt", "w") as report:

    report.write("STUDENT DATA PIPELINE REPORT\n")
    report.write("=" * 35 + "\n")

    report.write(
        f"Valid Students : {len(valid_students)}\n"
    )

    report.write(
        f"Invalid Students : {len(invalid_students)}\n"
    )

    report.write(
        f"Average Marks : {average_marks:.2f}\n"
    )

    report.write(
        f"Highest Marks : {highest_marks}\n"
    )

    report.write(
        f"Top Students : {len(top_students)}\n"
    )

print("✅ Pipeline Executed Successfully")