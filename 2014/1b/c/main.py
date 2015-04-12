import sys
from collections import defaultdict


sys.stdin = open('sample.in')
# sys.stdout = open('large.out', 'w')


def solve(zips, flights):
	def find_best(it):
		return min(it, key=lambda c: zips[c])

	connects_to = defaultdict(set)

	for a, b in flights:
		connects_to[a].add(b)
		connects_to[b].add(a)

	stack = [0]

	def take_flight(start, end):
		connects_to[start].remove(end)
		connects_to[end].remove(start)
		stack.append(end)

		print "Fly from %s -> %s" % (start, end)

	for j in range(100):
		at = stack[-1]
		if connects_to[at] == {}:
			print "Return"
			stack.pop()
		else:
			islands = []

			island = {}
			for city, _ in enumerate(zips):
				if any()

			best = float('inf')
			isolated_stack = [
			    {child for child in connects_to[ancestor] if connects_to[child] == {ancestor}}
				for ancestor in stack
			]
			best_stack = [
			    connects_to[ancestor]
				for ancestor in stack
			]

			isolated_stack = [find_best(children) if children else None for children in isolated_stack]
			best_stack =     [find_best(children) if children else None for children in best_stack]

			i = -1

			for ancestor, isolated, best in reversed(zip(stack, isolated_stack, best_stack)):
				# if there are some cities only accessible through this one, we must pick from those
				if isolated:
					next_city = isolated
					take_flight(ancestor, next_city)

					print next_city

	return zips, connects_to

n = int(raw_input())

for i in range(n):
	cities_n, flights_n = [int(x) for x in raw_input().split()]
	zips = [int(raw_input()) for _ in range(cities_n)]
	flights = [
		set(int(x)-1 for x in raw_input().split())
		for _ in range(flights_n)
	]

	print "Case #{}: {}".format(i+1, solve(zips, flights))
