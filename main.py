import numpy as np
from src.scheduling import *
from src.Preprocessing import *
from src.Solver import *
from src.Greedy import *
from src.Presentation import *
import  argparse




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Path to test txt file")

    args = parser.parse_args()
    N,K,M,p,P,R = readData(args)
    if prePro(N,K,M,p,P,R):
        print("\n")
        print(args,": \n")
        qfive(N,K,M,p,P,R)
        print("\n")
        qseven1(N,K,M,p,P,R)
        print("\n")
        qseven2(N,K,M,p,P,R)



if __name__ == '__main__':
    main()