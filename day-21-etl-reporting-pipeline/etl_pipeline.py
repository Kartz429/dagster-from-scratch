import csv

clean_students = []

# Extract
with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        # Transform
        row["name"] = row["name"].title()
        row["city"] = row["city"].title()

        clean_students.append(row)

# Load
with open("clean_students.csv", "w", newline="") as file:

    fieldnames = ["name", "city", "marks"]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(clean_students)

print("✅ clean_students.csv generated")