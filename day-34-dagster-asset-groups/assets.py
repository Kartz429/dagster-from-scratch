from dagster import asset


@asset(group_name="students")
def raw_students():

    return [
        {"name": "Kartik", "marks": 95},
        {"name": "Rahul", "marks": 88}
    ]


@asset(group_name="students")
def clean_students(raw_students):

    return raw_students


@asset(group_name="analytics")
def average_marks(clean_students):

    marks = [
        student["marks"]
        for student in clean_students
    ]

    return (
        sum(marks) / len(marks)
    )


@asset(group_name="reports")
def student_report(
    average_marks
):

    return (
        f"Average Marks: "
        f"{average_marks}"
    )