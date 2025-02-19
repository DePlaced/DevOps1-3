"""
This module contains tests for app/app.py module.
"""

from app.app import addition

def test_addition():
    
    """
    Test the functionality of addition in app/app.py.
    """
    
    assert addition(3, 5) == 8
    assert addition(-3, 5) == 2
    assert addition(0, 5) == 5
    assert addition(3.5, 2.5) == 6.0
    assert addition(-3, 0) == -3
