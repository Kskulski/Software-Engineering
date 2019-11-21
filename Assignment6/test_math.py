from unittest import TestCase
from unittest.mock import patch
from math import Math


class TestCalculator(TestCase):
    def setUp(self):
        self.calculator = Math()

    def test_add(self):
        self.assertEqual(self.calculator.add(10, 2), 12, "add two numbers positive numbers")

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5, "divide two positive numbers")

    def test_division_by_zero_throws_exception(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(1, 0)

    @patch('builtins.print')
    def test_print_dep(self, mock_print):
        self.calculator.sub_and_print(1, 2)
        mock_print.assert_called_with('result is : {}'.format(1-2))


if __name__ == '__main__':
    math = Math()
    weather = weather_client.get_weather_by_zip(zip_code='60564')
    print(weather)