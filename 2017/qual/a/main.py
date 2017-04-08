import sys
import itertools

which = "small0"

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))


def reprp(P):
    return ''.join('+' if p else '-' for p in P)

def flip(s, k, i):
    assert k + i  <= len(s)

    return s[:i] + [not p for p in s[i:i+k]] + s[i+k:]

def multiflip(s, k, ii):
    for i in ii:
        s = flip(s, k, i)
    return s

def solve(S, K):
    flipmax = len(S) - K + 1

    try:
        return next(
            len(flips)
            for flips in powerset(range(flipmax))
            if all(multiflip(S, K, flips))
        )
    except StopIteration:
        return "IMPOSSIBLE"

sys.stdin = open('{}.in'.format(which))
sys.stdout = open('{}.out'.format(which), 'w')

T = int(input())

for i in range(T):
    parts = input().split()
    S = [p == '+' for p in parts[0]]
    K = int(parts[1])
    res = solve(S, K)
    print("Case #{}: {}".format(i+1, res))
