import csv
import duckdb

from dagster import (
    asset,
    asset_check,
    AssetCheckResult,
    MaterializeResult
)


@asset(group_name="students")
def raw_students():

    students = []

    with open("students.csv", "r") as file:

        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

    return students


@asset(group_name="students")
def clean_students(raw_students):

    cleaned_students = []

    for student in raw_students:

        cleaned_students.append(
            {
                "name": student["name"].title(),
                "city": student["city"].title(),
                "marks": int(student["marks"])
            }
        )

    return cleaned_students


@asset_check(asset=clean_students)
def marks_validation(clean_students):

    valid = all(
        0 <= student["marks"] <= 100
        for student in clean_students
    )

    return AssetCheckResult(
        passed=valid
    )


@asset(group_name="warehouse")
def warehouse_students(clean_students):

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

    for student in clean_students:

        connection.execute(
            """
            INSERT INTO students
            VALUES (?, ?, ?)
            """,
            (
                student["name"],
                student["city"],
                student["marks"]
            )
        )

    connection.close()

    return "Warehouse Loaded"


@asset(group_name="analytics")
def analytics_dashboard(
    warehouse_students
):

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

    top_student = connection.execute(
        """
        SELECT name
        FROM students
        ORDER BY marks DESC
        LIMIT 1
        """
    ).fetchone()[0]

    connection.close()

    return MaterializeResult(
        value={
            "total_students":
            total_students,

            "average_marks":
            round(average_marks, 2),

            "highest_marks":
            highest_marks,

            "lowest_marks":
            lowest_marks,

            "top_student":
            top_student
        },

        metadata={
            "total_students":
            total_students,

            "top_student":
            top_student
        }
    )


@asset(group_name="reports")
def dashboard_report(
    analytics_dashboard
):

    report = f"""
STUDENT ANALYTICS DASHBOARD
===========================

Total Students : {analytics_dashboard['total_students']}
Average Marks  : {analytics_dashboard['average_marks']}
Highest Marks  : {analytics_dashboard['highest_marks']}
Lowest Marks   : {analytics_dashboard['lowest_marks']}
Top Student    : {analytics_dashboard['top_student']}
"""

    with open(
        "dashboard_report.txt",
        "w"
    ) as file:

        file.write(report)

    return report