import csv

print("📦 Student ETL Pipeline")

clean_students = []

# EXTRACT
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        # TRANSFORM
        row["name"] = row["name"].title()
        row["city"] = row["city"].title()

        clean_students.append(row)

# LOAD
with open("clean_students.csv", "w", newline="") as file:

    fieldnames = ["name", "city", "marks"]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(clean_students)

print("✅ ETL Completed")