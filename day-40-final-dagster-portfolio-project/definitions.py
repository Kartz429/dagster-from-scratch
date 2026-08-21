from dagster import (
    Definitions,
    define_asset_job
)

from assets import (
    raw_students,
    clean_students,
    warehouse_students,
    analytics_dashboard,
    dashboard_report,
    marks_validation
)

from schedules import (
    daily_student_schedule
)

from sensors import (
    student_file_sensor
)

student_pipeline_job = define_asset_job(
    "student_pipeline_job"
)

defs = Definitions(
    assets=[
        raw_students,
        clean_students,
        warehouse_students,
        analytics_dashboard,
        dashboard_report
    ],

    asset_checks=[
        marks_validation
    ],

    jobs=[
        student_pipeline_job
    ],

    schedules=[
        daily_student_schedule
    ],

    sensors=[
        student_file_sensor
    ]
)