from __future__ import division
import sys
import math
from collections import Counter

which = 'large'

sys.stdin = open('{}.in'.format(which))
sys.stdout = open('{}.out'.format(which), 'w')


def solve(counts):
	return min(
		sum((c - 1) // stack_size for c in counts) + stack_size
		for stack_size in range(1, max(counts)+1)
	)


t = int(raw_input())

for i in range(t):
	d = int(raw_input())
	counts = [int(c) for c in raw_input().split()]

	assert len(counts) == d
	print "Case #{}: {}".format(i+1, solve(counts))