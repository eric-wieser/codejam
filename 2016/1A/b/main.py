import sys
from collections import Counter

def solve(N, lists):
	c = Counter()

	for l in lists:
		c.update(l)

	needed = set()

	for height, count in c.items():
		if count % 2 != 0:
			needed.add(height)

	needed = sorted(needed)
	assert len(needed) == N

	return ' '.join(str(n) for n in needed)

sys.stdin = open('large.in')
sys.stdout = open('large.out', 'w')

T = int(input())

for i in range(T):
    N = int(input())
    lists = [
    	[int(x) for x in input().split()]
    	for i in range(2*N-1)
    ]
    assert all(len(l) == N for l in lists)
    res = solve(N, lists)
    print("Case #{}: {}".format(i+1, res))
