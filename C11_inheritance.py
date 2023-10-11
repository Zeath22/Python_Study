# lets say we have a bunch of classes that share some common ground
# it is wrong and redundent to write same code for both
# so We make a greater class that holds that common code and lets them borrow
# such as a student and a teacher, they both have names
# so we just error check once in the parent class
class Person:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name!")
        self.name = name


# by putting the Person in parenthesis we tell Student/Teacher to inherit from it
class Student(Person):
    def __init__(self, name, department):
        # to ACCESS the functionalities in the parent we use the keyword super
        # afetr we have access We call the function __init__ to pass the name
        super().__init__(name)
        self.department = department


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


# ? overriding
# class Animal:
#     def speak(self):
#         return "An animal speaks"

# class Dog(Animal):
#     def speak(self):  # This method overrides the speak method of the Animal class
#         return "A dog barks"

# class Cat(Animal):
#     def speak(self):  # This method overrides the speak method of the Animal class
#         return "A cat meows"
