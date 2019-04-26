# This program is designed to implement the Gauss - Chebyshev Quadrature Rule for numerical integration
# Required Libraries:
from __future__ import division
import numpy as np


def Gc(f, a, b, x, w, args):
    # Inputs:
    # f - the function being integrated
    # a - lower integration limit
    # b - upper integration limit
    # x - a vector of points
    # w - a vector of weights
    # args - a tuple of arguments to pass to f
    # Outputs:
    # integral - the approximated value of the integral
    ###################################################

    m = (b-a)/2

    # g transforms the original function f
    def g(a,b,x):
        y = (((x+1)*(b-a))/2)+a
        return f(y, args)*((1-x**2)**0.5)

    # Create an empty vector to store results to
    f_vec = numpy.empty(len(x))

    # For each sample point x, find the functional value and multiply it by its respective weighting.
    for i in range(len(x)):
        f_xi = g(a,b,x[i])
        f_vec[(i - 1)] = w[i] * f_xi

    # The integral is the weighted sum of the functional values, multiplied by (b-a)/2
    integral = np.sum(f_vec)*m

    return integral

