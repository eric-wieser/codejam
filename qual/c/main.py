import sys
import math
import itertools

def find_factor(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i


def find_factors(s):
    factors = []
    for base in range(2, 11):
        value = int(s, base)
        factors.append(find_factor(value))

    if not any(f is None for f in factors):
        return factors

def solve(N, J):
    for i in itertools.product('01', repeat=N-2):
        s = ''.join(('1',) + i + ('1',))
        res = find_factors(s)
        if res is not None:
            yield s, res
            J = J - 1

        if J == 0:
            return

debug = sys.stdout
sys.stdin = open('small.in')
sys.stdout = open('small.out', 'w')

T = int(input())

for i in range(T):
    N, J = map(int, input().split())
    res = solve(N, J)
    print("Case #{}:".format(i+1))
    for j, (num, factors) in enumerate(res):
        print(num, ' '.join(str(f) for f in factors))
        print(j, file=debug)
