from dagster import Definitions

from first_asset import (
    student_count,
    average_marks,
    top_student,
    student_report,
    passed_students,
    failed_students,
    result_summary
)

defs = Definitions(
    assets=[
        student_count,
        average_marks,
        top_student,
        student_report,
        passed_students,
        failed_students,
        result_summary
    ]
)