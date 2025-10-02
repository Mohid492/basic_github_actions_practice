import pytest
from Code import *

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 1) == -1
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 3) == -3
    assert multiply(0, 100) == 0

def test_is_equal():
    assert is_equal(2, 2) is True
    assert is_equal(2, 3) is False
    assert is_equal("a", "a") is True

def test_is_is():
    a = [1, 2]
    b = a
    c = [1, 2]
    assert is_is(a, b) is True
    assert is_is(a, c) is False
    assert is_is(None, None) is True