import sqlite3

connection = sqlite3.connect(
    "student_warehouse.db"
)

cursor = connection.cursor()

cursor.execute("""
SELECT COUNT(*)
FROM students
""")

total_students = cursor.fetchone()[0]

cursor.execute("""
SELECT AVG(marks)
FROM students
""")

average_marks = cursor.fetchone()[0]

cursor.execute("""
SELECT MAX(marks)
FROM students
""")

highest_marks = cursor.fetchone()[0]

print("\n📊 Warehouse Analytics")
print("-" * 30)

print(f"Total Students : {total_students}")
print(f"Average Marks  : {average_marks:.2f}")
print(f"Highest Marks  : {highest_marks}")

connection.close()