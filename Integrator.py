#!\usr\bin\python
"""
File: Integrator.py

Copyright (c) 2016 Michael Seaman

License: MIT

A class for integration, to be used inherited by MCint_class.py
Stores the function to be differentiated, and the stepsize h for evaluation
"""

import numpy as np
from unittest import TestCase


class Integrator:
    def __init__(self, a, b, n):
        self.a, self.b, self.n = a, b, n
        self.points, self.weights = self.construct_method()

    def construct_method(self):
        raise NotImplementedError(’no rule in class %s’ % self.__class__.__name__)

    def integrate(self, f):
        s=0
        for i in range(len(self.weights)):
            s += self.weights[i]*f(self.points[i])
        return s

    def vectorized_integrate(self, f):
        return np.dot(self.weights, f(self.points))

class Midpoint(Integrator):
    def construct_method(self):
        a, b, n = self.a, self.b, self.n
        h = (b-a)/float(n)
        x = np.linspace(a + 0.5*h, b - 0.5*h, n)
        w = np.zeros(len(x)) + h
    return x, w