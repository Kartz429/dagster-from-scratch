import csv


class StudentFileResource:

    def read_students(self):

        students = []

        with open("students.csv", "r") as file:

            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

        return students
        