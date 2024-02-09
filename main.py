import numpy as np
from Presentation import *
import  argparse
import os



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Path to test txt file")

    args = parser.parse_args()

    
    N,K,M,p,P,R = readData(args.path)

    arr = []
    for i in range(N):
        arr.append(Channel(i,K,M,P,R))

    if prePro(N,K,M,p,P,R):

        print("\n")
        print(args,": \n")
        qfive(N,K,M,p,P,R)
        print("\n")
        qseven1(N,K,M,p,P,R)
        print("\n")
        qseven2(N,K,M,p,P,R)
        print("\n")

        q11(N,p,arr)





if __name__ == '__main__':
    main()