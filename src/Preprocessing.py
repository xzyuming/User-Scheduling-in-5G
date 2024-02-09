from src.scheduling import *
from copy import deepcopy


def readData(path):
    with open(path,'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    P = []
    R = []
    N = int(float(lines[0]))
    M = int(float(lines[1]))
    K = int(float(lines[2]))
    p = float(lines[3])

    for i in range(N):
        A=[]
        for j in range(K):
            A.append([float(lines[4+i*K+j].split('   ')[m]) for m in range(M)])
        P.append(A)
    for i in range(N):
        A=[]
        for j in range(K):
            A.append([float(lines[N*K+4+i*K+j].split('   ')[m]) for m in range(M)])
        R.append(A)
    return N,K,M,p,P,R

def fmin(arr):
    min = arr[0]
    for i in range(len(arr)):
        if min>arr[i]:
            min = arr[i]
    return min

def prePro(N,K,M,p,P,R):
    arr = deepcopy(P)
    for i in range(N):
        arr[i] = [fmin(arr[i][j]) for j in range(M)]
        min = fmin(arr[i])
        if min>p:
            print("No solution")
            return False
    return True

        