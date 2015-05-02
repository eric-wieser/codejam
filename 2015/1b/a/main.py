from __future__ import division
import sys
import math
from collections import defaultdict
import numpy as np

which = 'sample'

sys.stdin = open('{}.in'.format(which))
# sys.stdout = open('{}.out'.format(which), 'w')


def solve(r, c, n):
	grid = np.ones(r, c)
	neighbours = grid*4
	neighbours[0,:] -= 1
	neighbours[-1,:] -= 1
	neighbours[:,0] -= 1
	neighbours[:,-1] -= 1

	print neighbours



t = int(raw_input())

for i in range(t):
	r, c, n = [int(c) for c in raw_input().split()]
	print solve(r, c, n)