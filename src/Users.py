from Power import *


class Users():

    def __init__(self, i1,i2, p: list, r: list):
        self.index = (i1,i2)
        self.powers = [Power(i1,i2,i, value[0], value[1]) for i, value in enumerate(zip(p, r))]



    def remove(self, power):
        self.powers[power.index] = None

