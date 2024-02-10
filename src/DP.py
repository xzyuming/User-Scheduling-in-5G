
def Dp_by_power(target, *channels):
    result = {}
    Dp_by_power_rec(0, result, target, *channels)
    choices = []
    i = 1
    print("max rate is ", result[(i,target)]["rate"])
    used_power = 0
    while i<=len(channels):
        choices.append(result[(i,target)]["choice"])
        used_power+= result[(i,target)]["used"]
        target-= result[(i,target)]["used"]
        i+=1
    print("The choices made are ", choices)
    print("used power is", used_power)


def Dp_by_power_rec(n : int, result:dict, p:float, *channels):
    if (n+1, p) in result.keys():
        return result[(n+1,p)]["rate"]
    max = 0
    k = 0
    m = 0
    used = 0

    if(n>= len(channels)):
        return 0

    for user in channels[n].users:
        for power in user.powers:
            if power.p> p:
                continue
            temp = power.r + Dp_by_power_rec(n+1, result, p-power.p, *channels)

            if temp>max:
                max = temp
                k = user.index[1]
                m = power.index[2]
                used = power.p
    result[(n+1, p)]= {"choice" : (n+1, k, m), "rate" : max, "used": used}
    return result[(n+1,p)]["rate"]

def Dp_by_rate(target: float, *channels):
    result = {}
    Dp_by_rate_rec(0, result, target, *channels)
    choices = []
    i = 1
    print("The target rate is ", target)
    print("The power spent is ", result[(i, target)]["power"])
    rate = 0
    while i<= len(channels):
        choices.append(result[(i, target)]["choice"])
        rate += result[(i, target)]["used"]
        target -= result[(i, target)]["used"]
        i+=1
    print("The choices maked are ", choices)
    print("The rate attended is", rate)


def Dp_by_rate_rec(n: int, result: dict, r: float, channels: list[object]):
    if (n + 1, r) in result.keys():
        return result[(n+1, r)]["power"]
    min = float('inf')
    k = 0
    m = 0
    used = 0
    if n >= len(channels):
        return 0
    for user in channels[n].users:
        for power in user.powers:

            temp = power.p + Dp_by_rate_rec(n + 1, result, r - power.r, channels)

            if temp < min:
                min = temp
                k = user.index[1]
                m = power.index[2]
                used = power.r
    result[(n + 1, r)] = {"choice": (n + 1, k , m ), "power": min, "used": used}
    return result[(n+1, r)]["power"]