import sys
import math
import itertools

def find_factor(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i

bases = range(2, 11)

def find_factors(s):
    factors = []
    for base in bases:
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

def solve_dumb(N, J):
    assert N%2 == 0
    n = N // 2
    factor = '1' + (n-1)*'0' + '1'
    factors = [int(factor, base) for base in bases]

    for i in itertools.product('01', repeat=n-2):
        s = ''.join(('1',) + i + ('1',))
        yield  s+s, factors
        J = J - 1
        if J == 0:
            return

debug = sys.stdout
sys.stdin = open('large.in')
sys.stdout = open('large.out', 'w')

T = int(input())

for i in range(T):
    N, J = map(int, input().split())
    res = solve_dumb(N, J)
    print("Case #{}:".format(i+1))
    for j, (num, factors) in enumerate(res):
        print(num, ' '.join(str(f) for f in factors))
        print(j, file=debug)
