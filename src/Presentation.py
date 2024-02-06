from Preprocessing import *
from scheduling import *
from Greedy import *
import os

os.chdir("D:/Program/Github/User-Scheduling-in-5G/src")

###Question 2

# N,K,M,p,P,R = readData("test1.txt")
# print(prePro(N,K,M,p,P,R))

###Question 3、4、5
def qfive(path):
    N,K,M,p,P,R = readData(path)
    print(P)
    if prePro(N,K,M,p,P,R):
        D = []
        for i in range(N):
            D.append(Channel(i,K,M,P,R))
        print("IP-dominated Removing results:")
        for i in range(N):
            print()
            print(f"{i+1}th channel:")
            rem,D[i] = D[i].IpRe()
            for j in range(len(D[i])):
                print(D[i][j].index)
        print("Then, LP-dominated Removing results(already removed IP-dominated):")
        for i in range(N):
            print()
            print(f"{i+1}th channel:")
            rem,D[i] = D[i].LpRe()
            for j in range(len(D[i])):
                print(D[i][j].index)
for i in range(1,6):
    qfive(f"test{i}.txt")


# def qseven(path):
#     A,Pvalue,Rvalue,Inst = greedy1(path)
#     print(A)
#     print(Pvalue)
#     print(Rvalue)


