class arguments:
    # *args passes variable number of non-keyworded arguments
    # and on which operation of the tuple can be performed.
    def multiplier(self, *numbers):
        total = 1
        for number in numbers:
            total *= number
        return total

    # **kwargs passes variable number of keyword arguments dictionary to function
    # on which operation of a dictionary can be performed.
    def save_user(self, **info):
        print(info)
        print(info["name"])
        return info


args1 = arguments()
# *args
print(args1.multiplier(1, 2, 3, 4, 5))

# **kwargs
userDict = args1.save_user(id=1, name="Adam", age=22)
print(userDict.get("id", "id"))
print(userDict.get("name", "Name"))
