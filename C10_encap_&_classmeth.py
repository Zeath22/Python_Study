# class Student:
#     def __init__(self, name, age):
#         if not name:
#             raise ValueError("Missing Name")
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old."


# def main():
#     student = get_student()
#     print(student)

# # this is considered out of place and it should be inside the class so we encapsulated everything
# # so we remove it and make it a class method
# def get_student():
#     name = input("name: ")
#     age = input("age: ")
#     return Student(name, age)

# # _______________________________________________________________________________________ # #
class Student:
    def __init__(self, name, age):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    # by doing this we can call this methof without making an object first
    @classmethod
    def get(cls):
        name = input("name: ")
        age = input("age: ")
        # this will return a new student object
        return cls(name, age)


def main():
    # by saying the class and get function we have integrated/migrated everything in the class into the obj
    student = Student.get()
    print(student)

# NOTE now we have everything encapsulated


if __name__ == "__main__":
    main()
