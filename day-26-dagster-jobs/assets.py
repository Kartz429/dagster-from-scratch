import csv

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
def clean_students(raw_students):

    cleaned_students = []

    for student in raw_students:

        student["name"] = student["name"].title()
        student["city"] = student["city"].title()

        cleaned_students.append(student)

    return cleaned_students


@asset
def student_report(clean_students):

    marks = [
        int(student["marks"])
        for student in clean_students
    ]

    return {
        "total_students": len(clean_students),
        "average_marks": round(
            sum(marks) / len(marks),
            2
        ),
        "highest_marks": max(marks),
    }