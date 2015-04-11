from __future__ import division
import sys
import math
from collections import Counter

sys.stdin = open('small.in')
# sys.stdout = open('small.out', 'w')

def solve(counts):
	specials = 0
	times = []

	counts = Counter(counts)

	print ""
	while True:
		first = max(counts)
		rest = counts - Counter({ first: counts[first] })
		print "\tCounts:", specials + first, counts

		times.append(specials + first)

		if first <= 3:
			break

		specials += counts[first]
		counts = rest + Counter({
			first - (first // 2): counts[first]
		}) + Counter({
			first // 2: counts[first]
		})

	return min(times)

t = int(raw_input())

for i in range(t):
	d = int(raw_input())
	counts = [int(c) for c in raw_input().split()]

	assert len(counts) == d

	print "Case #{}: {}".format(i+1, solve(counts))