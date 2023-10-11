# class is a blueprint for creating objects
# objects are an instance of a class
class Point:
    def move(self):
        print("move")

    # if a second a value is not passed, it will default
    # and all optional parameters must come after the required parameters
    def incrementWithDefault(self, fisrt, second=1):
        return fisrt+second


point1 = Point()
point1.move()
point1.x = 10   # not a good way to do it, look at constuctors.py
print(point1.x)


print(point1.incrementWithDefault(2))
print(point1.incrementWithDefault(2, 2))
