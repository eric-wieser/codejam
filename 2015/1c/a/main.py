from __future__ import division
import sys
import math
from collections import defaultdict
import numpy as np

which = 'large'

sys.stdin = open('{}.in'.format(which))
sys.stdout = open('{}.out'.format(which), 'w')


def solve(r, c, w):
	return r * ((c + w-1) // w) + (w - 1)


t = int(raw_input())

for i in range(t):
	r, c, w = [int(c) for c in raw_input().split()]
	res = solve(r, c, w)
	print "Case #{}: {}".format(i+1, res)
