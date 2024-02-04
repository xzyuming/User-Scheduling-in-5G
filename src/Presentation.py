from Preprocessing import *
from scheduling import *
from Greedy import *
import os

os.chdir("D:/GCC/User-Scheduling-in-5G/src")

def qfive(path):
    N,K,M,p,P,R = readData(path)
    if prePro(N,K,M,p,P,R):
        D = []
        for i in range(N):
            D.append(Channel(i,K,M,P,R))
        for i in range(N):
            print()
            print(f"{i+1}th channel:")
            rem,D[i] = D[i].LpRe()
            for j in range(len(D[i])):
                print(D[i][j].index)

def qseven(path):
    A,Pvalue,Rvalue,Inst = greedy1(path)
    print(A)
    print(Pvalue)
    print(Rvalue)


qfive("test1.txt")