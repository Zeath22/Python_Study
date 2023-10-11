# # basically we're trying to prevent wrong values
# class Student:
#     def __init__(self, name, age):
#         if not name:
#             raise ValueError("Missing Name")
#         if age < 18:
#             raise ValueError("Invalid Age")
#         self.name = name
#         self.age = age

#     # ? if we define our own str method in the class
#     # then whenever something wants the obj info as a string it will run rather than a memory placement number
#     def __str__(self):
#         return f"{self.name} is {self.age} years old."


# # now that we have created our own str method
# # the print wont bring back a memory place
# def main():
#     student = get_student()
#     print(student)


# def get_student():
#     name = input("name: ")
#     age = input("age: ")
#     return Student(name, age)


# # _______________________________________________________________________________________ # #
# we use getters and setters to prevent malicious access by making sure they go through our conditions
# we're only gonna do it for age
class Student:
    def __init__(self, name, age):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        # when python sees the self.age assignment it will trigger the setter
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    # ? getter
    # we have to put this @property before every getter to let python know
    # we have to place an underscore before the age name so python doesnt get confused
    @property
    def age(self):
        return self._age

    # ? setter
    # we have to put this @**.setter before to let python know
    # we have to place an underscore before the age name so python doesnt get confused
    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError("Invalid Age")
        self._age = age

# NOTE
# the reason we place an underscore in the getter and setter
# is not to trigger the setter because that's the trigger of the setter


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("name: ")
    age = input("age: ")
    return Student(name, age)


if __name__ == "__main__":
    main()
