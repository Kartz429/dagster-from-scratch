from dagster import asset


@asset
def daily_report():

    return "Daily Report Generated"