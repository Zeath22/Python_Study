# # what we're doing is creating more functional or more structural programming
# # by creating building blocks
# def main():
#     name = get_name()
#     age = get_age()
#     print(f"{name} is {age} years old.")

# # we are making building blocks that we can reuse
# def get_name():
#     return input("name: ")


# def get_age():
#     return input("age: ")


# # _______________________________________________________________________________________ # #
# # what we really wanna do is return the student
# def main():
#     student = get_student()
#     print(f"{student[0]} is {student[1]} years old.")


# # we return a tuple
# def get_student():
#     name = input("name: ")
#     age = input("age: ")
#     return (name, age)


# # _______________________________________________________________________________________ # #
# we're creating a class which allows basically to create our own data type called student
# we can just leave it with a triple dots ...
# class Student:
#     ...


# def main():
#     student = get_student()
#     print(f"{student.name} is {student.age} years old.")


# # now we make an object from that class and give it attributes such as name and age
# # objects = instances ______________ attributes = instance variables
# def get_student():
#     student1 = Student()
#     student1.name = input("name: ")
#     student1.age = input("age: ")
#     return student1


# # _______________________________________________________________________________________ # #
# we are making an initializing function or a constructor for our objects
# self tells the program that this is the object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def main():
    student = get_student()
    print(f"{student.name} is {student.age} years old.")


# we dont that much code and we can pass the attriutes as arguments through the class
def get_student():
    name = input("name: ")
    age = input("age: ")
    return Student(name, age)


if __name__ == "__main__":
    main()
