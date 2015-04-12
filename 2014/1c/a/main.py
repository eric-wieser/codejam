from __future__ import division
import sys
import math
from fractions import Fraction

sys.stdin = open('large.in')
sys.stdout = open('large.out', 'w')

def pow2(x):
	while x//2 *2 == x:
		x //= 2

	return x == 1

def solve(p, q):
	f = Fraction(p, q)

	test = Fraction(1, 2)

	if not pow2(f.denominator):
		return "impossible"

	for i in range(1, 41):
		if f >= test:
			assert f < test * 2
			# print "{} >= {}".format(f, test)
			return i
		test /= 2
		# print f

	return "impossible"

t = int(raw_input())

for i in range(t):
	p, q = map(int, raw_input().split('/'))
	print "Case #{}: {}".format(i+1, solve(p, q))
