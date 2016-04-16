import sys
from collections import Counter, defaultdict

def solve(N, Fs):
    bff = {
        i: f for i, f in enumerate(Fs, 1)
    }

    two_cl = {
        frozenset([i, f]) for i, f in bff.items() if bff[f] == i
    }
    def chain_from(c):
        at = c
        seen = [c]
        seen_set = {c}
        for size in range(N):
            at = bff[at]
            if at == seen[0] and len(seen) != 2:
                return seen, True
            elif at in seen_set:
                if len(seen) >= 2 and seen[-2] == at:
                    return seen[:-1], False
                return seen, False
            seen.append(at)
            seen_set.add(at)
        raise ValueError

    chains = [chain_from(i) for i in bff.keys()]

    try:
        largest_loop = max(len(items) for items, closed in chains if closed)
    except ValueError:
        largest_loop = 0

    largest_by_dest = defaultdict(int)
    for items, closed in chains:
        last = items[-1]
        largest_by_dest[last] = max(largest_by_dest[last], len(items))

    if two_cl:
        largest_v = sum(
            largest_by_dest[a] + largest_by_dest[b] for a, b in two_cl
        )
    else:
        largest_v = 0

    return max(largest_loop, largest_v)


sys.stdin = open('large.in')
# sys.stdout = open('large.out', 'w')

T = int(input())

for i in range(T):
    N = int(input())
    Fs = [int(x) for x in input().split()]
    assert len(Fs) == N
    res = solve(N, Fs)
    print("Case #{}: {}".format(i+1, res))
