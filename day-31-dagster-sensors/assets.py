from dagster import asset


@asset
def student_report():

    return "Student Report Generated"