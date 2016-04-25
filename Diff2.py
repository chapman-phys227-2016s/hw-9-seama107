#!\usr\bin\python
"""
File: Diff2

Copyright (c) 2016 Michael Seaman

License: MIT

A class for differentiation, to be used inherited by Backward2.py
Stores the function to be differentiated, and the stepsize h for evaluation
"""

import numpy as np
from unittest import TestCase



class Diff2():
    """
    Class holding a function to be differentiated as well as the stepsize h
    to evaluate from. Diff2 also stores the exact derivative to be checked against
    in the error method.
    Implemented (mostly) from the book
    """
    def __init__(self, f, h=1E-5, dfdx_exact = None):
        self.f = f
        self.h = np.array(h).astype(float)
        self.exact = dfdx_exact
        
    def error(self, x):
        if self.exact is not None:
            df_numerical = self(x)
            df_exact = self.exact(x)
            return df_exact - df_numerical

class Backward1(Diff2):
    """
    Implements the backward differentiation method for the instantaneous rate
    of change at the point x. Calculated using Euler's method.
    """
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x) - f(x-h))/h

def linear_func(x):
    return -50*x + 250.4

def dfdx_linear_func(x):
    return -50

class Test_Diff2(TestCase):
    def test_Backward1(self):
        """
        Tests that the backward differentiation method perfectly approximates
        a linear function using the dfdx_exact variable
        """
        d = Backward1(linear_func, dfdx_exact = dfdx_linear_func)
        test_values = np.array([-100, -40, 0, 60, 200])
        d.error = np.vectorize(d.error)

        assert np.all( abs(d.error(test_values)) <= np.full(5,1E-5))
