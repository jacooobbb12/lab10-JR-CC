"""

https://github.com/jacooobbb12/lab10-JR-CC
Partner 1: Caleb Clements
Partner 2: Jacob Rosen
"""

import unittest
from calculator import add, subtract, multiply, divide, logarithm, exponent, hypotenuse, square_root


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(0,5), 5)
        self.assertEqual(add(-1,-6), -7)
        self.assertEqual(add(1.5,4.8), 6.3)



    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5,0), 5)
        self.assertEqual(subtract(-1,-4), 3)
        self.assertEqual(subtract(5.5,2.5), 3)



    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(multiply(5,0), 0)
        self.assertEqual(multiply(-1,-6), 6)
        self.assertAlmostEqual(multiply(1.5,4.8), 7.2)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(5,5), 1)
        self.assertEqual(divide(-5,-10), 2)
        self.assertEqual(divide(4.8,12), 2.5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
          with self.assertRaises(ZeroDivisionError):
                divide(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(8, 2), 3)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(2, -1)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, 0)
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code



    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(5,12), 13)
        self.assertEqual(hypotenuse(8,15), 17)
    #     fill in code


    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        with self.assertRaises(ValueError):
            square_root(-12)

        with self.assertRaises(ValueError):
            square_root(-9)

    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()