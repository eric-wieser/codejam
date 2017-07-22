import sys
import math
import itertools

sys.stdin = open('small.in')
debug = sys.stdout
sys.stdout = open('small.out', 'w')

def valid(train):
	seen = set()
	last = None
	for c in train:
		if c != last and c in seen:
			return False
			seen.add(c)
			last = c
	return True

def flatten(word):
	def gen():
		last = None
		for c in word:
			if c != last:
				yield c
			last = c
	return ''.join(gen())


def solve(words):
	words = map(flatten, words)
	n = 0
	for train in itertools.permutations(words):
		if valid(itertools.chain.from_iterable(train)):
			n += 1

	return n % 1000000007

t = int(raw_input())

for i in range(t):
	n = int(raw_input())
	words = raw_input().split()
	print >> debug, "Done {}".format(i)
	print "Case #{}: {}".format(i+1, solve(words))

