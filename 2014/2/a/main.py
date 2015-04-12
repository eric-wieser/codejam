from __future__ import division
import sys
import math
from collections import deque

sys.stdin = open('large.in')
sys.stdout = open('large.out', 'w')

def solve(files, x):
	files = sorted(files)
	files = deque(files)
	count = 0

	while len(files) > 1:
		biggest = files.pop()
		if biggest + files[0] <= x:
			files.popleft()
		count += 1

	if files:
		count += 1

	return count

t = int(raw_input())

for i in range(t):
	n, x = map(int, raw_input().split())
	files = map(int, raw_input().split())
	assert len(files) == n
	print "Case #{}: {}".format(i+1, solve(files, x))
