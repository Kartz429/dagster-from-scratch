from dagster import (
    Definitions,
    define_asset_job,
)

from assets import (
    raw_students,
    clean_students,
    student_report,
)

student_pipeline_job = define_asset_job(
    name="student_pipeline_job"
)

defs = Definitions(
    assets=[
        raw_students,
        clean_students,
        student_report,
    ],
    jobs=[
        student_pipeline_job
    ]
)