
from collections import deque, namedtuple
import operator

class Quat(namedtuple('Quat', 'x i j k')):
	def __new__(cls, x=0, i=0, j=0, k=0):
		return super(Quat, cls).__new__(cls, x, i, j, k)

	def __mul__(self, other):
		if isinstance(other, (float, int)):
			other = Quat(x=other)

		return Quat(
			x=self.x*other.x - self.i*other.i - self.j*other.j - self.k*other.k,

			i=self.x*other.i + self.i*other.x + self.j*other.k - self.k*other.j,
			j=self.x*other.j + self.j*other.x + self.k*other.i - self.i*other.k,
			k=self.x*other.k + self.k*other.x + self.i*other.j - self.j*other.i
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


print J * I * J * J