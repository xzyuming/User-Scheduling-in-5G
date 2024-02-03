import Power


class Users():

    def __init__(self, index, p: list, r: list):
        self.index = index
        self.powers = [Power(index, value[0], value[1]) for index, value in enumerate(zip(p, r))]



    def remove(self, power):
        self.powers[power.index] = None

