class Power():

    def __init__(self, index: int, p, r):
        self.p = p
        self.r = r
        self.index = index

class Users():

    def __init__(self, index, p: list, r: list):
        self.index = index
        self.powers = [Power(index, value[0], value[1]) for index, value in enumerate(zip(p, r))]



    def remove(self, power):
        return self.powers.pop(power.index)

    def order(self):
        self.powers.sort(key= lambda x: x.p)

class Channel():

    def __init__(self, index, K, M, P, R):
        self.index = index
        self.M = M
        self.K = K
        self.users = [Users(i, value[0], value[1]) for i, value in enumerate(zip(P[index], R[index]))]

    def flatten(self):
        tab = []
        for user in self.users:
            tab.extend(user.powers)
        return tab

    def sorted_by_power(self):
        tab = self.flatten()
        return sorted(tab, key= lambda x: x.p)

