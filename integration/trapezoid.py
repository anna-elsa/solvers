# This program is designed to implement the Trapezoid Rule for numerical integration
from __future__ import division
import numpy as np

def Tz(f, a, b, n, args):
	# Inputs:
	# f - the function being integrated
	# a - lower integration limit
	# b - upper integration limit
	# n - the number of "bins" to integrate over
	# args - a tuple of arguments to pass to f

	# Outputs:
	# integral - the approximated value of the integral
	###################################################

	# Calculate the height of each trapezoid/bin
	h = (b-a)/n

	s = 0.5*(f(a, args) + f(b, args))
	for i in range(1,n):
		s = s + f((a + (i*h)), args)

	integral = h*s
	return integral


def trapezoid(f, lam, lower, upper, n):
	# Inputs:
	# f - function to be integrated
	# lam - a vector of relevant parameter values
	# lower - lower bound of integration
	# upper - upper bound of integration
	# n - the number of "bins" to integrate over

	# Output:
	# solution - vector of results
	###############################

	# create an empty array to store results to
	solution = np.zeros(len(lam))

	# For each value of lambda, the loop will find the value of the integral, and store it to the above vector
	for i in range(len(lam)):
		# Create a tuple that contains a vector of parameters
		parameters = np.array([0.04,lam[i],0.5])
		ptup = (parameters)

		# This takes care of infinite upper bound
		if (upper == np.inf):
			bdiff = 1
			b_0 = 50
			# While the difference between choices of b is still significant, we will continue to increase b
			# When doubling b no longer significantly changes the integral, then the loop breaks.
			while abs(bdiff) > .01:
				b_1 = b_0*2
				result_0 = Tz(f, lower, b_0, n, ptup)
				result_1 = Tz(f, lower, b_1, n, ptup)
				bdiff = result_1 - result_0
				b_0 = b_1
		else:
			b_1 = up

		# Call tz function from above to find the value of the integral.
		trapsol = Tz(f, lower, b_1, n, ptup)

		# Store results
		solution[i] = trapsol

	# The function returns a vector of results. each element of the vector is a different integral value
	return solution

