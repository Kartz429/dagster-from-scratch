from dagster import asset


@asset
def student_count():
    """
    Returns total number of students.
    """
    return 5


@asset
def average_marks():
    """
    Returns average marks.
    """
    return 87.4


@asset
def top_student():
    """
    Returns the name of the top student.
    """
    return "Kartik"


@asset
def student_report(
    student_count,
    average_marks,
    top_student
):
    """
    Generates a student report.
    """

    report = f"""
    STUDENT REPORT
    =========================
    Total Students : {student_count}
    Average Marks  : {average_marks}
    Top Student    : {top_student}
    """

    return report


@asset
def passed_students():
    """
    Returns passed students count.
    """
    return 4


@asset
def failed_students():
    """
    Returns failed students count.
    """
    return 1


@asset
def result_summary(
    passed_students,
    failed_students
):
    """
    Generates pass/fail summary.
    """

    summary = f"""
    RESULT SUMMARY
    =========================
    Passed Students : {passed_students}
    Failed Students : {failed_students}
    """

    return summary