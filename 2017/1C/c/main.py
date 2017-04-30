import sys
import itertools
import numpy as np

which = "sample"

def prob_n(event_probs):
    """
    Takes in the probability of a list of independant events
    Return p[i] = n(events) == i
    """
    event_probs = np.asarray(event_probs)

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

def solve(N, K, U, P):

    P = np.array(sorted(P))

    if N == K:
        Pnew = P.copy()
        Uleft = U
        i = 1
        while i < len(P):
            diff = P[i] - P[i-1]
            if Uleft > diff * i:
                Pnew[:i] += diff
                Uleft -= diff * i
            else:
                break
            i += 1

        Pnew[:i] += Uleft / i

        # print(U, P, Pnew)

    else:
        Pnew = P.copy()
        def p_without(i):
            rest = np.concatenate((Pnew[:i], Pnew[i+1:]))
            return prob_n(rest)[K-1]

        while True:
            best = min([
                i
                for i in range(len(Pnew))
                if P[i] != 1
            ], key=p_without)

            if Pnew[best] + U < 1:
                Pnew[best] += U
                break
            else:
                U -= (1 - Pnew[best])
                Pnew[best] = 1

    return prob_n(Pnew)[K:].sum()


sys.stdin = open('{}.in'.format(which))
# sys.stdout = open('{}.out'.format(which), 'w')

T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    U = float(input())
    P = list(map(float, input().split()))
    res = solve(N, K, U, P)
    print("Case #{}: {:.8f}".format(i+1, res))
