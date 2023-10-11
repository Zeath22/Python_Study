# if we want to sort it a by a value like name or age
# we can use a list of dictionaries
students = []

with open("Names_age.csv") as file:
    for line in file:
        name, age = line.rstrip().split(",")
        # now we make the dictionary that will be appened into the list
        student = {"name": name, "age": age}
        students.append(student)

# we use the sorted function to sort it by using a key value, we give it the key through a function
# instead of a normal function, we give it a lambda (annonymous) function
# we say lambda your argument is student which is the iterable
# and in student you can find and RETURN the key (which sorted() uses to sort) is named 'name"
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is {student['age']} years old.")
