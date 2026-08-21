from dagster import (
    Definitions,
    define_asset_job
)

from assets import (
    raw_students,
    clean_students,
    student_metrics,
    student_report,
    marks_validation
)

from resources import (
    StudentFileResource
)

from io_manager import (
    ReportIOManager
)

student_etl_job = define_asset_job(
    "student_etl_job"
)

defs = Definitions(
    assets=[
        raw_students,
        clean_students,
        student_metrics,
        student_report
    ],

    asset_checks=[
        marks_validation
    ],

    jobs=[
        student_etl_job
    ],

    resources={
        "student_file":
        StudentFileResource(),

        "report_io_manager":
        ReportIOManager()
    }
)