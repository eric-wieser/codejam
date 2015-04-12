from __future__ import division
import sys
import math
from collections import deque
import itertools

from collections import namedtuple

sys.stdin = open('sample.in')
debug = open('debug.txt', 'w')
# sys.stdout = open('small.out', 'w')

def treize(words):
	return set(
		word[:i]
		for word in words
		for i in range(len(word)+1)
	)

def solve(words, n):
	def splits():
		for group in itertools.product(range(n), repeat=len(words)):
			print group

			servers = [[] for i in range(n)]
			for i, x in zip(group, words):
				servers[i].append(x)

			# check all servers have words
			if not all(servers):
				continue

			count = sum(
				len(treize(server))
				for server in servers
			)
			yield count


	c = list(splits())
	return max(c), c.count(max(c))


t = int(raw_input())

for i in range(t):
	m, n = map(int, raw_input().split())
	words = [
		raw_input().strip()
		for _ in range(m)
	]
	print "Case #{}: {}".format(i+1, solve(words, n))
