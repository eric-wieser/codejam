import sys
import math

sys.stdin = open('small.in')
debug = sys.stdout
sys.stdout = open('small.out', 'w')

def solve(a, b, k):
	return sum(ai & bi < k for ai in range(a) for bi in range(b))




for ki in range(16):
	for ai in range(16):
		print >> debug, "{:2}".format(ai),
		print >> debug, "{:2}".format('|'),
		for bi in range(16):
			print >> debug, "{}".format('#' if ki > ai & bi else ' '),
		print >> debug
	print >> debug
	import time
	time.sleep(0.25)
n = int(raw_input())

for i in range(n):
	a, b, k = [int(x) for x in raw_input().split()]
	print "Case #{}: {}".format(i+1, solve(a, b, k))

