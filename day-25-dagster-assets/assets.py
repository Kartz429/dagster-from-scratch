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

    clean_data = []

    for student in raw_students:

        student["name"] = student["name"].title()
        student["city"] = student["city"].title()

        clean_data.append(student)

    return clean_data


@asset
def student_report(clean_students):

    marks = [
        int(student["marks"])
        for student in clean_students
    ]

    total_students = len(clean_students)

    average_marks = (
        sum(marks) / total_students
    )

    highest_marks = max(marks)

    return {
        "total_students": total_students,
        "average_marks": round(
            average_marks,
            2
        ),
        "highest_marks": highest_marks
    }