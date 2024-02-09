import numpy as np
import pkg_resources

import scheduling
import  argparse






def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Path to test txt file")

    args = parser.parse_args()
    pkg_resources.set_extraction_path

    #preprces(args)


if __name__ == '__main__':
    main()