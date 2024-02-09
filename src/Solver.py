from ortools.linear_solver import pywraplp
import numpy as np

def LPsolver(N,K,M,p,P,R):
    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        return
    Constp = np.array(P)
    Constr = np.array(R)
    Varx = []
    for i in range(N):
        Varx.append([])
        for j in range(K):
            Varx[i].append([])
            for k in range(M):
                Varx[i][j].append(solver.NumVar(0,1,f"x({i+1,j+1,k+1})"))
    #Varx = np.zeros((N,K,M))
    # Varx = list(Varx)
    # for i in range(N):
    #     for j in range(K):
    #         for k in range(M):
    #             Varx[i][j][k] = 
                #x = solver.NumVar(0, solver.infinity(), "x")
    print("Number of variables =", solver.NumVariables())

    # Constraint 0-N-1: forall n, sum(x) = 1
    constraints = []
    for i in range(N):
        constraint = solver.Constraint(1,1)
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

    # print("Number of constraints =", solver.NumConstraints())
    
    objective = solver.Objective()
    for i in range(N):
        for j in range(K):
            for k in range(M):
                objective.SetCoefficient(Varx[i][j][k],R[i][j][k])
    objective.SetMaximization()

    solver.Solve()
    opt_solution = 0
    opt_power = 0
    for i in range(N):
        for j in range(K):
            for k in range(M):
                #print(f"x({i+1,j+1,k+1}) = ", Varx[i][j][k].solution_value())
                opt_solution += Varx[i][j][k].solution_value()*R[i][j][k]
                opt_power += Varx[i][j][k].solution_value()*P[i][j][k]
    # print("Solution value: ", opt_solution)
    return opt_solution,opt_power





