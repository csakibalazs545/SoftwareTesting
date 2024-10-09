import pytest
from calculator import add, subtract, multiply, divide  # Adjust the import based on your actual file name

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(0, 0) == -1

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0
    assert subtract(-1, 1) == -2
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(5, 5) == 25
    assert multiply(3, 3) == 9
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(50, 10) == 6
    assert divide(100, 10) == 10
    assert divide(20, 20) == 1
    assert divide(8, 4) == 2
    