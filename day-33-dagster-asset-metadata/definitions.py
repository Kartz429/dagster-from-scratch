from dagster import Definitions

from assets import students

defs = Definitions(
    assets=[
        students
    ]
)