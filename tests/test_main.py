# test_main.py
import unittest
from app.main import calculate_taxes

class TestMainFunctions(unittest.TestCase):
    def test_calculate_taxes(self):
        total_amount = 100
        expected_taxes = 5  # Assuming a tax rate of 5%
        self.assertEqual(calculate_taxes(total_amount), expected_taxes)

if __name__ == '__main__':
    unittest.main()
