import Users



class Channel():

    def __init__(self,index, M, K, P, R):
        self.index = index
        self.M = M
        self.K = K
        self.users = [Users(index, value[0], value[1]) for index, value in enumerate(zip(P, R))]

    def flatten(self):
        tab = []
        for user in self.users:
            tab.extend(user.powers)
        return tab

    def sorted_by_power(self):
        tab = self.flatten()
        return sorted(tab, key= lambda x: x.p)
    
    
