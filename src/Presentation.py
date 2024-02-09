import time
from Preprocessing import *
from scheduling import *
from Greedy import *
from Solver import *



def qfive(path):
    N,K,M,p,P,R = readData(path)
    if prePro(N,K,M,p,P,R):
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



def qseven1(path):
    N,K,M,p,P,R = readData(path)
    if prePro(N,K,M,p,P,R):
        A,B,C,D = greedy1(N,K,M,p,P,R)
        E,F = LPsolver(N,K,M,p,P,R)
        print("Greedy: Rate: ",A[1],"  , power: ", A[2])
        print("LPsolver: Rate: ",E,"  , power: ",F)
        print()

def qseven2(path):
    N,K,M,p,P,R = readData(path)
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





