from C3_Calculator_Unit_testing import square


# we are gonna use this function as tester with the testing framework pytest
# which can be ran in the terminal by running "pytest filename.py"

# we use the assert keyword to say this function or this value MUST equal this.
# It is used for debugging purposes. It is a statement that evaluates an expression
# and raises an exception if the expression is not true.
def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_Zero():
    assert square(0) == 0


# NOTE
# we can make a folder full of tests
# we have to make a python file named "__init__.py" even if it's empty
# it will tell python that this folder is a package
# and then it will run all of the tests or python files in it
