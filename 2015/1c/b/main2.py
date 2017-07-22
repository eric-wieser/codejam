from __future__ import division
import sys
import math
import collections

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

def restart_point(word):
	for x in restart_points(word):
		yield x
		return

def word_chance(keyboard, word):


class Solver(object):
	def __init__(self, keyboard, word, length):
		self.keyboard = keyboard
		self.word = word
		self.lengh = length

		self.chances = collections.defaultdict(int)
		self.chances = collections.defaultdict(int)
		for c in self.keyboard:
			self.chances[c] = self.keyboard.count(c) / len(self.keyboard)

	def raw_prob(self, s):
		chance = 1
		for c in word:
			chance *= self.chances[c]

		return chance

	def raw_ways(self, s):
		ways = 1
		for c in word:
			ways *= self.keyboard.count(c)

		return ways

	def expected(self, existing, left):
		if len(word[existing:]) < left:
			return 0

		# chance of completion of word
		ex = self.raw_prob(word[existing:])

		sub_ex = sum( # expected subwords
			self.expected(rp, left - rp)
			rp in restart_points(word)
		) + sum(
			self.expected(0, left - existing)
		)

	def solve(self):
		self.words_from = [0] * self.length

		for i in range(self.length)[::-1]:
			if i + len(self.word) < self.length:
				self.words_from[i] = (
					self.raw_ways(self.word)
					+ sum(
						self.words_from[r]
						for r in [
							restart_points9
						]
					)

		while self.length > len(word):
			ex = self.raw_prob(word)
			for rp in restart_points(word)
				ex += self.raw_prob(word[rp:]

def solve(keyboard, word, length):
	expected = 1

	while length > len(word):
		ex = word_chance(keyboard, word)
		for rp in restart_points(word)
			ex += word_chance(keyboard)
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