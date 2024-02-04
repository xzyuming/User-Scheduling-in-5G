from Preprocessing import *
from scheduling import *
import os

os.chdir("D:/GCC/User-Scheduling-in-5G/src")

def qfive(path):
    N,K,M,p,P,R = readData(path)
    if prePro(path):
        D = []
        for i in range(N):
            D.append(Channel(i,K,M,P,R))
        for i in range(N):
            print()
            print(f"{i+1}th channel:")
            D[i] = D[i].LpRe()
            for j in range(len(D[i])):
                print(D[i][j].index)

qfive("test1.txt")

