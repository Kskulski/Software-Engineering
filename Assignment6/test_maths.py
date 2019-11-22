import unittest
from maths import Maths


class MathTest(unittest.TestCase):
	def setUp(self):
		self.calc = Maths()
		
	def test_is_even(self):
		self.assertEqual(self.calc.is_even(4), True, "tests if a positive number is even")
		self.assertEqual(self.calc.is_even(-6), True, "tests if a negative number is even")
		self.assertEqual(self.calc.is_even(0), True, "tests if 0 is even")
		self.assertEqual(self.calc.is_even(5), False, "tests if an odd number is even")
		self.assertEqual(self.calc.is_even(-9), False, "tests if a negative odd number is even")
		self.assertEqual(self.calc.is_even(4.2), True, "tests even decimal")
		self.assertEqual(self.calc.is_even(5.1), False, "tests odd decimal")

	def test_factorial(self):
		self.assertEqual(self.calc.factorial(8), 40320, "tests positive number")
		self.assertEqual(self.calc.factorial(-4), -24, "tests negative number")
		self.assertEqual(self.calc.factorial(0), 1, "tests 0")

	def test_power(self):
		self.assertEqual(self.calc.power(2, 5), 32, "tests two positive numbers")
		self.assertEqual(self.calc.power(-2, 8), 256, "tests a negative base")
		self.assertEqual(self.calc.power(2, -5), 32, "tests a negative power")
		self.assertEqual(self.calc.power(3, 0), 1, "tests to the zero power")
		self.assertEqual(self.calc.power(0, 5), 0, "tests zero as a base")

if __name__ == '__main__':
	unittest.run()