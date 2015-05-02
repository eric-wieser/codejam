from __future__ import division
import sys
import math
from collections import defaultdict, namedtuple
import numpy as np
import matplotlib.pyplot as plt

Hiker = namedtuple('Hiker', 'd t')

which = 'sample'

dbg = open('{}.dbg'.format(which), 'w')
sys.stdin = open('{}.in'.format(which))
# sys.stdout = open('{}.out'.format(which), 'w')


def plot(hikers):
	t = np.arange(0, max(s for d, s in hikers), min(s for d, s in hikers) / 360)
	fig, ax = plt.subplots()
	for h in hikers:
		ax.plot(t, (h.d + t/h.t * 360) % 360)
	plt.show()

def solve(hikers):
	plot(hikers)
	for at, time in hikers:
		print at, time



t = int(raw_input())

for i in range(t):
	n = int(raw_input())

	hikers = []

	for _ in range(n):
		d, h, m = [int(c) for c in raw_input().split()]
		for duration in range(m, m+h):
			hikers.append(Hiker(d, duration))

	print >> dbg, "Case #{}:".format(i+1)
	res = solve(hikers)
	print "Case #{}: {}".format(i+1, res)
	print >> dbg, res
	print >> dbg