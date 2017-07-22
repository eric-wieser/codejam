import sys
import math

sys.stdin = open('small.in')
debug = sys.stdout
sys.stdout = open('small.out', 'w')

def odd_triangle_below(n):
	best = 0
	best_tri = 0
	for i in xrange(1, n + 1, 2):
		tri = i*(i+1)/2
		if tri > n:
			break
		else:
			best = i
			best_tri = tri

	return best, best_tri

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def partial_prob(x, n):
	return sum(nCr(n, i) for i in xrange(x+1)) * 0.5**n

# for n in range(8):
# 	print [partial_prob(x, n) for x in reversed(range(n))]
# 	print sum([partial_prob(x, n) for x in reversed(range(n))])

def solve(n, x, y):
	x = abs(x)
	i, t = odd_triangle_below(n)
	rest = n - t

	print >> debug, "    n >= T(%d)" % i
	if x + y < i:
		print >> debug, "    Within the triangle?"
		return 1
	elif x + y > i + 2 or rest == 0:
		return 0
	elif rest >= 2*(i + 1):
		print >> debug, "    both sides full"
		return 1 if i + 1 >= y else 0
	elif rest >= i + 2:
		rest -= i + 1
		print >> debug, "    One side full - other %d/%d"% (rest, i+1)
		if i < y:
			return 0
		elif y >= rest-1:
			return 0.5
		else:
			return 0
	else:
		print >> debug, "    ", i, rest, t
		print >> debug, "    hmmm %d %d" % (y, rest)
		return partial_prob(i  - y, rest)


n = int(raw_input())

for i in range(n):
	m, x, y = [int(x) for x in raw_input().split()]
	print "Case #{}: {}".format(i+1, solve(m, x, y))


def rec(a=0, b=0, depth=2):
	if depth != 0:
		return ((p + q) / 2 for p, q in zip(rec(a+1, b), rec(b+1, a)))
	else:
		return