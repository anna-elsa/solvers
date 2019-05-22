# Program purpose: Solve a linear system of equations using Gauss-Seidel Method

################################## NOTES #################################################
# Consider the following form of a linear system:
#   ax + by = j
#   cx + dy = k
#  ... where x & y are variables, and a, b, c, d, f, and k are numbers. 
# 
#  The linear system can be rewritten as a product of 2 matrices: coefficients, and variables, 
#  and set equal to the constant matrix. See below example:
#  [ a  b ] * [ x ] = [ j ]
#  [ c  d ]   [ y ]   [ k ]
# 
#  The first matrix is a (2x2) matrix containing variable coefficients. 
#  The second matrix is a (2x1) matrix containing the variables. 
#  Multiplied together, these matrices are set equal to a (2x1) matrix of constants. 
#  This same form can be used in 3+ dimensions.
#  
#  If you have a linear systems of equations, write it in this matrix form before using ths python solver.
##########################################################################################

def gs(coef, cons, inx, maxiter, tol):
    # Arguments are:
    # coef - the coefficient matrix of the linear system.
    # cons - the constant matrix of the linear system.
    # inx - a vector containing the guesses for the variable values.
    # maxiter - the maximum iterations ran before ending the process.
    # tol - the tolerance level that must be satisfied for a solution to be found.

    # Generate DLU matrices
    D = np.diag(np.diag(coef))
    L = np.tril(np.tril(coef, k=-1)) * (-1)
    DL = D - L
    DLinv = np.linalg.inv(DL)
    U = np.triu(np.triu(coef, k=1)) * (-1)

    # Set maximum iteration condition
    iterations = range(1, maxiter + 1)

    # Create a Base table to append results to.
    output = np.array([0, 0])

    # Create a boolean that will say if we found results or not.
    foundsolution = False

    for iteration in iterations:

        # Conduct Gauss - Jacobi Iterations
        step1 = np.matmul(U, inx)
        step2 = cons + step1
        outx = np.matmul(DLinv, step2)

        # Calculate the difference between input and output & take euclidean norm
        diff = outx - inx
        norm = np.linalg.norm(diff, ord=2)

        # Add it to our array
        row = np.array([iteration, norm])
        output = np.vstack([output, row])

        # The input for next iteration is equal to the output on the current iteration
        inx = outx

        # One of the end conditions: The euclidean norm is less than the tolerance level
        if norm < tol:
            print("\nA solution has been found during iteration " + str(iteration))
            foundsolution = True
            iteration_table = pd.DataFrame(data=output[1:, 0:])
            iteration_table.columns = ["Iteration #", "Euclidean Norm"]
            break
    if foundsolution == True:
        print("\nThe output at each iteration:")
        print iteration_table
        return inx
    else:
        print("No solution was found in the given iterations")
