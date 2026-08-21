from dagster import (
    asset,
    asset_check,
    AssetCheckResult
)


@asset
def students():

    return [
        {
            "name": "Kartik",
            "marks": 95
        },
        {
            "name": "Rahul",
            "marks": 88
        },
        {
            "name": "Priya",
            "marks": 91
        }
    ]


@asset_check(asset=students)
def marks_validation(students):

    valid = all(
        0 <= student["marks"] <= 100
        for student in students
    )

    return AssetCheckResult(
        passed=valid
    )