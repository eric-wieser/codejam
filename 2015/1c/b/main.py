from __future__ import division
import sys
import math
from collections import defaultdict

which = 'small.0'

dbg = open('{}.dbg'.format(which), 'w')
sys.stdin = open('{}.in'.format(which))
sys.stdout = open('{}.out'.format(which), 'w')


def restart_points(word):
	for i, _ in enumerate(word):
		if i == 0:
			continue

		if word.startswith(word[i:]):
			yield i

	yield len(word)

def word_chance(keyboard, word):
	chance = 1
	n = length(keyboard)
	for c in word:
		chance *= keyboard.count(c) / n

	return chance

def solve(keyboard, word, length):
	expected = 1

	while length > len(word):
		ex = word_chance(keyboard, word)
	print >> dbg, word + '#' * (length - len(word))
	print >> dbg, needed(keyboard, word, length)
	pass

def solve_bad(keyboard, word, length):
	import itertools
	wc = 0
	n = 0

	all_words = itertools.product(keyboard, repeat=length)
	best = 0

	for bad_word in all_words:
		n += 1
		wc_i = 0
		bad_word = ''.join(bad_word)
		for i in range(length):
			if bad_word[i:].startswith(word):
				wc_i += 1

		best = max(best, wc_i)
		wc += wc_i


	print >> dbg, keyboard, length, len(list(itertools.combinations(keyboard, length)))

	return best - wc / n

# def needed(keyboard, word, length):
# 	if set(keyboard) & set(word) != set(word):
# 		return 0

# 	for i, _ in enumerate(word):
# 		if i == 0:
# 			continue

# 		if word.startswith(word[i:]):
# 			break
# 	else:
# 		i = len(word)

# 	return 1 + (length - len(word)) // i



t = int(raw_input())

for i in range(t):
	k, l, s = [int(c) for c in raw_input().split()]
	keyboard = raw_input()
	assert len(keyboard) == k
	word = raw_input()
	assert len(word) == l


	print >> dbg, "Case #{}:".format(i+1)
	res = solve_bad(keyboard, word, s)
	print "Case #{}: {}".format(i+1, res)
	print >> dbg, res
	print >> dbg
	dbg.flush()