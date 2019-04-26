# This program is designed to implement the Gauss - Legendre Quadrature Rule for numerical integration
# Required Libraries:
from __future__ import division
import numpy as np


def Gl(f, a, b, x, w, args):
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
        return f(y, args)

    # Create an empty vector to store results to
    f_vec = np.zeros(len(x))

    # For each sample point x, find the functional value and multiply it by its respective weighting.
    for i in range(len(x)):
        f_xi = g(a,b,x[i])
        f_vec[(i - 1)] = w[i] * f_xi

    # The integral is the weighted sum of the functional values, multiplied by (b-a)/2
    integral = np.sum(f_vec)*m

    return integral


def gaussleg(f, lam, lower, upper, n):
    # Inputs:
    # f - function to be integrated
    # lam - a vector of relevant parameter values
    # lower - lower bound of integration
    # upper - upper bound of integration
    # n - the number of "bins" to integrate over

    # Output:
    # solution - vector of results
    ###############################

    # Generate sample points and weights
    x, w = np.polynomial.legendre.leggauss(n)

    # create an empty array to store results to
    solution = np.zeros(len(lam))

    # For each value of lambda, the loop will find the value of the integral, and store it to the above vector
    for i in range(len(lam)):
        # Create a tuple that contains a vector of parameters
        parameters = np.array([0.04, lam[i], 0.5])
        ptup = (parameters)

        # This takes care of infinite upper bound
        if (upper == np.inf):
            bdiff = 1
            b_0 = 50
            # While the difference between choices of b is still significant, we will continue to increase b
            # When doubling b no longer significantly changes the integral, then the loop breaks.
            while abs(bdiff) > .01:
                b_1 = b_0 * 2
                result_0 = Gl(f, lower, b_0, x, w, ptup)
                result_1 = Gl(f, lower, b_1, x, w, ptup)
                bdiff = result_1 - result_0
                b_0 = b_1
        else:
            b_1 = up

        # Call gl function from above to find the value of the integral.
        gausslegsol = Gl(f, lower, b_1, x, w, ptup)

        # Store results
        solution[i] = gausslegsol

    # The function returns a vector of results. each element of the vector is a different integral value
    return solution
