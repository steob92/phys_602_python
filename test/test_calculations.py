import sys
import os
import numpy as np

# Add the base directory to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from calculations import (
    add,
    sub,
    mult,
    div,
    sqrt,
)

a = 1.4
b = 0.1


def test_add():
    assert add(a, b) == a + b


def test_sub():
    assert sub(a, b) == a - b


def test_mult():
    assert mult(a, b) == a * b


def test_div():
    assert div(a, b) == a / b

def test_sqrt():
    assert sqrt(a) == np.sqrt(a) if a > 0 else 0


print ("All our tests worked!")