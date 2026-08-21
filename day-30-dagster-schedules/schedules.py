from dagster import ScheduleDefinition

daily_report_schedule = ScheduleDefinition(
    job_name="daily_report_job",

    cron_schedule="0 6 * * *"
)