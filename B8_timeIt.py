# we use timeit to see how long it will take to run our code
from timeit import timeit

code1 = """
def calculate(age):
    if age <= 0:
        raise ValueError("age is not valid")
    return 10/age


try:
    calculate(0)
except ValueError as ex:
    pass
"""
# you can always avoid raising exceptions, it will make your code way faster
code2 = """
def calculate(age):
    if age <= 0:
        return None
    return 10/age


xfactor = calculate(0)
if xfactor == None:
    pass
"""

print("raising exception code time=", timeit(code1, number=10000))
print("without exception code time=", timeit(code2, number=10000))
