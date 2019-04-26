# This program is designed to implement the Simpson's Rule for numerical integration

from __future__ import division
import numpy as np


def Simp(f, a, b, n, args):
	# Inputs:
	# f - the function being integrated
	# a - lower integration limit
	# b - upper integration limit
	# n - the number of "bins" to integrate over
	# args - a tuple of arguments to pass to f

	# Outputs:
	# integral - the approximated value of the integral
	###################################################

	# Calculate the necessary change in x (width of "bin")
	dx = (b - a)/n

	# Calculate initial functional value (at lower limit)
	f0 = f(a,args)

	# Calculate final functional value (at upper limit)
	fn = f(b,args)

	# Create an empty vector to store intermediate functional values to
	f_i = np.zeros(n-1)

	# For each "bin" 1 to n-1, calculate the functional value at the given x, and weight it.
	for i in range(1,n):
		# Even instances receive a weight of 2
		if i%2 == 0:
			x = a + (i*dx)
			f_i[i-1] = 2*f(x,args)
		# Odd instances receive a weight of 4
		else:
			x = a + (i*dx)
			f_i[i-1] = 4*f(x,args)

	# Sum all weighted intermediate functional values
	fi = np.sum(f_i)

	# The integral is equal to the sum of all weighted functional values, times the change in x divided by 3
	integral = (dx/3)*(fi+f0+fn)

	return integral


def simpson(f, lam, lower, upper, n):
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
				result_0 = Simp(f, lower, b_0, n, ptup)
				result_1 = Simp(f, lower, b_1, n, ptup)
				bdiff = result_1 - result_0
				b_0 = b_1
		else:
			b_1 = up

		# Call simp function from above to find the value of the integral.
		simpsol = Simp(f, lower, b_1, n, ptup)

		# Store results
		solution[i] = simpsol

	# The function returns a vector of results. each element of the vector is a different integral value
	return solution



