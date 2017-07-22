from __future__ import division
import sys
import math
import collections

which = 'small.0'

dbg = open('{}.dbg'.format(which), 'w')
sys.stdin = open('{}.in'.format(which))
# sys.stdout = open('{}.out'.format(which), 'w')






def solve(keyboard, word, length):
	def restart_point():
		for i, _ in enumerate(word):
			if i == 0:
				continue

			if word.startswith(word[i:]):
				return i

	rp = restart_point()

	def raw_ways(s):
		ways = 1
		for c in s:
			ways *= keyboard.count(c)

		return ways

	words_from = [0] * length

	for i in range(length)[::-1]:
		left = length - i - len(word)

		if left < 0:
			continue


		words_from[i] = raw_ways(word) * len(keyboard) ** left
		if rp:
			words_from[i] += raw_ways(word) * words_from[i+rp]

		if left >= 1:
			words_from[i] += len(keyboard) **len(word) * words_from[i + len(word)]

		if i + 1 < length:
			words_from[i] += len(keyboard) * words_from[i + 1]

	print >> dbg, word, keyboard
	print >> dbg, words_from

	return words_from[0]

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

	real = solve(keyboard, word, length)

	print >> dbg, real, wc

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