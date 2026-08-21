import os

from dagster import (
    sensor,
    RunRequest
)


@sensor(
    job_name="student_pipeline_job"
)
def student_file_sensor():

    if os.path.exists(
        "students.csv"
    ):

        yield RunRequest(
            run_key="student-file"
        )