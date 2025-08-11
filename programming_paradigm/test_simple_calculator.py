import unittest
from unittest import TestCase
from simple_calculator import SimpleCalculator

class SimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 4), 1)
        self.assertEqual(self.calc.subtract(-5, 4), -9)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(6, 3), 18)
        self.assertEqual(self.calc.multiply(-6, 3), -18)

    def test_division(self):
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(9, 0), "None")


