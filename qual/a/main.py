import sys

sys.stdin = open('sample.in')

def lines(data):
	rows = [
		[data[i][j] for i in range(4)]
		for j in range(4)
	]
	cols = [
		[data[j][i] for i in range(4)]
		for j in range(4)
	]
	diagonals = [
		[data[0][0], data[1][1], data[2][2], data[3][3]],
		[data[0][3], data[1][2], data[2][1], data[3][0]]
	]

	return rows + cols + diagonals

def solve(data):
	for line in lines(data):
		if all(x in 'XT' for x in line):
			return "X won"
		elif all(x in 'OT' for x in line):
			return "O won"

	if not any(d == '.' for row in data for d in row):
		return "Draw"
	else:
		return "Game has not completed"

n = int(raw_input())

for i in range(n):
	rows = [raw_input() for _ in range(4)]
	raw_input()
	print "Case #{}: {}".format(i+1, solve(rows))

