from dagster import (
    asset,
    DailyPartitionsDefinition
)

# Create daily partitions

daily_partitions = DailyPartitionsDefinition(
    start_date="2026-08-01"
)


@asset(
    partitions_def=daily_partitions
)
def daily_sales(context):

    partition_date = context.partition_key

    return {
        "date": partition_date,
        "sales": 5000
    }


@asset(
    partitions_def=daily_partitions
)
def sales_report(daily_sales):

    return (
        f"Report Generated For "
        f"{daily_sales['date']} "
        f"with sales ₹{daily_sales['sales']}"
    )