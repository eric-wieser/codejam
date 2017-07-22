import sys
import itertools
import math
import collections

which = "sample"


Ticket = collections.namedtuple('Ticket', 'seat buyer')

def solve(n_seats, n_buyers, tickets):
    if n_buyers != 2: return
    print(n_seats, n_buyers, tickets)

    by_seat = collections.defaultdict(set)
    by_buyer = collections.defaultdict(set)
    for t in tickets:
        by_seat[t.seat].add(t)
        by_buyer[t.buyer].add(t)

    print('seat', dict(by_seat))
    print('buyer', dict(by_buyer))
    print()


sys.stdin = open('{}.in'.format(which))
# sys.stdout = open('{}.out'.format(which), 'w')

T = int(input())

for i in range(T):
    N, C, M = map(int, input().split())
    tickets = [
        Ticket(*(int(x) -1 for x in input().split()))
        for i in range(M)
    ]
    res = solve(N, C, tickets)
    print("Case #{}: {}".format(i+1, res))
