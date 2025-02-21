from numpy import sqrt as np_sqrt
from numpy import array

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

def sqrt(a):
    """function to get sqrt(a)"""
    if a > 0:
        return np_sqrt(a)
    return 0
