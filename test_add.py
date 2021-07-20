import pytest
from add import add

def test():
    a = 100
    b = 200
    assert add(a, b) == -100
