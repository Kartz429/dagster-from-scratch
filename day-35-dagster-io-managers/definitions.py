from dagster import (
    Definitions
)

from assets import (
    student_report
)

from io_manager import (
    FileIOManager
)

defs = Definitions(
    assets=[
        student_report
    ],

    resources={
        "io_manager":
        FileIOManager()
    }
)
