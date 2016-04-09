import sys

def solve(stack):
    print(stack)

sys.stdin = open('sample.in')

T = int(input())

for i in range(T):
    stack = input().strip()
    res = solve(stack)
    print("Case #{}: {}".format(i+1, res))
