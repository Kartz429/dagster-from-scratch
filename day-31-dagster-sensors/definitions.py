from dagster import (
    Definitions,
    define_asset_job
)

from assets import (
    student_report
)

from sensors import (
    student_file_sensor
)

student_report_job = define_asset_job(
    "student_report_job"
)

defs = Definitions(
    assets=[
        student_report
    ],

    jobs=[
        student_report_job
    ],

    sensors=[
        student_file_sensor
    ]
)