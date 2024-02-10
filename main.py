import numpy as np
from src.Presentation import *
import  argparse
import os
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Path to test txt file")

    args = parser.parse_args()

    
    N,K,M,p,P,R = readData(args.path)



    if prePro(N,K,M,p,P,R):
        arr = []
        for i in range(N):
            arr.append(Channel(i, K, M, P, R))

        print("\n")
        print(args,": \n")
        qfive(N,K,M,p,P,R)
        print("\n")
        qseven1(N,K,M,p,P,R)
        print("\n")
        rate = qseven2(N,K,M,p,P,R)
        print("\n")
        q11(rate, p,*arr)
        print("\n")

    path = os.path.dirname(args.path)
    print(" - Loading directory", path)
    decision = input("! WARNING: loading large JSON data sets may take a lot of memory and slow down/freeze your system. \
                     \nDo you wish to continue? Type 'yes' to load directory.\n")
    pattern = re.compile(r'test\d+\.txt')
    if decision == "yes":
        for root, dirs, files in os.walk(path):
            for f in sorted(files):
                if pattern.match(f):
                    N, K, M, p, P, R = readData(os.path.join(root, f))

                    if prePro(N, K, M, p, P, R):
                        arr = []
                        for i in range(N):
                            arr.append(Channel(i, K, M, P, R))

                        print("\n")
                        print(args, ": \n")
                        qfive(N, K, M, p, P, R)
                        print("\n")
                        qseven1(N, K, M, p, P, R)
                        print("\n")
                        rate = qseven2(N, K, M, p, P, R)
                        print("\n")
                        q11(rate, p, *arr)
                        print("\n")



if __name__ == '__main__':
    main()