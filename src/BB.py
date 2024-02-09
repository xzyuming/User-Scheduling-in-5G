from queue import PriorityQueue
import numpy as np
from Greedy import Imax
import copy
from  scheduling import *
class Node():
    def __init__(self, branch, bound, power, level, result = []):
        self.branch = branch
        self.bound = bound
        self.level = level
        self.result = result
        self.used_power = power
    def __lt__(self, other):
        return self.bound > other.bound

def greedy_solver(p, *channels): # Our greedy function
    arr = list(channels)
    N = len(channels)
    for i in range(N):
        rem, arr[i] = arr[i].LpRe()
    ILP = 1  # is this LP or ILP
    lmax = []  # range of every channel after ip-lp-dominated treatment
    T = []  # arrary to compare efficiency
    Pv = []  # p\r values
    Rv = []
    In = []  # indices
    budget = p
    # because of methods IP-LP-dominated treatment, every channel has at least two acceptable elements

    # initialization
    for i in range(N):
        Pv.append(arr[i][0].p)
        Rv.append(arr[i][0].r)
        In.append(arr[i][0])
        lmax.append(len(arr[i]))
        j = 0
        while arr[i][j + 1].p - arr[i][j].p == 0 and j <= lmax[i] - 2:
            j += 1
        if j == lmax[i] - 1 and arr[i][j].p - arr[i][j - 1].p == 0:
            T.append(0)
            continue
        T.append((arr[i][j + 1].r - arr[i][j].r) / (arr[i][j + 1].p - arr[i][j].p))

    k = 0
    l = [1 for i in range(N)]

    while (sum(Pv) < budget):
        if Imax(T) == -1:
            break
        k = Imax(T)
        Pv[k] = arr[k][l[k]].p
        Rv[k] = arr[k][l[k]].r
        In[k] = arr[k][l[k]]
        l[k] += 1
        if l[k] > lmax[k] - 1:
            T[k] = 0
            continue
        if arr[k][l[k]].p - arr[k][l[k] - 1].p != 0:
            T[k] = (arr[k][l[k]].r - arr[k][l[k] - 1].r) / (arr[k][l[k]].p - arr[k][l[k] - 1].p)

    xa = 0
    xb = 0
    use = sum(Pv)
    rat = sum(Rv)
    if (use > budget):
        ILP = 0
        rest = Pv[k] - (use - budget)
        a = l[k] - 1
        b = a - 1
        xa = (rest - arr[k][b].p) / (arr[k][a].p - arr[k][b].p)
        xb = 1 - xa
        use = budget
        rat = rat - xb * arr[k][a].r + xb * arr[k][b].r
        Pv[k] = {xb: arr[k][b].p, xa: arr[k][a].p}
        Rv[k] = xa * arr[k][a].r + xb * arr[k][b].r
        In[k] = {xb: arr[k][b], xa: arr[k][a]}

    return (ILP, rat, use),In
#   return bound, result


def branch_and_bound(*channels):
    K = channels[0].K
    init_bound = 0
    branch =  np.zeros()
    level = 0
    node = Node(branch, init_bound, 0, level)
    q = PriorityQueue()
    q.put(node)

    current_feasible_solution = None
    current_feasible_bound = float('-inf')
    used_power = 0

    while q:
        node = q.get()
        new_branch = node.branch.copy()
        data = copy.deepcopy(channels)
        for i, k in enumerate(new_branch):
            data[i].users = data[i].users[k]
        level = node.level +1
        for i in range(K):
            new_branch.append(i)
            new_bound, new_result = greedy_solver(data)
            node = Node(new_branch, new_bound[1], new_bound[2], level, new_result)

            if node.bound <= current_feasible_bound:
                continue

            if new_bound[0]:
                current_feasible_solution = node.result
                current_feasible_bound = node.bound
                used_power = node.used_power
                continue

            q.put(node)
    return current_feasible_solution, current_feasible_bound, used_power















