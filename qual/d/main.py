import sys
import math
import itertools
import numpy as np

def solve(k, complexity, samples):
    to_visit = 0
    done = False
    students_at = []
    students_at_t = []
    while to_visit < k:
        step = 0
        step_t = ()
        for c in range(complexity):
            if to_visit >= k:
                next_i = 0
            else:
                next_i = to_visit
            step = k * step + next_i
            step_t += (next_i,)
            to_visit = to_visit + 1

        students_at.append(step)
        students_at_t.append(step_t)

    if len(students_at) > samples:
        return "IMPOSSIBLE"

    print(students_at_t, file=debug)
    return ' '.join(str(sa+1) for sa in students_at)

debug = sys.stdout
sys.stdin = open('large.in')
sys.stdout = open('large.out', 'w')

T = int(input())

for i in range(T):
    K, C, S = map(int, input().split())
    print("Case #{}:".format(i+1), file=debug)
    print("  K={} C={} S={}".format(K, C, S), file=debug)
    res = solve(K, C, S)
    print("Case #{}: {}".format(i+1, res))
