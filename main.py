import numpy as np

import Channel
import  argparse






def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Path to test txt file")

    args = parser.parse_args()

    #read_txtfile(args)


if __name__ == '__main__':
    main()