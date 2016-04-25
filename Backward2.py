#!\usr\bin\python
"""
File: Backward2

Copyright (c) 2016 Michael Seaman

License: MIT

Extending the Diff2 class, this subclass implements the Backwards integration method using 3 points, given
by the formula:
f(x) \approx (f(x - 2h) - 4f(x - h) + 3f(x))/2h
"""


import numpy as np
from unittest import TestCase
from Diff2 import Diff2
from Diff2 import linear_func
from Diff2 import dfdx_linear_func

class Backward2(Diff2):
    """
    Implements the backward differentiation method for the instantaneous rate
    of change at the point x. Calculated using 3 points, moving backwards along
    the function f.
    """
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x - 2*h) - 4*f(x - h) + 3*f(x))/(2*h)

class Test_Backward(TestCase):
    def test_Backward2(self):
        """
        Tests that the backward differentiation method perfectly approximates
        a linear function using the dfdx_exact variable
        """
        d = Backward2(linear_func, dfdx_exact = dfdx_linear_func)
        test_values = np.array([-100, -40, 0, 60, 200])
        d.error = np.vectorize(d.error)

        assert np.all( abs(d.error(test_values)) <= np.full(5,1E-5))
