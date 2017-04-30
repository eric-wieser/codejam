import sys
import itertools
import math
import collections

which = "large"


Activity = collections.namedtuple('Activity', 'who start end')

day = 24 * 60

def tdiff(end, start):
    return (end - start) % day

def n_to_exceed(vals, lim):
    vals = sorted(vals, reverse=True)
    val = 0
    i = 0
    while val < lim:
        val += vals[i]
        i += 1
    return i


def solve(act1, act2):
    busy1 = sum(a.end-a.start for a in act1)
    busy2 = sum(a.end-a.start for a in act2)

    schedule = sorted(act1 + act2, key=lambda a: a.start)

    swaps_needed = 0
    swap_buffers = []
    buffers1 = []
    buffers2 = []
    for ai, aj in zip(schedule, schedule[1:] + schedule[0:]):
        gap = tdiff(aj.start, ai.end)
        if ai.who != aj.who:
            swaps_needed += 1
            swap_buffers.append(gap)
        elif ai.who == 1:
            buffers1.append(gap)
        elif ai.who == 2:
            buffers2.append(gap)
        else:
            assert False

    swap_total = sum(swap_buffers)

    # person 1 fills all the changeover gaps
    leeway1 = busy1 + swap_total + sum(buffers1) - day / 2
    leeway2 = busy2 + swap_total + sum(buffers2) - day / 2

    if leeway1 < 0:
        return swaps_needed + 2 * n_to_exceed(buffers2, -leeway1)
    elif leeway2 < 0:
        return swaps_needed + 2 * n_to_exceed(buffers1, -leeway2)
    elif leeway1 >= 0 and leeway2 >= 0:
        return swaps_needed


sys.stdin = open('{}.in'.format(which))
sys.stdout = open('{}.out'.format(which), 'w')

T = int(input())

for i in range(T):
    Ac, Aj = map(int, input().split())
    act1 = [
        Activity(1, *map(int, input().split()))
        for i in range(Ac)
    ]
    act2 = [
        Activity(2, *map(int, input().split()))
        for i in range(Aj)
    ]
    res = solve(act1, act2)
    print("Case #{}: {}".format(i+1, res))
