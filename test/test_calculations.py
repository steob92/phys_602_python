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
    assert sqrt(a) == np.sqrt(a)

a_array = np.random.normal(0, 4, 100)
b_array = np.random.normal(0, 4, 100)

def test_add_arr():
    assert add(a_array, b_array) == a_array + b_array

def test_sub_arr():
    assert sub(a_array, b_array) == a_array - b_array

def test_mult_arr():
    assert mult(a_array, b_array) == a_array * b_array

def test_div_arr():
    assert div(a_array, b_array) == a_array / b_array

def test_sqrt_arr():
    assert sqrt(a_array) == np.array([
        np.sqrt(_a) if _a > 0 else 0 for _a in a_array
    ])