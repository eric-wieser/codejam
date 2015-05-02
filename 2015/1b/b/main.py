from __future__ import division
import sys
import math
from collections import defaultdict
import numpy as np

which = 'small.1'

dbg = open('{}.dbg'.format(which), 'w')
sys.stdin = open('{}.in'.format(which))
sys.stdout = open('{}.out'.format(which), 'w')

"""
Fails for

[[0 1 0 1 0]
 [1 0 1 0 1]
 [0 1 0 1 0]]

 vs


[[1 0 1 0 1]
 [0 1 0 1 0]
 [1 0 1 0 1]]

"""

def tilings(r,c):
	"""number of gaps - corners, edges, centers, filled"""

	# vals: free, end, corner, edge, center

	if r == 1 and c == 1:
		yield [1, 0, 0, 0, 0]

	if c == 1:
		r, c = c, r

	if r == 1:
		if c % 2 == 0:
			yield [c//2, 1, c//2 - 1, 0, 0]
		else:
			yield [(c+1)//2, 0, (c-1)//2, 0, 0]
			yield [(c-1)//2, 2, (c-3)//2, 0, 0]


	if r % 2 == 0 or c % 2 == 0:
		vals = [0, 0, 0, 0, 0]
		vals[2] = 2
		vals[3] = r - 2 + c - 2
		if c > 2 and r > 2:
			vals[4] = (r - 2) * (c - 2) // 2

		vals[0] = r*c - sum(vals[1:])

		yield vals
	else:
		vals = [0, 0, 0, 0, 0]
		# empty corners
		vals[2]  = 4
		vals[3] = max(0, r - 3) + max(0, c - 3)
		if c > 2 and r > 2:
			vals[4] = ((r - 2) * (c - 2) + 1) // 2
		vals[0] = r*c - sum(vals[1:])

		yield vals

		vals = [0, 0, 0, 0, 0]
		# full corners
		vals[2] = 0
		vals[3] = r - 1 + c - 1
		if c > 2 and r > 2:
			vals[4] = ((r - 2) * (c - 2) - 1) // 2
		vals[0] = r*c - sum(vals[1:])

		yield vals


# print list(tilings(3,5))
# print list(tilings(1,5))

def solve(r, c, n):
	r, c = min(r, c), max(r, c)
	grid = np.ones((r, c), np.int32)
	neighbours = grid*4
	neighbours[0,:] -= 1
	neighbours[-1,:] -= 1
	neighbours[:,0] -= 1
	neighbours[:,-1] -= 1

	print >> dbg, "G:\n", grid
	print >> dbg, "N:\n", neighbours

	for i in range(0, r*c - n):
		weights = np.where(grid, neighbours, -1)

		x, y = np.unravel_index(weights.argmax(), grid.shape)

		if x+1 < r:  neighbours[x+1, y] -= 1
		if y+1 < c:  neighbours[x, y+1] -= 1
		if 0 <= x-1: neighbours[x-1, y] -= 1
		if 0 <= y-1: neighbours[x, y-1] -= 1

		grid[x, y] = 0
		print >> dbg, "G:\n", grid
		print >> dbg, "N:\n", neighbours

	count = np.sum(grid*neighbours)

	assert count % 2 == 0

	return count // 2

def cost(patt, n):

	res = 0
	for i in range(5):
		if n <= patt[i]:
			return res + n*i
		n -= patt[i]
		res += patt[i] * i

	raise ValueError




def solve2(r, c, n):
	patterns = list(tilings(r, c))
	print >> dbg, patterns
	return min(cost(p, n) for p in patterns)




t = int(raw_input())

for i in range(t):
	r, c, n = [int(c) for c in raw_input().split()]
	print >> dbg, "Case #{}:".format(i+1)
	res = solve2(r, c, n)
	print "Case #{}: {}".format(i+1, res)
	print >> dbg, res
	print >> dbg