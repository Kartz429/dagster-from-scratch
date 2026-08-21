from dagster import (
    asset,
    asset_check,
    AssetCheckResult,
    MaterializeResult
)


@asset(group_name="students")
def raw_students(context):

    students = (
        context.resources.student_file
        .read_students()
    )

    return students


@asset(group_name="students")
def clean_students(raw_students):

    cleaned = []

    for student in raw_students:

        student["name"] = (
            student["name"].title()
        )

        student["city"] = (
            student["city"].title()
        )

        cleaned.append(student)

    return cleaned


@asset_check(asset=clean_students)
def marks_validation(
    clean_students
):

    valid = all(
        0 <= int(student["marks"]) <= 100
        for student in clean_students
    )

    return AssetCheckResult(
        passed=valid
    )


@asset(group_name="analytics")
def student_metrics(
    clean_students
):

    marks = [
        int(student["marks"])
        for student in clean_students
    ]

    return MaterializeResult(
        value={
            "total_students":
            len(clean_students),

            "average_marks":
            round(
                sum(marks) / len(marks),
                2
            ),

            "highest_marks":
            max(marks)
        },

        metadata={
            "record_count":
            len(clean_students),

            "highest_marks":
            max(marks)
        }
    )


@asset(
    group_name="reports",
    io_manager_key="report_io_manager"
)
def student_report(
    student_metrics
):

    report = f"""
STUDENT REPORT
========================

Total Students : {student_metrics['total_students']}
Average Marks  : {student_metrics['average_marks']}
Highest Marks  : {student_metrics['highest_marks']}
"""

    return report