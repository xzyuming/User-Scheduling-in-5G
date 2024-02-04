from Users import *



class Channel():

    def __init__(self,index, K, M, P, R):
        self.index = index
        self.M = M
        self.K = K
        self.users = [Users(index,i, value[0], value[1]) for i, value in enumerate(zip(P[index], R[index]))]

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
                rem.append(res.pop())
        return rem,res
    
    def LpRe(self):
        rem,arr = self.IpRe()
        S = [arr[0],arr[1]]
        d = (arr[1].r-arr[0].r)/(arr[1].p-arr[0].p)
        for i in range(2,len(arr)):
            for j in S[::-1]:
                if (arr[i].r-j.r)/(arr[i].p-j.p)>=d:
                    d= (arr[i].r-j.r)/(arr[i].p-j.p)
                    S.pop()
            S.append(arr[i])
        return S        
    
    
