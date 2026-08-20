import csv

students = [
    ["name", "city", "marks"],
    ["kartik", "mumbai", 95],
    ["rahul", "pune", 110],
    ["priya", "delhi", 91],
    ["amit", "bangalore", -5],
    ["neha", "chennai", 85]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("✅ students.csv created")