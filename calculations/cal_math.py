from numpy import sqrt as np_sqrt
from numpy import vectorize


def add(a, b):
    """function to add a and b"""
    return a + b


def sub(a, b):
    """function to sub a and b"""
    return a - b


def mult(a, b):
    """function to mult a and b"""
    return a * b


def div(a, b):
    """function to div a and b"""
    return a / b


# Use the vectorize decorator
# This will apply the function to every element in the array
@vectorize
def sqrt(a):
    """function to get sqrt(a) more words"""
    # Numpy is built upon C and Fortran code
    # These are "statically typed" languages
    # Meaning that the data type (int/float)
    # Is required by the user at compile time
    # Python is "dynamically typed" meaing the
    # data type can be infered at run time
    # Here a > "0" being passed to numpy will
    # infer the datatype to be an "int" rather
    # than a float. Likewise "return 0" returns
    # an integer. When this gets vectorized
    # Numpy will convert the output from a float
    # to an integer
    # if a > 0:
    #     return np_sqrt(a)
    # return 0

    # Notice the decimal point
    if a > 0.0:
        return np_sqrt(a)
    return 0.0
