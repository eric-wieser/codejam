from __future__ import division
import sys
import math
from collections import defaultdict

which = 'sample'

dbg = open('{}.dbg'.format(which), 'w')
sys.stdin = open('{}.in'.format(which))
# sys.stdout = open('{}.out'.format(which), 'w')

class Solver(object):
	def __init__(self, coins, maxc, maxv):
		self.coins = coins
		self.maxc = maxc
		self.maxv = maxv

		self.populate()

	def populate(self):
		needed = [float('inf')] * self.maxv
		needed[0] = 0
		for coin in sorted(self.coins):
			for i in range(self.maxv):
				if i >= coin:
					needed[i] = min(
						needed[i],
						needed[i - coin] + 1,
					)

		self.needed_coins = needed

def solve(count, denominations, v):
	s = Solver(denominations, count, v)
	cant = [i for i, x in enumerate(s.needed_coins) if x > count]
	# return needed(keyboard, word, length
	print >> dbg, "Can't make", cant

t = int(raw_input())

for i in range(t):
	c, d, v = [int(x) for x in raw_input().split()]
	denominations = [int(coin) for coin in raw_input().split()]
	assert len(denominations) == d

	print >> dbg, "Case #{}: (C={}, D={}, V={})".format(i+1, c, denominations, v)
	res = solve(c, denominations, v)
	print "Case #{}: {}".format(i+1, res)
	print >> dbg, res
	print >> dbg