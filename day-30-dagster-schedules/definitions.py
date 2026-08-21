from dagster import (
    Definitions,
    define_asset_job
)

from assets import (
    daily_report
)

from schedules import (
    daily_report_schedule
)

daily_report_job = define_asset_job(
    "daily_report_job"
)

defs = Definitions(
    assets=[
        daily_report
    ],

    jobs=[
        daily_report_job
    ],

    schedules=[
        daily_report_schedule
    ]
)