import csv

students = [
    ["name", "city", "marks"],
    ["Kartik", "Mumbai", 95],
    ["Rahul", "Pune", 88],
    ["Priya", "Delhi", 91],
    ["Neha", "Chennai", 85]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("✅ students.csv created")