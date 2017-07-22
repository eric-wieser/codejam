import sys

sys.setrecursionlimit(2000)

def solve(S):
    if len(S) == 1:
        return S
    if S[-1] >= max(S[:-1]):
        return S[-1] + solve(S[:-1])
    else:
        return solve(S[:-1]) + S[-1]

sys.stdin = open('large.in')
sys.stdout = open('large.out', 'w')

T = int(input())

for i in range(T):
    S = input()
    res = solve(S)
    print("Case #{}: {}".format(i+1, res))
