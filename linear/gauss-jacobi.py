# Define a Gauss Jacobi Function
def gj(coef, cons, inx, maxiter, tol):
    # Arguments are:
    # coef - the coefficient matrix of the linear system.
    # cons - the constant matrix of the linear system.
    # inx - a vector containing the guesses for the variable values.
    # maxiter - the maximum iterations ran before ending the process.
    # tol - the tolerance level that must be satisfied for a solution to be found.

    # Generate DLU matrices
    D = np.diag(np.diag(coef))
    Dinv = np.linalg.inv(D)
    L = np.tril(np.tril(coef, k=-1)) * (-1)
    U = np.triu(np.triu(coef, k=1)) * (-1)

    # Set maximum iteration condition
    iterations = range(1,maxiter + 1)

    # Create a Base table to append results to.
    output = np.array([0, 0])

    # Create a boolean that will say if we found results or not.
    foundsolution = False

    # Solve the system
    for iteration in iterations:

        # Conduct Gauss - Jacobi Iteration
        step1 = L + U
        step2 = np.matmul(step1, inx)
        step3 = cons + step2
        outx = np.matmul(Dinv, step3)

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