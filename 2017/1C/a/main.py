import sys
import itertools
import collections
import math

which = "small0"

class Pancake(collections.namedtuple('Pancake', 'r h')):
    @property
    def top_area(self):
        return math.pi * self.r * self.r

    @property
    def side_area(self):
        return 2 * math.pi * self.r * self.h

def solve_bad(sizes, K):
    sizes = sorted(sizes, key=lambda p: p.r, reverse=True)

    return max(
        stack[0].top_area + sum(p.side_area for p in stack)
        for stack in itertools.combinations(sizes, K)
    )

sys.stdin = open('{}.in'.format(which))
sys.stdout = open('{}.out'.format(which), 'w')

T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    sizes = [
        Pancake(*map(int, input().split()))
        for i in range(N)
    ]
    res = solve_bad(sizes, K)
    print("Case #{}: {}".format(i+1, res))
