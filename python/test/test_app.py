import unittest
import sys
import os
sys.path.append(os.path.abspath("C:/Users/paapl/desktop/GIT/DevOps1-3/python"))
from app import addition

class TestAdditionFunction(unittest.TestCase):

    def test_addition(self):
        # Test with two positive integers
        self.assertEqual(addition(3, 5), 8)
        
        # Test with negative integers
        self.assertEqual(addition(-3, 5), 2)
        
        # Test with a zero
        self.assertEqual(addition(0, 5), 5)
        
        # Test with floating point numbers
        self.assertEqual(addition(3.5, 2.5), 6.0)
        
        # Test with zero and negative number
        self.assertEqual(addition(-3, 0), -3)

if __name__ == "__main__":
    unittest.main()


