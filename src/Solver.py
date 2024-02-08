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

    objective = s


# Constraint 0: x + 2y <= 14.
solver.Add(x + 2 * y <= 14.0)

# Constraint 1: 3x - y >= 0.
solver.Add(3 * x - y >= 0.0)

# Constraint 2: x - y <= 2.
solver.Add(x - y <= 2.0)

print("Number of constraints =", solver.NumConstraints())

