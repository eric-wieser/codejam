import sys
import math
import itertools
import numpy as np

def solve(k, complexity, samples):
    if samples != k:
        return "IMPOSSIBLE"

    step = 1
    for c in range(complexity - 1):
        step = k * step + 1

    sample_at = list(range(0, samples * step, step))

    return ' '.join(str(sa+1) for sa in sample_at)

debug = sys.stdout
sys.stdin = open('small.in')
sys.stdout = open('small.out', 'w')

T = int(input())

for i in range(T):
    K, C, S = map(int, input().split())
    res = solve(K, C, S)
    print("Case #{}: {}".format(i+1, res))
    print("  K={} C={} S={}".format(K, C, S), file=debug)
