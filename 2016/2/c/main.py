import sys
import numpy as np

from collections import defaultdict

def diff_cyc(a, b, L):
	d = (a - b) % L
	if d > L // 2:
		d -= L
	return d

print(diff_cyc(8, 1, 8))

def solve(R, C, courtiers):
	grid = np.empty((R, C), dtype='c')
	grid[...] = '!'

	N = 2*(R + C)

	print(R, C, courtiers)

	by_dist = defaultdict(set)

	for a, b in courtiers:
		by_dist[abs(diff_cyc(a, b, N))].add((a, b))

	print(by_dist)

	for a, b in by_dist[1]:
		a, b = sorted([a, b])
		if a > C:
			


	return b'\n'.join(
		b''.join(row)
		for row in grid
	).decode('ascii')

sys.stdin = open('sample.in')
# sys.stdout = open('small.out', 'w')

T = int(input())

for i in range(T):
    R, C = (int(x) for x in input().split())
    courtiers = [int(x) for x in input().split()]
    courtiers = [e for e in zip(courtiers[::2], courtiers[1::2])]
    res = solve(R, C, courtiers)
    print("Case #{}:\n{}".format(i+1, res))