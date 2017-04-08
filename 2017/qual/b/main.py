import sys
import itertools
import math

which = "small0"

def solve(N):
    base10 = str(N)
    last = '0'
    for i, letter in enumerate(base10):
        if letter < last:
            break
        last = letter
    else:
        return N

    power = len(base10) - i
    power = 10**power
    N = N // power * power
    N -= 1
    return solve(N)


sys.stdin = open('{}.in'.format(which))
sys.stdout = open('{}.out'.format(which), 'w')

T = int(input())

for i in range(T):
    N = int(input())
    res = solve(N)
    print("Case #{}: {}".format(i+1, res))
