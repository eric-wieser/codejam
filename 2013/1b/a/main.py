import sys

sys.stdin = open('large.in')
sys.stdout = open('large.out', 'w')

def solve(armin_size, sizes):
	sizes = sorted(sizes)
	steps = 0

	for i, size in enumerate(sizes):
		add_count = 0
		remove_count = len(sizes) - i
		while armin_size <= size:
			armin_size += armin_size - 1
			add_count += 1

			if add_count >= remove_count:
				return steps + remove_count

		armin_size += size
		steps += add_count

	return steps

n = int(raw_input())

for i in range(n):
	size, _ = [int(x) for x in raw_input().split()]
	sizes = [int(x) for x in raw_input().split()]
	print "Case #{}: {}".format(i+1, solve(size, sizes))
