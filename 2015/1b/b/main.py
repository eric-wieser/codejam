from __future__ import division
import sys
import math
from collections import defaultdict
import numpy as np

which = 'small.0'

dbg = open('{}.dbg'.format(which), 'w')
sys.stdin = open('{}.in'.format(which))
sys.stdout = open('{}.out'.format(which), 'w')


def solve(r, c, n):
	r, c = min(r, c), max(r, c)
	grid = np.ones((r, c), np.int32)
	neighbours = grid*4
	neighbours[0,:] -= 1
	neighbours[-1,:] -= 1
	neighbours[:,0] -= 1
	neighbours[:,-1] -= 1

	print >> dbg, "G:", grid
	print >> dbg, "N:", neighbours

	for i in range(0, r*c - n):

		x, y = np.unravel_index(np.where(grid, neighbours, -1).argmax(), grid.shape)

		if x+1 < r:  neighbours[x+1, y] -= 1
		if y+1 < c:  neighbours[x, y+1] -= 1
		if 0 <= x-1: neighbours[x-1, y] -= 1
		if 0 <= y-1: neighbours[x, y-1] -= 1

		grid[x, y] = 0
		print >> dbg, "G:", grid
		print >> dbg, "N:", neighbours

	count = np.sum(grid*neighbours)

	assert count % 2 == 0

	return count // 2



t = int(raw_input())

for i in range(t):
	r, c, n = [int(c) for c in raw_input().split()]
	print >> dbg, "Case #{}:".format(i+1)
	res = solve(r, c, n)
	print "Case #{}: {}".format(i+1, res)
	print >> dbg, res
	print >> dbg