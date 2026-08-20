import csv

valid_students = []
invalid_students = []

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        row["name"] = row["name"].title()
        row["city"] = row["city"].title()

        marks = int(row["marks"])

        if 0 <= marks <= 100:
            valid_students.append(row)
        else:
            invalid_students.append(row)

with open("valid_students.csv", "w", newline="") as file:

    fieldnames = ["name", "city", "marks"]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(valid_students)

with open("invalid_students.csv", "w", newline="") as file:

    fieldnames = ["name", "city", "marks"]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(invalid_students)

print("✅ Data Validation Complete")