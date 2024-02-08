import os
os.chdir("D:/Program/Github/User-Scheduling-in-5G/src")
print(os.getcwd())
from scheduling import *
from Greedy import *
from Preprocessing import *
from Presentation import *
from Solver import *

###Question 2

# for i in range(1,6):
#     print("\n")
#     print(f"File{i}: \n")
#     N,K,M,p,P,R = readData(f"test{i}.txt")
#     print(prePro(N,K,M,p,P,R))



### Question 5

# for i in range(1,6):
#     print("\n")
#     print(f"File{i}: \n")
#     N,K,M,p,P,R = readData(f"test{i}.txt")
#     if prePro(N,K,M,p,P,R):
#         qfive(f"test{i}.txt")


### Question 7

# for i in range(1,6):
#     print()
#     print(f"File{i}: \n")
#     qseven1(f"test{i}.txt")
print("File 4: \n")
qseven2("test4.txt")
print("File 5: \n")
qseven2("test5.txt")




 







































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