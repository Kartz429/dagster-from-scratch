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
def load_to_duckdb(raw_students):

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

    return "Data Loaded Successfully"


@asset
def analytics_report(load_to_duckdb):

    connection = duckdb.connect(
        "student_warehouse.duckdb"
    )

    total_students = connection.execute(
        """
        SELECT COUNT(*)
        FROM students
        """
    ).fetchone()[0]

    average_marks = connection.execute(
        """
        SELECT AVG(marks)
        FROM students
        """
    ).fetchone()[0]

    highest_marks = connection.execute(
        """
        SELECT MAX(marks)
        FROM students
        """
    )