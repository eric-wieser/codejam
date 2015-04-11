from __future__ import division
import sys
import math
from collections import deque

sys.stdin = open('small.in')
sys.stdout = open('small.out', 'w')

def solve(counts):
	clapping = 0
	needed = 0
	for shyness, count in enumerate(counts):
		if shyness > clapping:
			extras = shyness - clapping
			needed += extras
			clapping += extras

		clapping += count

	return needed

t = int(raw_input())

for i in range(t):
	line = raw_input().split()
	s_max = int(line[0])
	counts = [int(c) for c in line[1]]

	assert len(counts) == s_max + 1

	print "Case #{}: {}".format(i+1, solve(counts))
