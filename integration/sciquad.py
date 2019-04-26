# This program is designed to use scipy's numerical integration tool to find the integral of a function over several parameter values.

# Required libraries:
import scipy.integrate
import numpy as np


def sciquad(f,lam,lower,upper):
	# Inputs:
	# f - function to be integrated
	# lam - a vector of relevant parameter values
	# lower - lower bound of integration
	# upper - upper bound of integration

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

		# Call scipy.integrate to find the value of the integral given a function f, lower bound, upper bound, and the tuple of given parameters.
		scisol = scipy.integrate.quad(f,lower,upper, args = ptup)

		# Store results
		solution[i] = scisol[0]

	# The function returns a vector of results. each element of the vector is a different integral value
	return solution