from __future__ import division
import sys
import math
from collections import deque, namedtuple
import operator

dbg = open('small.dbg', 'w')

sys.stdin = open('small.in')
sys.stdout = open('small.out', 'w')

class Quat(namedtuple('Quat', 'x i j k')):
	def __new__(cls, x=0, i=0, j=0, k=0):
		return super(Quat, cls).__new__(cls, x, i, j, k)

	def __mul__(self, other):
		if isinstance(other, (float, int)):
			other = Quat(x=other)

		return Quat(
			x=self.x*other.x - self.i*other.i - self.j*other.j - self.k*other.k,

			i=self.x*other.i + self.i*other.x - self.j*other.k + self.k*other.j,
			j=self.x*other.j + self.j*other.x - self.k*other.i + self.i*other.k,
			k=self.x*other.k + self.k*other.x - self.i*other.j + self.j*other.i
		)

	def __rmul__(self, other):
		if isinstance(other, (float, int)):
			other = Quat(x=other)

		return other.__mul__(self)

	def conj(self):
		return Quat(self.x, -self.i, -self.j, -self.k)

	def __abs__(self):
		return (
			self.x*self.x +
			self.i*self.i +
			self.j*self.j +
			self.k*self.k
		) ** 0.5

	def inv(self):
		return self.conj() * (1/ abs(self))

	def __str__(self):
		parts = []
		if self.x: parts += [(self.x, '')]
		if self.i: parts += [(self.i, 'i')]
		if self.j: parts += [(self.j, 'j')]
		if self.k: parts += [(self.k, 'k')]

		res = ''
		for v, suff in parts:
			if not res:
				if v < 0:
					res += "-"
					v = -v
			else:
				if v < 0:
					res += " - "
					v = -v
				else:
					res += " + "

			if not suff or v != 1: res += str(v)
			res += suff

		return res

	def __eq__(self, other):
		if isinstance(other, (float, int)):
			other = Quat(x=other)

		return super(Quat, self).__eq__(other)

	def __ne__(self, other):
		if isinstance(other, (float, int)):
			other = Quat(x=other)

		return super(Quat, self).__ne__(other)

	__repr__ = __str__

I = Quat(i=1)
J = Quat(j=1)
K = Quat(k=1)

def _collect(seq, func, first=None):
	seq = iter(seq)
	res = first or next(seq)
	yield res

	for x in seq:
		res = func(res, x)
		yield res

def collect(seq, func, first=None):
	return list(_collect(seq, func, first))

def solve(quats, repts):
	n = len(quats)

	fsum = collect(quats,           lambda t, x: t * x, first=1)
	bsum = collect(reversed(quats), lambda t, x: x * t, first=1)


	total_prod = 1
	for x in range(repts % 3):
		total_prod *= fsum[-1]

	if total_prod != 1:
		print >> dbg, "Total == {}^{} == {} != 1".format(fsum[-1], repts, total_prod)
		return "NO"

	print >> dbg, "In:  ", quats, '*', repts
	print >> dbg, "Fsum:", fsum
	print >> dbg, "Bsum:", bsum

	firstI = 0
	look_for = I
	for _ in range(3):
		try:
			firstI += fsum.index(look_for)
			break
		except ValueError:
			firstI += n
			look_for = fsum[-1].inv() * look_for
	else:
		print >> dbg, "No I"
		return "NO"

	lastK = 0
	look_for = K
	for _ in range(3):
		try:
			lastK -= bsum.index(look_for)
			break
		except ValueError:
			lastK -= n
			look_for = bsum[-1].inv() * look_for
	else:
		print >> dbg, "No K"
		return "NO"

	lastK += n * repts

	if lastK > firstI:
		if n * repts < 100:
			all_quats = quats * repts
			print >> dbg, "IJK: ", all_quats[:firstI], all_quats[firstI:lastK], all_quats[lastK:]
		else:
			all_quats = quats * 3
			print >> dbg, "I K: ", all_quats[:firstI], all_quats[lastK % (3*n):]
		return "YES"

	else:
		print >> dbg, "Too short - I = [:{}], K = [{}:]".format(firstI, lastK)
		return "NO"

t = int(raw_input())

for i in range(t):
	l, x = map(int, raw_input().split())
	chars = list(raw_input())

	assert len(chars) == l

	quats = [Quat(**{c: 1}) for c in chars]

	print >> dbg, "Case #{}:".format(i+1)
	res = solve(quats, repts=x)
	print "Case #{}: {}".format(i+1, res)
	print >> dbg, res
	print >> dbg
