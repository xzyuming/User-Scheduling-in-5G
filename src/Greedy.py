from scheduling import *
from Preprocessing import *

def Imax(arr):
    L = len(arr)
    max = 0
    ind = 0
    for i in range(L):
        if max<arr[i]:
            max = arr[i]
            ind = i
    return ind

def greedy1(path):
    if not prePro(path):
        return False
    N,K,M,p,P,R = readData(path)
    budget = p
    arr = []
    for i in range(N):
        arr.append(Channel(i,K,M,P,R))
        arr[i] = arr[i].LpRe()
    ILP = 1     # is this LP a ILP 
    lmax = []   # range of every channel after ip-lp-dominated treatment
    T = []      # arrary to compare efficiency
    Pv = []     # p\r values
    Rv = []
    In = []     # indices

    # because of methods IP-LP-dominated treatment, every channel has at least two acceptable elements 

    # initialization
    for i in range(N):
        Pv.append(arr[i][0].p)
        Rv.append(arr[i][0].r)
        In.append(arr[i][0])
        T.append((arr[i][1].r-arr[i][0].r)/(arr[i][1].p-arr[i][0].p))
        lmax.append(len(arr[i]))
    
    k = 0   
    l = [1 for i in range(N)]

    while(sum(Pv)<budget):
        k = Imax(T) 
        Pv[k] = arr[k][l[k]].p
        Rv[k] = arr[k][l[k]].r
        In[k] = arr[k][l[k]]
        l[k]+=1
        if l[k] > lmax[k]-1:
            T[k] = 0
            continue
        T[k] = (arr[k][l[k]].r-arr[k][l[k]-1].r)/(arr[k][l[k]].p-arr[k][l[k]-1].p)
    
    xa = 0
    xb = 0
    use = sum(Pv)
    rat = sum(Rv)
    if (use>budget):
        ILP = 0
        rest = Pv[k]-(use-budget)
        a = l[k] - 1
        b = a - 1
        xa = (rest-arr[k][b].p)/(arr[k][a].p - arr[k][b].p)
        xb = 1 - xa
        use = budget
        rat = rat - xb*arr[k][a].r + xb*arr[k][b]
        Pv[k] = {xb:arr[k][b].p, xa:arr[k][a].p}
        Rv[k] = xa*arr[k][a] + xb*arr[k][b]
        In[k] = {xb:arr[k][b],xa:arr[k][a]} 
    
    return ILP, rat, Pv, Rv, In
