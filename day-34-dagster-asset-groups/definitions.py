from dagster import Definitions

from assets import (
    raw_students,
    clean_students,
    average_marks,
    student_report
)

defs = Definitions(
    assets=[
        raw_students,
        clean_students,
        average_marks,
        student_report
    ]
)