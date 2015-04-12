from __future__ import division
import sys
import math

sys.stdin = open('large.in')
sys.stdout = open('large.out', 'w')

def flatten(s):
	def gen():
		last = None
		for c in s:
			if c != last:
				yield c
			last = c
	return ''.join(gen())

def minimum_changes(values):
	m = sum(values) / len(values)

	m1 = int(math.floor(m))
	m2 = int(math.ceil(m))
	m3 = sorted(values)[len(values) // 2]

	return sum(abs(v - m3) for v in values)

	return min(
		sum(abs(v - m1) for v in values),
		sum(abs(v - m2) for v in values),
		sum(abs(v - m4) for v in values)
	)


def counts(s):
	count = 1
	last = None
	for c in s:
		if c == last:
			count += 1
		else:
			if last is not None:
				yield count
				count = 1
			last = c
	yield count

def solve(strs):
	f = flatten(strs[0])
	if not all(f == flatten(s) for s in strs[1:]):
		return "Fegla Won"

	swaps = 0
	for c in zip(*(counts(s) for s in strs)):
		swaps += minimum_changes(c)

	return swaps

t = int(raw_input())

for i in range(t):
	n = int(raw_input())
	strs = [raw_input() for _ in range(n)]
	print "Case #{}: {}".format(i+1, solve(strs))
