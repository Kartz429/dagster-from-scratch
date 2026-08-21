import csv
import sqlite3

connection = sqlite3.connect(
    "student_warehouse.db"
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    name TEXT,
    city TEXT,
    marks INTEGER
)
""")

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        cursor.execute("""
        INSERT INTO students
        VALUES (?, ?, ?)
        """, (
            row["name"],
            row["city"],
            row["marks"]
        ))

connection.commit()

print("✅ Data Loaded Into Warehouse")

connection.close()