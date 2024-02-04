class Power():

    def __init__(self, i1, i2, i3, p, r):
        self.p = p
        self.r = r
        self.index = (i1,i2,i3)


class Users():
    
    def __init__(self, i1,i2, p: list, r: list):
        self.index = (i1,i2)
        self.powers = [Power(i1,i2,i+1, value[0], value[1]) for i, value in enumerate(zip(p, r))]


    def order(self):
        self.powers.sort(key= lambda x: x.p)

class Channel():

    def __init__(self,ind, K, M, P, R):
        self.index = ind+1
        self.M = M
        self.K = K
        self.users = [Users(ind+1,i+1, value[0], value[1]) for i, value in enumerate(zip(P[ind], R[ind]))]

    def remove(self, ind):
        a = ind[1]-1
        b = ind[2]-1
        return self.users[a].powers.pop(b)

    def flatten(self):
        tab = []
        for user in self.users:
            tab.extend(user.powers)
        return tab

    def sorted_by_power(self):
        tab = self.flatten()
        return sorted(tab, key= lambda x: x.p)

    def IpRe(self):
        arr = self.sorted_by_power()
        rem = []
        res = [arr[0]]
        for i in range(1,len(arr)):
            res.append(arr[i])
            if res[-1].r<=res[-2].r:
                int = res.pop()
                rem.append(int)
                self.remove(int.index)
        return rem,res
    
    def LpRe(self):
        rem,arr = self.IpRe()
        S = [arr[0],arr[1]]
        d = (arr[1].r-arr[0].r)/(arr[1].p-arr[0].p)
        for i in range(2,len(arr)):
            for j in S[::-1]:
                if (arr[i].r-j.r)/(arr[i].p-j.p)>=d:
                    d= (arr[i].r-j.r)/(arr[i].p-j.p)
                    int = S.pop()
                    rem.append(int)
                    self.remove(int.index)
            S.append(arr[i])
        return rem,S        
    
