class Point:
    # This is a constructor used for Automatic initialization
    # of objects at the time of their declaration
    # or It's used to give the class intial values
    # It is also a Magic Method
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # self is a reference to itself or to the current object
    def move(self):
        print("move")


point2 = Point(10, 20)
print(point2.x)
point2.x = 11
print(point2.x)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi my name is {self.name}")


John = Person("John Smith")
John.talk()
bob = Person("Bob Smith")
bob.talk()
