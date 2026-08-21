import csv
import duckdb

from dagster import asset


@asset
def raw_students():

    students = []

    with open("students.csv", "r") as file:

        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

    return students


@asset
def student_warehouse(raw_students):

    connection = duckdb.connect(
        "student_warehouse.duckdb"
    )

    connection.execute("""
    CREATE TABLE IF NOT EXISTS students(
        name VARCHAR,
        city VARCHAR,
        marks INTEGER
    )
    """)

    connection.execute(
        "DELETE FROM students"
    )

    for student in raw_students:

        connection.execute(
            """
            INSERT INTO students
            VALUES (?, ?, ?)
            """,
            (
                student["name"],
                student["city"],
                int(student["marks"])
            )
        )

    connection.close()

    return "Warehouse Updated"


@asset
def analytics_metrics(student_warehouse):

    connection = duckdb.connect(
        "student_warehouse.duckdb"
    )

    total_students = connection.execute(
        "SELECT COUNT(*) FROM students"
    ).fetchone()[0]

    average_marks = connection.execute(
        "SELECT AVG(marks) FROM students"
    ).fetchone()[0]

    highest_marks = connection.execute(
        "SELECT MAX(marks) FROM students"
    ).fetchone()[0]

    lowest_marks = connection.execute(
        "SELECT MIN(marks) FROM students"
    ).fetchone()[0]

    passed_students = connection.execute(
        """
        SELECT COUNT(*)
        FROM students
        WHERE marks >= 40
        """
    ).fetchone()[0]

    connection.close()

    return {
        "total_students": total_students,
        "average_marks": round(
            average_marks,
            2
        ),
        "highest_marks": highest_marks,
        "lowest_marks": lowest_marks,
        "passed_students": passed_students
    }


@asset
def dashboard_report(analytics_metrics):

    report = f"""
STUDENT DASHBOARD
========================

Total Students : {analytics_metrics['total_students']}
Average Marks  : {analytics_metrics['average_marks']}
Highest Marks  : {analytics_metrics['highest_marks']}
Lowest Marks   : {analytics_metrics['lowest_marks']}
Passed Students: {analytics_metrics['passed_students']}
"""

    with open(
        "dashboard_report.txt",
        "w"
    ) as file:

        file.write(report)

    return report