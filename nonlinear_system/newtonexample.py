# ------------------------------------------------------------------------------------------------------ #
# Author: Anna Lonergan                                                                                  #
# Purpose: Script providing examples for the Newton-raphson Functions.                                   #
# ------------------------------------------------------------------------------------------------------ #

# necessary libraries:
import numpy as np
from newtonraphson import * 


##################################################################
# EXAMPLE 1 -> 2 Functions                                       #
# Consider a market with nonlinear demand and supply curves.     #
# Solve the system of equations for equilibrium Price & Quantity #
# Supply: P(Qs) = 20*(1.5**Qs/100)                               #
# Demand: P(Qd) = (2000 - Qd)**0.7                               #
# The market equilibrium is:                                     #
# P = 165.55, Q = 521.26                                         #
# Now, lets test the algorithm                                   #
##################################################################

# Create system of equations
def F(X):
    # F takes one argument, X.
    # X is a tuple, list or vector containing values for the relevant system variables (P & Q)
    p = X[0]
    q = X[1]
    # System is a vector of zeros, the same length as X. 
    # Each element of the vector "system" will hold a function.
    # Length of X and system *must* match, because the number of unknowns (2: P & Q) must match the number of equations (2). 
    system = np.zeros(len(X))
    system[0] = 20*(1.5**(q/100)) - p
    system[1] = (2000 - q)**0.7 - p
    # This function returns a vector of 2 equations, evaluated at X. 
    return system


# Set initial guess, P = 0, Q = 0
init = np.array([0,0])

# Find the Solution:
# Only required inputs are function & initial value guesses. 
# Tolerance and Maximum Iterations are optional. I choose not to specify, so we'll use the NR function defaults.
solution, results = NR(F, init)

print("\nExample 1: Nonlinear Market")
print("Price in the market is %3.3f, and the Quantity Demanded is %3.3f." % (solution[0], solution[1]))
print("\n Iteration Output:")
print(results)

# Nice! The solutions from my solver match those listed above. It seems to be working in 2 dimensions. 


##################################################################
# EXAMPLE 2 -> 3 Functions                                       #
# Consider a market with 3 cournot duopolists.                   #
# Each producer chooses its own quantity based on what the other #
# duopolists produce.                                            #
# Solve this system of the duopolists' reaction curves.          #
# Supply1: Q1(q2,q3) = 5 - 0.5q2 -0.3q3                          #
# Supply2: Q2(q1,q3) = 7 - 0.6q1 -0.1q3                          #
# Supply3: Q3(q1,q2) = 4 - 0.2q1 -0.4q2                          #
# The market equilibrium is:                                     #
# q1 = 1.67 , q2 = 5.87 , q3 = 1.32                              #
# Now, lets test the algorithm                                   #
##################################################################

# Create system of equations
def Duopoly(Q):
    # Duopoly takes one argument, Q.
    # Q is a tuple, list or vector containing values for the relevant system variables (Q1-Q3)
    q1 = Q[0]
    q2 = Q[1]
    q3 = Q[2]
    # System is a vector of zeros, the same length as Q. 
    # Each element of the vector "system" will hold a function.
    # Length of Q and system *must* match, because the number of unknowns (3: q1, q2 & q3) must match the number of equations (3). 
    system = np.zeros(len(Q))
    system[0] = 5 - (0.5*q2) - (0.3*q3) - q1
    system[1] = 7 - (0.6*q1) - (0.1*q3) - q2
    system[2] = 4 - (0.2*q1) - (0.4*q2) - q3
    # This function returns a vector of 3 equations, evaluated at Q. 
    return system


# Set initial guess, all quantities equal 0. 
init = np.array([0,0,0])

# Find the Solution:
# Only required inputs are function & initial value guesses. 
# Tolerance and Maximum Iterations are optional. I choose not to specify, so we'll use the NR function defaults.
solution, results = NR(Duopoly, init)

print("\nExample 2: Cournot Duopolists")
print("Q1 is %3.3f, Q2 is %3.3f, and Q3 is %3.3f." % (solution[0], solution[1], solution[2]))
print("\n Iteration Output:")
print(results)

# Again, the solutions from my solver match those listed above. It seems to be working in 3 dimensions. 


