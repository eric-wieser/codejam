import sys

def round_for(L):
	if L == 'R':
		return 'RS'
	if L == 'S':
		return 'PS'
	if L == 'P':
		return 'PR'

def tournament_for(l, N):
	if N == 0: return l

	parents = round_for(l)
	return ''.join(
		sorted(
			tournament_for(p, N-1)
			for p in parents
		)
	)

def solve(N, R, P, S):
	trees = [tournament_for(letter, N)
			 for letter in 'PRS']
	try:
		return min(
			t
			for t in trees
			if t.count('P') == P and t.count('R') == R
		)
	except ValueError:
		return "IMPOSSIBLE"

sys.stdin = open('large.in')
sys.stdout = open('large.out', 'w')

T = int(input())

for i in range(T):
    N, R, P, S = (int(x) for x in input().split())

    res = solve(N, R, P, S)
    print("Case #{}: {}".format(i+1, res))