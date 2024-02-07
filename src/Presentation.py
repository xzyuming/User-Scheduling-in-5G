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
for i in range(1,6):
    print(f"Test{i}'s results:")
    qfive(f"test{i}.txt")
    print("\n\n")


# def qseven(path):
#     A,Pvalue,Rvalue,Inst = greedy1(path)
#     print(A)
#     print(Pvalue)
#     print(Rvalue)


