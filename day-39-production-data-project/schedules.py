from dagster import ScheduleDefinition

daily_student_schedule = ScheduleDefinition(
    job_name="student_pipeline_job",
    cron_schedule="0 6 * * *"
)
