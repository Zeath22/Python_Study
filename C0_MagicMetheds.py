# Magic Methods are predifined and They start and end with underscores __ __
# These methods provide a way to define how objects of a class behave
# with respect to various operations,
# such as arithmetic operations, comparison, string representation, and more.
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = Point(0, 1)
p2 = Point(0, 1)
# normally if we didn't customize our comparison method it would give false
print(p1 == p2)
# we customized our comparison operator, That's crazy

p1 = Point(4, 5)
p2 = Point(3, 1)
p3 = p1 + p2
print(str(p3))
