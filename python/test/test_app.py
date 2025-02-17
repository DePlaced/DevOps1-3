import unittest
from app import addition  # Import the function you want to test

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


