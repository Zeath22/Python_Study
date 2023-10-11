import csv

name = input("name? ")
city = input("from? ")

with open("student.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, city])
    # or we can use dictwriter which then by utilizing fieldnames the order wont matter
    # writer = csv.DictWriter(file, fieldnames=["name", "city"])
    # writer.writerow({"name": name, "city": city})
