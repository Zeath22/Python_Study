try:
    Age = int(input(">"))
    income = 2000
    risk = income / Age
    print(Age, " ", risk)
    print("connection opened")
except ZeroDivisionError:
    print("cant divide by zero")
except ValueError as ex:            # we can also name the error and print it
    print("invalid input")
    print(ex)
except (KeyError, RecursionError):
    print("invalid input")          # we can have multiple exception cases
else:
    print("IF there are no exeptions thrown, Now run this code")
finally:           # this will run always at the end, used for closing files and connections
    print("connection closed")
