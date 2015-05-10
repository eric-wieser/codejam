from __future__ import division
import sys
import math
from collections import defaultdict

which = 'sample'

dbg = open('{}.dbg'.format(which), 'w')
sys.stdin = open('{}.in'.format(which))
# sys.stdout = open('{}.out'.format(which), 'w')


def solve(count, denominations, v):
	return needed(keyboard, word, length)
	pass

t = int(raw_input())

for i in range(t):
	c, d, v = [int(c) for c in raw_input().split()]
	denominations = [int(c) for c in raw_input().split()]
	assert len(denominations) == d

	print >> dbg, "Case #{}:".format(i+1)
	res = solve(c, denominations, v)
	print "Case #{}: {}".format(i+1, res)
	print >> dbg, res
	print >> dbg