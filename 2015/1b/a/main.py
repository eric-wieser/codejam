from __future__ import division
import sys
import math
from collections import defaultdict
import numpy as np

which = 'sample'

sys.stdin = open('{}.in'.format(which))
# sys.stdout = open('{}.out'.format(which), 'w')


def solve(n):

	while n > 10:
		sn = str(n)
		snr = sn[::-1]
		steps = 0

		to_pow_10 = min(
			int(sn[0]) + int(sn[1:]),
			int(snr[0]) + int(snr[1:])
		)
		print to_pow_10
		steps += to_pow_10 + 9
		n = 10 ** (len(sn) - 1) - 9
		print n, steps


print solve(7542)

# t = int(raw_input())

# for i in range(t):
# 	n = int(raw_input())
# 	print solve(n)