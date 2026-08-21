from dagster import Definitions

from assets import (
    raw_students,
    load_to_duckdb,
    analytics_report
)

defs = Definitions(
    assets=[
        raw_students,
        load_to_duckdb,
        analytics_report
    ]
)