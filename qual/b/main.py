import sys

sys.stdin = open('large.in')
sys.stdout = open('large.out', 'w')

def solve(data, w, h):
	row_maxs = [
		max(data[y][x] for x in range(w))
		for y in range(h)
	]
	col_maxs = [
		max(data[y][x] for y in range(h))
		for x in range(w)
	]
	return "YES" if not any(
		data[y][x] < row_maxs[y] and data[y][x] < col_maxs[x]
		for x in range(w)
		for y in range(h)
	) else "NO"

n = int(raw_input())

for i in range(n):
	h, w = [int(x) for x in raw_input().split()]
	rows = [
		[int(x) for x in raw_input().split()]
		for _ in range(h)
	]
	print "Case #{}: {}".format(i+1, solve(rows, w, h))
