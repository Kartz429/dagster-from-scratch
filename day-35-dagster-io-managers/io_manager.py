from dagster import IOManager


class FileIOManager(IOManager):

    def handle_output(
        self,
        context,
        obj
    ):

        with open(
            "output.txt",
            "w"
        ) as file:

            file.write(str(obj))

    def load_input(
        self,
        context
    ):

        with open(
            "output.txt",
            "r"
        ) as file:

            return file.read()