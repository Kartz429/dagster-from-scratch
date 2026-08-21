from dagster import IOManager


class ReportIOManager(IOManager):

    def handle_output(
        self,
        context,
        obj
    ):

        with open(
            "report.txt",
            "w"
        ) as file:

            file.write(str(obj))

    def load_input(
        self,
        context
    ):

        return None