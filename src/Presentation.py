import time
from src.Preprocessing import *
from src.scheduling import *
from src.Greedy import *
from src.Solver import *
from src.DP import *
from src.BB import *

def qfive(N,K,M,p,P,R):
    # N,K,M,p,P,R = readData(path)
    # if prePro(N,K,M,p,P,R):
        D = []
        D1 = []
        D2 = []
        for i in range(N):
            D.append(Channel(i,K,M,P,R))
            D1.append([])
            D2.append([])
        print("Instance after IP-dominated Removing:")
        for i in range(N):
            print()
            print(f"{i+1}th channel:")
            rem,A = D[i].IpRe()
            D1[i].append(rem)
            for j in range(len(A)):
                print(A[j].index,end = ' ')
        print("\n\nThen, instance after LP-dominated Removing(already removed IP-dominated):")
        for i in range(N):
            print()
            print(f"{i+1}th channel:")
            rem,A = D[i].LpRe()
            D2[i].append(rem)
            for j in range(len(A)):
                print(A[j].index,end = ' ')




def qseven1(N,K,M,p,P,R):
    # N,K,M,p,P,R = readData(path)
    # if prePro(N,K,M,p,P,R):
        A,B,C,D = greedy1(N,K,M,p,P,R)
        E,F = LPsolver(N,K,M,p,P,R)
        print("Greedy: Rate: ",A[1],"  , power: ", A[2])
        print("LPsolver: Rate: ",E,"  , power: ",F)
        print()

def qseven2(N,K,M,p,P,R):
    # N,K,M,p,P,R = readData(path)
    start = 0
    end = 0
    if prePro(N,K,M,p,P,R):
        start = time.perf_counter()
        A,B,C,D = greedy1(N,K,M,p,P,R)
        end = time.perf_counter()
        print("Greedy runtime: ", end-start)
        print()
        start = time.perf_counter()
        E,F = LPsolver(N,K,M,p,P,R)
        end = time.perf_counter()
        print("LP-solver runtime: ", end-start)
        print()

    return A[1]
def q11(rate, p, *channels):
    start = 0
    end = 0


    print()
    start = time.perf_counter()
    Dp_by_power(p, *channels)
    end = time.perf_counter()
    print("DP_power runtime: ", end - start)
    print()
    start = time.perf_counter()
    Dp_by_rate(rate, channels)
    end = time.perf_counter()
    print("DP_rate runtime: ", end-start)
    '''
    start = time.perf_counter()
    current_feasible_solution, current_feasible_bound, used_power = branch_and_bound(p, *channels)
    end = time.perf_counter()
    print("Greedy runtime: ", end-start)
'''

