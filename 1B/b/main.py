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


def solve(ps, K):
	K2 = K // 2
	ps = sorted(ps)
	chosen = ps[:K2] + ps[-K2:]
	assert len(chosen) == K
	print(chosen, file=debug)
	return prob_n(chosen)[K2]

def solve_bad(ps, K):
	best = max(
		prob_n(subset)[K // 2]
		for subset in itertools.combinations(ps, K)
	)
	return best

debug = sys.stdout
sys.stdin = open('small.in')
sys.stdout = open('small.out', 'w')

T = int(input())

for i in range(T):
    N, K = (int(x) for x in input().split())
    ps = [float(p) for p in input().split()]
    assert len(ps) == N
    res = solve_bad(ps, K)
    print("Case #{}: {}".format(i+1, res))