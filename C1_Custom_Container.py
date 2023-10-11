# We can make our own container class like lists and dictionaries
# we can customize our container with the magic methods
class TagDict:
    def __init__(self):
        self.__tags = {}

    # this will get the value if the key exists in the dict
    # if it doesn't exist, it will make one
    # now we add our custom additions to it like recognizing lower and capital letters
    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    # now we can get the value of the called key just by the name of it
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    # now we can new keys and values instantly
    def __setitem__(self, key, count):
        self.__tags[key.lower()] = count

    # to be able to return the length
    def __len__(self):
        return len(self.__tags)
    # now we can iterate through our container

    def __iter__(self):
        return iter(self.__tags)


tagName = TagDict()
tagName.add("python")
tagName.add("python")
tagName.add("PyThoN")
# this is how we use the set item method
tagName["java"] = 10

print(tagName.__tags)
