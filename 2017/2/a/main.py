import sys
import itertools
import collections
import math
import heapq
import numpy as np

which = "sample"

def ceildiv(a, b):
    return (a + (b-1)) // b

def solve2(groups):
    even = sum(g % 2 == 0 for g in groups)
    odd  = sum(g % 2 == 1 for g in groups)

    return even + ceildiv(odd, 2)

def solve3(groups):
    m0 = sum(g % 3 == 0 for g in groups)
    m1 = sum(g % 3 == 1 for g in groups)
    m2 = sum(g % 3 == 2 for g in groups)

    n = m0

    if m1 > m2:
        return m0 + m2 + ceildiv(m1 - m2, 3)
    else:
        return m0 + m1 + ceildiv(m2 - m1, 3)

def solve4(groups):
    m0 = sum(g % 4 == 0 for g in groups)
    m1 = sum(g % 4 == 1 for g in groups)
    m2 = sum(g % 4 == 2 for g in groups)
    m3 = sum(g % 4 == 3 for g in groups)


    U = np.array([
        [4, 0, 0],
        [2, 1, 0],
        [0, 2, 0],
        [1, 0, 1],
    ])
    m = np.array([m1, m2, m3])
    n = m0

    with np.errstate(divide='ignore'):
        k_max = (m / U).min(axis=1)
        k_max = np.where(np.isnan(k_max), 0, k_max).astype(int)

    ks = np.indices(k_max + 1).reshape(4, -1)

    left_bym = m[:,None] - U.T @ ks

    invalid = np.any(left_bym < 0, axis=0, keepdims=True)
    left = np.sum(left_bym, axis=0, keepdims=True)

    print(ks)
    print(left_bym)
    print(left)



    if m3 > m1:
        n += m1
        m3 -= m1
        m1 -= m1
    else:
        n += m3
        m3 -= m3
        m1 -= m3





def solve(G, P):
    if P == 2:
        return solve2(G)
    elif P == 3:
        return solve3(G)
    elif P == 4:
        return solve4(G)
    else:
        raise ValueError

sys.stdin = open('{}.in'.format(which))
# sys.stdout = open('{}.out'.format(which), 'w')

T = int(input())

for i in range(T):
    N, P = map(int, input().split())
    G = list(map(int, input().split()))
    assert len(G) == N
    res = solve(G, P)
    print("Case #{}: {}".format(i+1, res))
