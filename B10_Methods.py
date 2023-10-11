# Classmethods come to the rescue by allowing you to define alternative constructors
# that provide a more intuitive way to initialize objects
class Point:
    def __init__(self, x, y):   # a magic method, these methods start and finish with 2 underscores
        self.x = x
        self.y = y

    @classmethod            # just a decorator
    def zero(cls):          # cls instead of self because it references the class
        return cls(0, 0)

    def draw(self):
        print(f"Point is {self.x} and {self.y}")

    def __str__(self):      # a magic method
        return f"{self.x} {self.y}"


poi = Point.zero()  # we didn't create an object for it
poi.draw()
print(poi.__str__())
