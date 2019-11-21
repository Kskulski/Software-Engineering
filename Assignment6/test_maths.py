import unittest
from maths import Math


class MathTest(unittest.TestCase):
	def setUp(self):
		self.calc = Math()
		
	def test_is_even(self):
		self.assertEqual(self.calc.is_even(4), 0, "tests if a positive number is even")
		self.assertEqual(self.calc.is_even(-6), 0, "tests if a negative number is even")
		self.assertEqual(self.calc.is_even(0), 0, "tests if 0 is even")
		self.assertEqual(self.calc.is_even(5), 1, "tests if an odd number is even")
		self.assertEqual(self.calc.is_even(4.2), True, "tests a decimal")

	#def test_factorial(self):
	#	self.assertEqual(self.calc.factorial(),,"tests")

if __name__ == '__main__':
	unittest.run()