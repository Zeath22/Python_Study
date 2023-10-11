# we can make our own library and use the code in it
# using a main function in Python is a best practice for structuring your code,
# improving readability, and promoting reusability while also helping with testing
def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello {name}")


def goodbye(name):
    print(f"Goodbye {name}")


# The if __name__ == "__main__": block ensures that the main function is
# only executed when the script is run as the main program,
# and not when it's imported as a module into another script
if __name__ == "__main__":
    main()
