import os
os.chdir("D:/Program/Github/User-Scheduling-in-5G/src")
print(os.getcwd())
from scheduling import *
from Greedy import *
from Preprocessing import *



# N,K,M,p,P,R = readData("test1.txt")
# print(N,K,M,p)
# print(P,R)
N = 4
K = 3
M = 2
p = 100.0
P = [[[1.0, 12.0], [19.0, 35.0], [37.0, 50.0]], [[20.0, 50.0], [16.0, 17.0], [1.0, 7.0]], [[13.0, 36.0], [34.0, 46.0], [1.0, 27.0]], [[16.0, 28.0], [1.0, 32.0], [35.0, 43.0]]]
R = [[[65.0, 98.0], [62.0, 90.0], [23.0, 95.0]], [[49.0, 54.0], [76.0, 81.0], [50.0, 85.0]], [[24.0, 86.0], [41.0, 62.0], [63.0, 87.0]], [[15.0, 56.0], [13.0, 95.0], [41.0, 42.0]]]
for i,value in enumerate(zip(P[0],R[0])):
    print(i,value)


# D = Channel(0,N,K,M,P,R)

# user_instance = User(1, 2, [100.0, 200.0, 300.0], [50.0, 75.0, 100.0])
# print(user_instance.index)
# A = [[i,value[0],value[1]] for i,value in enumerate(zip(x,y))]
# print(A)







































## Fonction to search the pairs that p1<p2 but r1>r2
# def search(arr,res):
#     if len(arr)<2:
#         return arr,res
#     mid = len(arr)//2
#     left,res = search(arr[:mid],res)
#     right,res = search(arr[mid:],res)
#     i = 0
#     j = 0
#     while i<len(left) and j<len(right):
#         if left[i][1] <= right[j][1]:
#             i+=1
#         else:
#             # print(left[i][2],right[i][2])
#             if right[j][2] not in res: 
#                 res.append(right[j][2])
#             j+=1
#     while i<len(left):
#         i += 1
#     while j < len(right): 
#         j += 1
#     return arr,res

# Res = []
# for i in range(N):
#     n = [[P[i][j],R[i][j],j+1] for j in range(K*M)]
#     B = QuickSort(n)
#     r = []
#     print(B)
#     r1,r2 = search(B,r)
#     Res.append(r2)

# print(Res)
# for j in range(N):
#     for k in range(len(Res[j])):
#         Res[j][k] = [(Res[j][k]-1)//M+1,(Res[j][k]-1)%M+1,j+1]