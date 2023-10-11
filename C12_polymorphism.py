# suppose we want to change/alter the way a made function works
# we can overload that function, like the addition operator +
# we can overload how it works

# let's say there is a man and his wife, They want to buy a house
# they want to combine fortunes that are made from gold, silver and bronze

class Bank:
    def __init__(self, gold=0, silver=0, bronze=0):
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def __str__(self):
        return f"{self.gold} gold, {self.silver} silver and {self.bronze} bronze."

    # we cant add the banks together because addition doesnt work that way
    # so we overloadiing it, we have method overloading and operator overloading, this is the latter
    # self is always the left operand and other is the right operand
    def __add__(self, other):
        gold = self.gold + other.gold
        silver = self.silver + other.silver
        bronze = self.bronze + other.bronze
        return Bank(gold, silver, bronze)


man = Bank(100, 50, 25)
print(man)
woman = Bank(25, 50, 100)
print(woman)

total = man + woman
print(total)


# NOTE
# Polymorphism, enables more generic and reusable code
# by allowing objects or methods to be used in multiple forms.
# This facilitates a clean and DRY (Don’t Repeat Yourself) codebase,
# promoting efficient and maintainable software design.
