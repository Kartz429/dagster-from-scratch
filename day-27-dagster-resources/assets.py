from dagster import asset


@asset
def raw_students(context):

    students = (
        context.resources.student_file
        .read_students()
    )

    return students


@asset
def student_count(raw_students):

    return len(raw_students)


@asset
def student_report(student_count):

    return (
        f"Total Students : {student_count}"
    )