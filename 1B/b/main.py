import sys
import numpy as np
import itertools

def prob_n(event_probs):
    """
    Takes in the probability of a list of independant events
    Return p[i] = n(events) == i
    """
    # probability of an empty set of events is 1
    if len(event_probs) == 0:
        return np.array([1])

    # P(n(A,As...) == N) = P(a)P(n(As...) == N-1) + P(!a)P(n(As...) == N)
    first, rest = event_probs[0], event_probs[1:]

    res = np.zeros(len(event_probs) + 1)
    p_rest_n = prob_n(rest)
    res[1:] += first * p_rest_n
    res[:-1] += (1-first) * p_rest_n
    return res

def p_tie(ps):
	return prob_n(ps)[len(ps) // 2]

def solve_pairwise(ps, K):
	K2 = K // 2
	ps = sorted(ps)
	left = ps[:]
	chosen = []
	for i in range(K2):
		attempts = [
			([left[0], left[-1]], left[1:-1]),
			([left[0], left[1]], left[2:]),
			([left[-1], left[-2]], left[:-2])
		]
		chosen, left = max((
			(chosen + attempt, remain)
			for attempt,remain in attempts),
			key=lambda t: p_tie(t[0])
		)

	assert len(chosen) == K
	print(sorted(chosen), file=debug)
	return prob_n(chosen)[K2]

def solve_replace(ps, K):
	K2 = K // 2
	choose = set(range(K2)) | set(range(len(ps) - K2, len(ps)))
	assert len(choose) == K
	all_i = set(range(len(ps)))
	prob = p_tie([ps[i] for i in choose])

	while True:
		attempt = []
		for i in choose:
			for i2 in choose:
				for j in all_i - choose:
					for j2 in all_i - choose:
						if i == i2 or j == j2:
							add = {i}
							remove = {j}
						else:
							add = {i, i2}
							remove = {j, j2}
					choose_new = (choose - add) | remove
					prob_new = p_tie([ps[k] for k in choose_new])
					attempt.append((prob_new, choose_new))

		if not attempt:
			break

		prob_new, choose_new = max(
			attempt, key=lambda t: t[0]
		)
		if prob_new <= prob:
			break

		choose = choose_new
		prob = prob_new

	print(sorted([ps[i] for i in choose]), file=debug)
	return prob



def solve_bad(ps, K):
	best = max(
		itertools.combinations(ps, K),
		key=lambda subset: prob_n(subset)[K // 2]
	)
	print(sorted(best), file=debug)
	return prob_n(best)[K // 2]

debug = open('sample.debug', 'w')
sys.stdin = open('sample.in')
sys.stdout = open('sample.out', 'w')

T = int(input())

for i in range(T):
    print("Case #{}:".format(i+1), file=debug)
    N, K = (int(x) for x in input().split())
    ps = [float(p) for p in input().split()]
    assert len(ps) == N
    res = solve_replace(ps, K)
    print("Case #{}: {}".format(i+1, res))