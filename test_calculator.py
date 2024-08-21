import unittest
from calculator import add, subtract, multiply, divide, exponent, modulus, integer_divide

class TestCalculator(unittest.TestCase):   
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_divide(self):
        self.assertEqual(divide(8, 2), 4.0)
    
    def test_exponent(self):
        self.assertEqual(exponent(2, 3), 8)
    
    def test_modulus_division_by_zero(self):
        self.assertEqual(modulus(5, 2), 1)
    
    def test_integer_divide_by_zero(self):
        self.assertEqual(integer_divide(5, 3), 1)
    
if __name__ == '__main__':
    unittest.main()