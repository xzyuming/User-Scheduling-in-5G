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
            print(N)
            for k in range(N):
                print(k)
                n = [[P[k][j],R[k][j],j+1] for j in range(K*M)]
                n = QuickSort(n)
                n = IpRe(n)
                n = LpRe(n)
                Res[f"test{i}"][k] = n
        else:
            Res[f"test{i}"] = False
    return Res

## Show the result
Res = qFive()
for i in range(1,6):
    if Res[f"test{i}"] != False:
        print(f"Result of test{i}:\n")
        for k in Res[f"test{i}"]:
            print(k)
            print("\n")
                                


