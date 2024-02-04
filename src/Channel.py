import Users



class Channel():

    def __init__(self,index, K, M, P, R):
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
    
    
