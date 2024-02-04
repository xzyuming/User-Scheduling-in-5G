from queue import PriorityQueue
import numpy as np

class Node():
    def __init__(self, branch, bound, level, result = []):
        self.branch = branch
        self.bound = bound
        self.level = level
        self.result = result
    def __lt__(self, other):
        return self.bound > other.bound

def lp_solver(branch):
    pass
#   return bound, result

def is_integer_solution(result):
    return all(value %1 ==0 for value in result)

def branch_and_bound(lp_solver, N, K, M, p):

    init_bound = 0
    branch =  np.zeros()
    level = 0
    node = Node(branch, init_bound, level)
    q = PriorityQueue()
    q.put(node)

    current_feasible_solution = None
    current_feasible_bound = float('-inf')
    while q:
        node = q.get()
        new_branch = node.branch.copy()
        level = node.level +1
        for i in range(K):
            new_branch[level] = i
            new_bound, new_result = lp_solver(new_branch)
            node = Node(new_branch, new_bound, level, new_result)

            if node.bound <= current_feasible_bound:
                continue

            if is_integer_solution(node.result):
                current_feasible_solution = node.result
                current_feasible_bound = node.bound
                continue

            q.put(node)
    return current_feasible_solution, current_feasible_bound















