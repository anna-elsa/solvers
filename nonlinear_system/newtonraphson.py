# ------------------------------------------------------------------------------------------------------ #
# Author: Anna Lonergan                                                                                  #
# Purpose: Script defining Newton-Raphson method for solving systems of linear and nonlinear equations   #
# ------------------------------------------------------------------------------------------------------ #

# Necessary Libraries:
import numpy as np
import numdifftools as nd
import pandas as pd

# Define NR (Newton-Raphson) function
def NR(F, x, tol = 0.000001, maxiter = 50):
    # Newton - Raphson Algorithm 
    # Inputs:
    # F - a function. Defines the function(s) of the system, length = n.
    # x - list/array. initial guess for variables. length = n
    # tol - numeric. The error tolerance level. Default is 1e-6
    # maxiter - numeric. Number of maximum iterations to run algorithm. Default is 50.

    # Output:
    # solution - vector of length n which solves the system
    # nrout - data frame with information on norms and iteration number.
    ###############################################################################

    # Generate a dummy variable equal to zero. Dummy will be set to 1 if a solution is found.
    sol_found = 0

    # Create a base array to append results to
    results = np.zeros(len(x)+3)

    # Loop for Newton-Raphson Algorithm
    for iteration in range(1, maxiter + 1):

        # Step 2: Evaluate function at x, called Fval, and its Euclidean norm
        Fval = F(x)
        fnorm = np.linalg.norm(Fval, ord=2) # ord = 2 for Euclidean norm

        # Step 3: Compute the Jacobian Matrix
        jac = nd.Jacobian(F)(x)

        # Step 4: Solve for delta
        delta = np.linalg.solve(jac, -1*Fval)
        dnorm = np.linalg.norm(delta, ord = 2) # ord = 2 for Euclidean norm

        # Store iteration results
        row = np.zeros(len(x)+3)
        row[0] = iteration
        row[1] = fnorm
        row[2] = dnorm
        for i in range(len(x)):
            row[i+3] = x[i]
        results = np.vstack([results, row])

        # Stopping condition 1: 
        if abs(fnorm) < tol:
            solution = x
            sol_found = 1
            break
        # Stopping condition 2:
        elif abs(dnorm) < tol:
            solution = x
            sol_found = 1
            break
        # If neither stopping condition is met, repeat steps 2 - 5 with updated x
        # Update x
        x = x + delta

    if sol_found == 1:
        iteration_table = pd.DataFrame(results[1:,0:])
        names1 = np.array(["Iteration #", "F norm", "D norm"])
        names2 = ['']*len(x)
        for i in range(len(x)):
            names2[i] = 'X_'+str(i)
        names = np.append(names1, names2)
        iteration_table.columns = names

        return solution, iteration_table
    else: 
        print "Could not find a solution with given parameters."
        return results


