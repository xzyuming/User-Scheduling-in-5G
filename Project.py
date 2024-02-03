import numpy as np

## Get the arrays of lists which represent all elements of the matrix of each server 
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
            A.append(float(lines[4+i*3+j].split('   ')[0]))
            A.append(float(lines[4+i*3+j].split('   ')[1]))
        P.append(A)
    for i in range(N):
        A=[]
        for j in range(K):
            A.append(float(lines[N*K+4+i*3+j].split('   ')[0]))
            A.append(float(lines[N*K+4+i*3+j].split('   ')[1]))
        R.append(A)
    return N,K,M,p,P,R


###Q2

def prePro(filepath):
    N,K,M,p,P,R = readData(filepath)
    if K>N:
        print("No solution")
        return False
    for i in range(N):
        max = 0
        counter = 0 
        min = P[i][0]
        for j in range(K*M):
            if P[i][j]<min:
                min = P[i][j]
        if min>p:
            print("No solution")
            return False
    return True


###Q3

## Fonction of sorting
def QuickSort(arr):

    def partition(arr,low,high): 
        i = ( low-1 )         
        pivot = arr[high][0]     
        for j in range(low , high): 
            if   arr[j][0] <= pivot: 
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return ( i+1 ) 
  
    def quickSort(arr,low,high): 
        if low < high: 
            pi = partition(arr,low,high) 
            quickSort(arr, low, pi-1) 
            quickSort(arr, pi+1, high) 
    
    n = len(arr)
    if n<=1:
        return arr
    quickSort(arr,0,n-1)
    return arr



## Remove IP-dominated  rem is what we remove, res is the rest
def ipRe(arr):
    rem = []
    res = [arr[0]]
    for i in range(1,len(arr)):
        res.append(arr[i])
        if res[-1][1]<=res[-2][1]:
            rem.append(res.pop())

    return rem


# N,K,M,p,P,R = readData('test1.txt')

## Removed points
# Res = []
# for i in range(N):
#     n = [[P[i][j],R[i][j],j+1] for j in range(K*M)]
#     B = QuickSort(n)
#     print(B)
#     Res.append(ipRe(B))

# for i in range(N):
#     for k in range(len(Res[i])):
#         Res[i][k] = [(Res[i][k][2]-1)//M+1,(Res[i][k][2]-1)%M+1,i+1]


# print(Res)




###Q4
## Order the array and remove IP-dominated 
def IpRe(arr):
    rem = []
    res = [arr[0]]
    max = arr[0][1]
    for i in range(1,len(arr)):
        res.append(arr[i])
        if res[-1][1]<=res[-2][1]:
            rem.append(res.pop())
    return res

## Remove LP-dominated
def LpRe(arr):
    S = [arr[0],arr[1]]
    d = (arr[1][1]-arr[0][1])/(arr[1][0]-arr[0][0])
    for i in range(2,len(arr)):
        for j in S[::-1]:
            if (arr[i][1]-j[1])/(arr[i][0]-j[0])>=d:
                d= (arr[i][1]-j[1])/(arr[i][0]-j[0])
                S.pop()
        S.append(arr[i])
    return S

# N,K,M,p,P,R = readData('test1.txt')

# n = [[P[3][j],R[3][j],j+1] for j in range(K*M)]
# n = QuickSort(n)
# print(n)
# n = IpRe(n)
# print(n)
# n = LpRe(n)
# print(n)

###Q5

def qFive():
    Res = {}
    for i in range(1,6):
        if prePro(f"test{i}.txt"):
            Res[f"test{i}"] = {}
            N,K,M,p,P,R = readData(f"test{i}.txt")
            for k in range(N):
                n = [[P[k][j],R[k][j],j+1] for j in range(K*M)]
                n = QuickSort(n)
                n = IpRe(n)
                n = LpRe(n)
                Res[f"test{i}"][k] = n
        else:
            Res[f"test{i}"] = False
    return Res

## Show the result
# Res = qFive()
# for i in range(1,6):
#     if Res[f"test{i}"] != False:
#         print(f"Result of test{i}:\n")
#         for k in Res[f"test{i}"]:
#             print(k)
#             print("\n")
                                

###Q6

def Tmax(arr):
    L = len(arr)
    max = 0
    index = 0
    for i in range(L):
        if max<arr[i]:
            max = arr[i]
            index = i
    return index


def greedy1(arr,pv):
    L = len(arr)
    lmax = []
    Pv = []
    Rv = []
    T = []
    for i in range(L):
        Pv.append(arr[i][0][0])
        Rv.append(arr[i][0][1])
        T.append((arr[i][1][1]-arr[i][0][1])/(arr[i][1][0]-arr[i][0][0]))
        lmax.append(len(arr[i]))
    k = 0    
    # tmp = [0,0,0]
    l = [1 for i in range(L)]
    while(sum(Pv)<pv):
        k = Tmax(T) 
        Pv[k] = arr[k][l[k]][0]
        Rv[k] = arr[k][l[k]][1]
        # tmp = arr[k][l[k]]
        l[k]+=1
        if l[k] > lmax[k]-1:
            T[k] = 0
            continue
        T[k] = (arr[k][l[k]][1]-arr[k][l[k]-1][1])/(arr[k][l[k]][0]-arr[k][l[k]-1][0])
    q = 0
    if (sum(Pv)>pv):
        q = (pv-sum(Pv))/Pv[k] + 1
        Rv[k] *= q
        Pv[k] *= q
    return Pv,Rv,q

if prePro("test3.txt"):
    N,K,M,p,P,R = readData("test3.txt")
    res = []
    for k in range(N):
        n = [[P[k][j],R[k][j],j+1] for j in range(K*M)]
        n = QuickSort(n)
        n = IpRe(n)
        n = LpRe(n)
        res.append(n)
    print(res)
    res1,res2,q = greedy1(res,p) 
    print(res1)
    print(res2)
    print(q)

