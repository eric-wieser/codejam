from __future__ import division
import sys
import math


which = 'small'

dbg = open('{}.dbg'.format(which), 'w')

sys.stdin = open('{}.in'.format(which))
sys.stdout = open('{}.out'.format(which), 'w')

def solve(x, r, c):
	""" return True if tiling is always possible """

	lg, sm = max(r, c), min(r, c)

	print >> dbg, "{}x{} {}-omino".format(r, c, x)

	if (r*c) % x != 0:
		print >> dbg, "can't divide"
		return False

	elif x == 2:
		return True

	elif x > lg:
		print >> dbg, "1*x cannot be contained"
		return False

	elif (x + 1) // 2 > sm:
		print >> dbg, "an L shape doesn't fit"
		return False

	elif x >= 7:
		print >> dbg, "omino exists with a hole"
		return False

	elif x >= 2 * sm:
		print >> dbg, "baseline wider than height to force orientation, enough to reach top"
		return False


	return True

t = int(raw_input())

for i in range(t):
	x, r, c = map(int, raw_input().split())
	print >> dbg, "Case #{}:".format(i+1)
	possible = solve(x, r, c)
	print "Case #{}: {}".format(i+1, 'GABRIEL' if possible else 'RICHARD')
	print >> dbg, 'OK' if possible else 'Impossible'
	print >> dbg
