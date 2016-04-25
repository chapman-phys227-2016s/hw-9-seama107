#!\usr\bin\python
"""
File: MCint_class.py

Copyright (c) 2016 Michael Seaman

License: MIT

Implements the Integrator interface by realizing the Monte Carlo method
"""

import numpy as np
import time
from unittest import TestCase
from Integrator import Integrator


class MCint_class(Integrator):
    """
    Implements the construct_method method using the Monte Carlo integral
    approximation. Randomness is brought from np.random
    """
    def __init__(self, a, b, n, seed = -1):
        """
        Overloading the initializer to now add a seed, since random computations
        are now involved
        """
        if seed == -1:
            self.RNG = np.random.RandomState(int(time.time() * 100000) % 4294967295 )
        else:
            self.RNG = np.random.RandomState(seed)
        Integrator.__init__(self, a, b, n)


    def construct_method(self):
        """
        Returns an array of n random x values with equal probabilities throughout 
        a to b and an array of length n filled with h = (b-a)/n
        """
        a, b, n = self.a, self.b, self.n
        h = (b-a)/float(n)
        x = self.RNG.uniform(a, b, n)
        w = np.zeros(len(x)) + h
    	return x, w

def known_function(x):
    return 3 * x ** 3 - 10 * x ** 2 + 14

def known_integral(x):
    return .75 * x ** 4  - (10/3) * x ** 3 + 14 * x

def horizontal_function(x):
    return 10 + 0 * x

def horizontal_integral(x):
    return 10 * x


class Test_Integrator(TestCase):
    def test_MCint_same_seed(self):
        """
        Tests that two MC integrators return the same value given the same
        seed for their random values
        """
        a, b, n = -3.5, 6.5, 50
        seed_0 = int(time.time())
        mc1 = MCint_class( a, b, n, seed = seed_0)
        mc2 = MCint_class( a, b, n, seed = seed_0)
        assert (mc1.vectorized_integrate(known_function) == mc2.vectorized_integrate(known_function))

    def test_MCint_horizontal(self):
        """
        Tests the MC integration on a horizontal function, where it should 
        calculate the integral perfectly
        """
        a, b, n = -3.5, 6.5, 50
        mc1 = MCint_class(a, b, n)
        assert(mc1.vectorized_integrate(horizontal_function) == (horizontal_integral(b) - horizontal_integral(a)))


