import sys

dictionary = open('dictionary.txt').read().split()
sys.stdin = open('sample.in')
# sys.stdout = open('large.out', 'w')

def match(s, word, prev_i):
	changes = 0
	for i, (s_c, w_c) in enumerate(zip(s, word)):
		if s_c != w_c:
			if i > prev_i + 4:
				prev_i = i
				changes = changes + 1
			else:
				return False
	return prev_i, changes

def first_words(s, prev_i=-100):
	return filter(bool, ((word, match(s, word, prev_i)) for word in dictionary))

def solve(s):
	steps_to = [None]*len(s)

	steps_to[0] = 0

	for i in range(len(s)):
		remaining = s[i:]
		if steps_to[i] is None:
			continue

		for word in dictionary:
			if len(word) > len(remaining):
				continue

	print first_words(s)

	return "Nope"

n = int(raw_input())

for i in range(n):
	text = raw_input()
	print "Case #{}: {}".format(i+1, solve(text))
