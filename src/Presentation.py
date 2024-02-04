from Preprocessing import *
from Channel import *
from Users import *
from Power import *

def qfive(path):
    N,K,M,p,P,R = readData(path)
    if prePro(path):
        D = []
        for i in range(N):
            D.append(Channel(i,K,M,P,R))
        for i in range(N):
            D[i] = D[i].LpRe()
            print(D[i].Users[i])
