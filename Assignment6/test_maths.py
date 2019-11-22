import unittest
from maths import Math


class MathTest(unittest.TestCase):
	def setUp(self):
		self.calc = Math()
		
	def test_is_even(self):
		self.assertEqual(self.calc.is_even(4), True, "tests if a positive number is even")
		self.assertEqual(self.calc.is_even(-6), True, "tests if a negative number is even")
		self.assertEqual(self.calc.is_even(0), True, "tests if 0 is even")
		self.assertEqual(self.calc.is_even(5), False, "tests if an odd number is even")
		self.assertEqual(self.calc.is_even(-9), False, "tests if a negative odd number is even")
		self.assertEqual(self.calc.is_even(4.2), True, "tests even decimal")
		self.assertEqual(self.calc.is_even(5.1), False, "tests odd decimal")

	#def test_factorial(self):
	#	self.assertEqual(self.calc.factorial(),,"tests")

	#def test_power(self):
		#self

if __name__ == '__main__':
	unittest.run()