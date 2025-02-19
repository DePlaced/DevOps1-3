import pytest
from app.app import addition

def test_addition():
    assert addition(3, 5) == 8
    assert addition(-3, 5) == 2
    assert addition(0, 5) == 5
    assert addition(3.5, 2.5) == 6.0
    assert addition(-3, 0) == -3
