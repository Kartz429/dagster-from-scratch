from dagster import Definitions

from assets import (
    raw_students,
    student_warehouse,
    analytics_metrics,
    dashboard_report
)

defs = Definitions(
    assets=[
        raw_students,
        student_warehouse,
        analytics_metrics,
        dashboard_report
    ]
)