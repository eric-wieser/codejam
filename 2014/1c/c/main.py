import sys
from collections import defaultdict


sys.stdin = open('small.in')
sys.stdout = open('small.out', 'w')
debug = open('debug.txt', 'w')

class Diamond(object):
	def __init__(self, w, h):
		if w < 3 or h < 3:
			raise ValueError

		w, h = sorted([w, h])

		self.w = w
		self.h = h
		self.grid = grid = {}

		for x in range(w):
			for y in range(h):
				self.grid[x, y] = '.'

		grid[1, 0] = grid[0, 1] = grid[w-2, h-1] = grid[w-1, h-2] = '#'

		x = 1
		y = 0
		while x < w - 1:
			grid[x, y] = '#'
			grid[w - x - 1, h - y - 1] = '#'
			x += 1
			y += 1
		while y < h - 1:
			grid[x, y] = '#'
			grid[w - x - 1, h - y - 1] = '#'
			y += 1


		self.perim = 2 * ((w - 2) + 1 + (h - w))
		self.area = w * (h - w + 3) - 4

		self.expand_top_next = True
		self.no_more_expansion = False
		self.expand_sides_by = w - 2

	def enlarge(self):
		if self.expand_sides_by > 0:
			self.area += self.expand_sides_by
			self.perim += 1

			x = self.w - 1
			y = self.expand_sides_by
			while y > 0:
				if self.expand_top_next:
					self.grid[x, y-1] = '#'
					if x != self.w - 1:
						self.grid[x, y] = '.'
				else:
					self.grid[self.w - x - 1, self.h - (y-1) - 1] = '#'
					if x != self.w - 1:
						self.grid[self.w - x - 1, self.h - (y) - 1] = '.'

				x -= 1
				y -= 1

			if not self.expand_top_next:
				self.expand_sides_by -= 1


		elif not self.no_more_expansion:
			if self.expand_top_next:
				self.grid[0, 0] = '#'

				self.area += 1
				self.perim += 1

			else:
				self.grid[self.w-1, self.h-1] = '#'

				self.area += 1
				self.perim += 1

				self.no_more_expansion = True

		else:
			raise ValueError

		self.expand_top_next = not self.expand_top_next


	def __str__(self):
		return "<Diamond {s.w}x{s.h} area={s.area} perim={s.perim}\n\t{disp}\n>".format(
			disp='\n\t'.join(
				''.join(self.grid[x, y] for x in range(self.w))
				for y in range(self.h)
			),
			s = self
		)


def try_bb(w, h):
	d = Diamond(w, h)
	while d.area < k:
		d.enlarge()

	return d


def solve(n, m, k):
	# no ability to enclose
	if n <= 2 or m <= 2:
		print >> debug, "Too small"
		return k
	if k < 4:
		print >> debug, "Too few"
		return k

	def bboxes():
		for w in range(3, n+1):
			for h in range(3, m+1):
				if w * h >= k:
					yield w, h

	n, m = sorted([n, m])

	diamonds = (try_bb(w, h) for w, h in bboxes())

	d = min(diamonds, key=lambda d: d.perim)
	print >> debug, (n, m, k), d
	return d.perim

t = int(raw_input())

for i in range(t):
	n, m, k = map(int, raw_input().split())

	print "Case #{}: {}".format(i+1, solve(n, m, k))
