import sys
import os
import pytest

sys.path.append(os.path.abspath("C:/Users/paapl/desktop/GIT/DevOps1-3/python"))
from app import addition

def test_addition():
    # Test with two positive integers
    assert addition(3, 5) == 8
    
    # Test with negative integers
    assert addition(-3, 5) == 2
    
    # Test with a zero
    assert addition(0, 5) == 5
    
    # Test with floating point numbers
    assert addition(3.5, 2.5) == 6.0
    
    # Test with zero and negative number
    assert addition(-3, 0) == -3
