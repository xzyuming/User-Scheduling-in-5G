
def Dp_by_power(N: int, target : float, *channels:list[object]):
    result = {}
    Dp_by_power_rec(0, result, target, channels)
    key = sorted(result, key= lambda x: x[0])
    choices = []
    i = 1
    print("max rate is ", result[(i,target)["rate"]])
    while target > 0:
        choices.append(result[(i,target)["choice"]])
        i+=1
        target-= result[(i,target)["used"]]
    print("The choices maked are ", choices)


def Dp_by_power_rec(n : int, result:dict, p:float, channels:list[object]):
    if (n+1, p) in result.keys():
        return result[(n,p)]["rate"]
    max = 0
    k = 0
    m = 0
    used = 0
    for user in channels[n].users:
        for power in user.powers:
            temp = power.r + Dp_by_power_rec(n+1, result, p-power.p, channels)
            if temp>max:
                max = temp
                k = user.index
                m = power.index
                used = power.p
    result[(n+1, p)]= {"choice" : (n+1, k+1, m+1), "rate" : max, "used": used}


def Dp_by_rate(N: int, target: float, *channels: list[object]):
    result = {}
    Dp_by_rate_rec(0, result, target, channels)
    key = sorted(result, key=lambda x: x[0])
    choices = []
    i = 1
    print("min spend is ", result[(i, target)["power"]])
    while target > 0:
        choices.append(result[(i, target)["choice"]])
        i += 1
        target -= result[(i, target)["used"]]
    print("The choices maked are ", choices)


def Dp_by_rate_rec(n: int, result: dict, r: float, channels: list[object]):
    if (n + 1, r) in result.keys():
        return result[(n, r)]["rate"]
    min = float('inf')
    k = 0
    m = 0
    used = 0
    for user in channels[n].users:
        for power in user.powers:
            temp = power.p + Dp_by_rate_rec(n + 1, result, r - power.r, channels)
            if temp < min:
                min = temp
                k = user.index
                m = power.index
                used = power.r
    result[(n + 1, r)] = {"choice": (n + 1, k + 1, m + 1), "power": min, "used": used}