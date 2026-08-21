from dagster import Definitions

from assets import (
    student_report
)

defs = Definitions(
    assets=[
        student_report
    ]
)