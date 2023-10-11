# our classes have objects
# our objects have atributes
# like a john(obj) is a person(class) who has a name(Atr)
# we have 2 types of Atributes: class and instance(obj) Atributes
class Point:
    default_point_color = "black"     # a class wide atribute

    def __init__(self, x, y):
        self.x = x
        self.y = y


first = Point(1, 2)
print(first.default_point_color)

# changing the class will change every obj unless
Point.default_point_color = "red"
print(Point.default_point_color)
print(first.default_point_color)

# if you change the obj is set to custom color
first.default_point_color = "yellow"
print(first.default_point_color)
