# when we create our own functions, we might need to raise some exceptions
def calculate(age):
    if age <= 0:
        raise ValueError("age is not valid")
    return 10/age


try:
    calculate(0)
except ValueError as ex:
    print(ex)
