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
        a = 5
        b = 2
        subtracted = a - b
        subtracted_two = subtract(a,b)
        assert subtracted == subtracted_two

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ########Partner2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self): # 3 assertions
    #     fill in code
        self.assertEqual(logarithm(2, 2), 1)
        self.assertEqual(logarithm(8, 2), 3)
        self.assertEqual(logarithm(16, 4), 2)


    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(2, -1)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()