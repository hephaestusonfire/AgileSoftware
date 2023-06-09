def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

import unittest

class FactorialTestCase(unittest.TestCase):
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(10), 3628800)

if __name__ == '__main__':
    unittest.main()
