'''script to define and run unit tests for each method 
in the SimpleCalculator class. Your tests should cover 
various scenarios to ensure the class functions correctly.'''

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        ''' Setup the SimpleCalculator instance before
        each test.'''
        self.calc = SimpleCalculator()
    def test_addition(self):
        '''Test the addition method.'''
        self.assertEqual(self.calc.add(2, 3),5)
        self.assertEqual(self.calc.add(2, -3),-1)
    def test_subtraction(self):
        '''Test the subtraction method.'''
        self.assertEqual(self.calc.subtract(6, 2),4)
        self.assertEqual(self.calc.subtract(2, 6),-4)
    def test_multiplication(self):
        '''Test the multiplication method.'''
        self.assertEqual(self.calc.multiply(2, 3),6)
    def test_division(self):
        '''Test the division method.'''
        self.assertEqual(self.calc.divide(10, 5),2)

