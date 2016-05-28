import sys

def solve():
	pass

sys.stdin = open('sample.in')
# sys.stdout = open('small.out', 'w')

T = int(input())

for i in range(T):
    S = input()
    res = solve(S)
    print("Case #{}: {}".format(i+1, res))