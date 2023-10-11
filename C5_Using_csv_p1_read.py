import csv

students = []

with open("student.csv") as file:
    # reader is way smarter from the split method
    reader = csv.DictReader(file)
    for row in reader:
        # this way it will read the headers of the column
        students.append({"name": row["name"], "house": row["house"]})
        # or just
        # students.append(row)

for student in students:
    print(f"{student['name']} is from {student['house']}.")
