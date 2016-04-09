import sys
import itertools

def solve(N):
    if N == 0:
        return "INSOMNIA"

    seen = [False] * 10
    for i in itertools.count(1):
        prod = N * i
        for c in str(prod):
            seen[ord(c) - ord('0')] = True
        if all(seen):
            return prod

sys.stdin = open('small.in')
sys.stdout = open('small.out', 'w')

T = int(input())

for i in range(T):
    N = int(input())
    res = solve(N)
    print("Case #{}: {}".format(i+1, res))
