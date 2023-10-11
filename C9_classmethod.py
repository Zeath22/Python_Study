# in the world of harry potter There is a hat that sorts the students to their houses
# but there's only 1 hat, the hat is not bound to any object
# he is his own entity, so we can only have 1 one hat, not a hat for every object created
import random


class Hat:
    # we didnt make the __init__ function because it contains self which bounds stuff to the object
    # any function made is automatically assigned to objects but when we make one for the class
    # we have to write the decorator
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # we have this decorator that tells python this is a class method
    # we pass through cls as a reference to the class, so whatever the class contains there's access
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
