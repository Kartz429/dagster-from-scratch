import csv

total_students = 0
total_marks = 0

with open("valid_students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        total_students += 1
        total_marks += int(row["marks"])

average_marks = total_marks / total_students

print("\n📊 Validation Report")
print("-" * 30)

print(f"Valid Students   : {total_students}")
print(f"Average Marks    : {average_marks:.2f}")