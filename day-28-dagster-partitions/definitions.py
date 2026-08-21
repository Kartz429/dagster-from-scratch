from dagster import Definitions

from assets import (
    daily_sales,
    sales_report
)

defs = Definitions(
    assets=[
        daily_sales,
        sales_report
    ]
)