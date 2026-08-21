from dagster import Definitions

from assets import (
    students,
    marks_validation
)

defs = Definitions(
    assets=[
        students
    ],
    asset_checks=[
        marks_validation
    ]
)