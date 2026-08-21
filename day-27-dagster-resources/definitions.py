from dagster import Definitions

from assets import (
    raw_students,
    student_count,
    student_report
)

from resources import (
    StudentFileResource
)

defs = Definitions(
    assets=[
        raw_students,
        student_count,
        student_report
    ],
    resources={
        "student_file":
        StudentFileResource()
    }
)