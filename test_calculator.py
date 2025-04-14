# https://github.com/Madam-TLE/lab10-TL-DS.git
# Partner 1: Trish Le
# Partner 2: Diego Salazar

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        #a = 3
        #b = 4
        #added = a + b
        #added_two = add(a,b)
        #assert added == added_two
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(2, 5), 7)
        self.assertEqual(add(3, 5), 8)

    def test_subtract(self): # 3 assertions
        #a = 5
        #b = 2
        #subtracted = a - b
        #subtracted_two = subtract(a,b)
        #assert subtracted == subtracted_two
        self.assertEqual(subtract(4, 3), 1)
        self.assertEqual(subtract(7, 5), 2)
        self.assertEqual(subtract(8, 5), 3)
    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(4, 5), 20)
        self.assertEqual(mul(6, 7), 42)

    def test_divide(self):
        self.assertAlmostEqual(div(10, 5), 2)
        self.assertAlmostEqual(div(5, 2), 2.5)
        self.assertAlmostEqual(div(8, 4), 2)

    ########Partner2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):
        self.assertEqual(logarithm(2, 2), 1)
        self.assertEqual(logarithm(8, 2), 3)
        self.assertEqual(logarithm(16, 4), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(2, -1)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        self.assertEqual(logarithm(1, 5), 0)
        self.assertEqual(logarithm(1, 5), 0)

    def test_hypotenuse(self):
        with self.assertRaises(TypeError):
            hypotenuse("1", "1")
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(0)
        self.assertAlmostEqual(square_root(1), 1)
        self.assertAlmostEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(16), 4)


# Do not touch this
if __name__ == "__main__":
    unittest.main()