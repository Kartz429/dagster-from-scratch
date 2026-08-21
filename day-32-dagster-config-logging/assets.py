from dagster import (
    asset,
    Config
)


class StudentConfig(Config):

    report_name: str


@asset
def student_report(
    context,
    config: StudentConfig
):

    context.log.info(
        "Generating student report..."
    )

    report = (
        f"{config.report_name} Generated"
    )

    context.log.info(
        "Report generated successfully."
    )

    return report