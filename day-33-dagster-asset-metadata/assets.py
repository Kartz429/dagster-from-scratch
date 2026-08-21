from dagster import (
    asset,
    MaterializeResult,
    MetadataValue
)


@asset
def students():

    data = [
        {"name": "Kartik", "marks": 95},
        {"name": "Rahul", "marks": 88},
        {"name": "Priya", "marks": 91}
    ]

    return MaterializeResult(
        value=data,

        metadata={
            "record_count": len(data),

            "source_file":
            MetadataValue.text(
                "students.csv"
            ),

            "highest_marks":
            max(
                student["marks"]
                for student in data
            )
        }
    )