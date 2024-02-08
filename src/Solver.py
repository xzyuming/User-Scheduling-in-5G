from ortools.linear_solver import pywraplp
import numpy as np

def LPsolver(N,K,M,p,P,R):
    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        return
    Constp = np.array(P)
    Constr = np.array(R)
    Varx = np.zeros((N,K,M))
    for i in range(N):
        for j in range(K):
            for k in range(M):
                Varx[i][j][k] = solver.NumVar(0,1,f"x({i+1,j+1,k+1})")
                #x = solver.NumVar(0, solver.infinity(), "x")
    print("Number of variables =", solver.NumVariables())

    # Constraint 0-N-1: forall n, sum(x) = 1
    constraints = []
    for i in range(N):
        constraint = solver.Constraint(1)
        for j in range(K):
            for k in range(M):
                constraint.SetCoefficient(Varx[i][j][k],1)
                constraints.append(constraint)
    
    # Constraint N: Respect the budget
    constraint = solver.Constraint(0,p)
    for i in range(N):
        for j in range(K):
            for k in range(M):
                constraint.SetCoefficient(Varx[i][j][k],P[i][j][k])
    constraints.append(constraint)

    print("Number of constraints =", solver.NumConstraints())
    
    objective = solver.Objective()
    for i in range(N):
        for j in range(K):
            for k in range(M):
                objective.SetCoefficient(Varx[i][j][k],R[i][j][k])
    objective.SetMaximization()

    solver.Solve()
    for i in range(N):
        for j in range(K):
            for k in range(M):
                print(f"x({i+1,j+1,k+1}) = ")
                opt_solution += Varx[i][j][k]*R[i][j][k]
    print("Solution value: ", opt_solution)





