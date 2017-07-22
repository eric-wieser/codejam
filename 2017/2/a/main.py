import sys
import itertools
import collections
import math
import heapq
import numpy as np

which = "large"

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
    mtot = np.sum(m)

    k_max = np.ones(U.shape, int) * mtot
    np.floor_divide(m, U, out=k_max, where=U!=0)
    k_max = k_max.min(axis=1)

    ks = np.indices(k_max + 1).reshape(4, -1)

    left_bym = m[:,None] - U.T @ ks

    invalid = np.any(left_bym < 0, axis=0, keepdims=True)
    left = np.sum(left_bym, axis=0, keepdims=True)
    left[invalid] = np.sum(m)


    best_i = np.argmin(left)
    k = ks[:,best_i]
    lbm = left_bym[:, best_i]

    print(k)
    print(lbm)

    return m0 + np.min(left)


def solve(groups, P):
    groups = np.array(groups)

    ms = np.sum(groups % P == np.arange(P)[:,None], axis=1)

    if P == 2:
        U = np.array([
            [2]
        ])
    elif P == 3:
        U = np.array([
            #1, 2
            [3, 0],
            [0, 3],
            [1, 1]
        ])
    elif P == 4:
        U = np.array([
            #1, 2, 3
            [4, 0, 0],
            [0, 2, 0],
            [0, 0, 4],
            [2, 1, 0],
            [1, 0, 1],
            [0, 1, 2]
        ])
    else:
        raise ValueError

    m = ms[1:]

    mtot = np.sum(m)

    k_max = np.ones(U.shape, int) * mtot
    np.floor_divide(m, U, out=k_max, where=U!=0)
    k_max = k_max.min(axis=1)

    ks = np.indices(k_max + 1).reshape(U.shape[0], -1)

    n_groups = U.T @ ks  #[size,ki]

    invalid = np.any(n_groups > m[:,None], axis=0, keepdims=True)
    happy = ks.sum(axis=0, keepdims=True)
    happy[invalid] = 0

    best_i = np.argmax(happy.ravel())
    best_happy = happy[:,best_i].squeeze()

    n = ms[0] + best_happy

    if n_groups[:,best_i].sum() != mtot:
        n += 1

    return n

solve(np.random.randint(0, 4, 100), 4)




# def solve(G, P):
#     if P == 2:
#         return solve2(G)
#     elif P == 3:
#         return solve3(G)
#     elif P == 4:
#         return solve4(G)
#     else:
#         raise ValueError

sys.stdin = open('{}.in'.format(which))
sys.stdout = open('{}.out'.format(which), 'w')

T = int(input())

for i in range(T):
    N, P = map(int, input().split())
    G = list(map(int, input().split()))
    assert len(G) == N
    res = solve(G, P)
    print("Case #{}: {}".format(i+1, res))
