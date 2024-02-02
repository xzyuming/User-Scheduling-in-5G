import numpy as np

# Get the arrays of lists which represent all elements of the matrix of each server 
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

#Q3

# Fonction of sorting
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

# Fonction to search the pairs that p1<p2 but r1>r2
def search(arr,res):
    if len(arr)<2:
        return arr,res
    mid = len(arr)//2
    left,res = search(arr[:mid],res)
    right,res = search(arr[mid:],res)
    i = 0
    j = 0
    while i<len(left) and j<len(right):
        if left[i][1] <= right[j][1]:
            i+=1
        else:
            # print(left[i][2],right[i][2])
            if right[j][2] not in res: 
                res.append(right[j][2])
            j+=1
    while i<len(left):
        i += 1
    while j < len(right): 
        j += 1
    return arr,res

# Remove implemention
def ipRe(arr):
    res = []
    for i in range(len(arr)-1):
        if (arr[i][0]<arr[i+1][0] and arr[i][1]>=arr[i+1][1]) or (arr[i][0] == arr[i+1][0] and arr[i][1]>arr[i+1][1]):
            res.append(arr[i+1])
    return res


# Algo implemention
N,K,M,p,P,R = readData('test1.txt')

# Res = []
# for i in range(N):
#     n = [[P[i][j],R[i][j],j+1] for j in range(K*M)]
#     B = QuickSort(n)
#     print(B)
#     Res.append(ipRe(B))

# for i in range(N):
#     for k in range(len(Res[i])):
#         Res[i][k] = [Res[i][k][2]//M+1,(Res[i][k][2]-1)%M+1,i+1]


Res = []
for i in range(N):
    n = [[P[i][j],R[i][j],j+1] for j in range(K*M)]
    B = QuickSort(n)
    r = []
    print(B)
    r1,r2 = search(B,r)
    Res.append(r2)

print(Res)
for j in range(N):
    for k in range(len(Res[j])):
        Res[j][k] = [(Res[j][k]-1)//M+1,(Res[j][k]-1)%M+1,j+1]

print(Res)

